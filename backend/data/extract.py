import pandas as pd
import json

def debug(msg):
    print(f"[DEBUG] {msg}")

# --- 1. Load CSVs ---
halts = pd.read_csv("wienerlinien-ogd-haltepunkte.csv", sep=";", encoding="utf-8")
haltestellen = pd.read_csv("wienerlinien-ogd-haltestellen.csv", sep=";", encoding="utf-8")
linien = pd.read_csv("wienerlinien-ogd-linien.csv", sep=";", encoding="utf-8")
fahrwege = pd.read_csv("wienerlinien-ogd-fahrwegverlaeufe.csv", sep=";", encoding="utf-8")

debug(f"halts: {len(halts)} rows")
debug(f"haltestellen: {len(haltestellen)} rows")
debug(f"linien: {len(linien)} rows")
debug(f"fahrwege: {len(fahrwege)} rows")

# --- 2. Clean StopID columns ---
halts['StopID'] = pd.to_numeric(halts['StopID'], errors='coerce')
halts = halts.dropna(subset=['StopID'])
halts['StopID'] = halts['StopID'].astype(int)

# --- 3. Keep only Vienna stops ---
halts = halts[halts['Municipality']=='Wien']

# --- 4. Merge haltestellen for platform info ---
stops = pd.merge(halts, haltestellen, on='DIVA', how='left', suffixes=('_halt','_station'))

# --- 5. Merge with fahrwege and linien ---
fahrwege['LineID'] = pd.to_numeric(fahrwege['LineID'], errors='coerce')
fahrwege = fahrwege.dropna(subset=['LineID'])
fahrwege['LineID'] = fahrwege['LineID'].astype(int)

linien['LineID'] = pd.to_numeric(linien['LineID'], errors='coerce')
linien = linien.dropna(subset=['LineID'])
linien['LineID'] = linien['LineID'].astype(int)

stops = pd.merge(stops, fahrwege, left_on='StopID', right_on='StopID', how='left')
stops = pd.merge(stops, linien, left_on='LineID', right_on='LineID', how='left')

debug(f"Rows after merging line info: {len(stops)}")

# --- 6. Drop rows with missing line/direction ---
stops = stops[stops['LineText'].notna() & stops['Direction'].notna()]
debug(f"Rows after dropping NaNs in line/direction: {len(stops)}")

# --- 7. Deduplicate ---
stops = stops.drop_duplicates(subset=['StopID','LineText','Direction'])
debug(f"Rows after deduplication: {len(stops)}")

# --- 8. Group multiple lines per stop ---
grouped = stops.groupby(['StopID','StopText','PlatformText']).agg({
    'LineText': lambda x: list(x.unique()),
    'Direction': lambda x: list(x.unique())
}).reset_index()

# --- 9. Prepare final JSON ---
output = []
for _, row in grouped.iterrows():
    output.append({
        "stopId": int(row['StopID']),
        "stopName": row['StopText'],
        "lines": row['LineText'],
        "directions": row['Direction'],
        "platform": row['PlatformText']
    })

debug(f"Total stops in final JSON: {len(output)}")

with open("stops_clean.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
debug("Generated stops_clean.json")
