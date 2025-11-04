import pandas as pd
import json

def debug(msg):
    print(f"[DEBUG] {msg}")

# 1. Load CSVs
halts = pd.read_csv("wienerlinien-ogd-haltepunkte.csv", sep=";", encoding="utf-8")
haltestellen = pd.read_csv("wienerlinien-ogd-haltestellen.csv", sep=";", encoding="utf-8")
linien = pd.read_csv("wienerlinien-ogd-linien.csv", sep=";", encoding="utf-8")
fahrwege = pd.read_csv("wienerlinien-ogd-fahrwegverlaeufe.csv", sep=";", encoding="utf-8")

debug(f"halts: {len(halts)} rows")
debug(f"haltestellen: {len(haltestellen)} rows")
debug(f"linien: {len(linien)} rows")
debug(f"fahrwege: {len(fahrwege)} rows")

# 2. Clean StopID columns
halts['StopID'] = pd.to_numeric(halts['StopID'], errors='coerce')
halts = halts.dropna(subset=['StopID'])
halts['StopID'] = halts['StopID'].astype(int)

# 3. Filter only Vienna
halts = halts[halts['Municipality']=='Wien']

# 4. Optionally merge haltestellen if  platform info needed
stops = pd.merge(halts, haltestellen, on='DIVA', how='left', suffixes=('_halt','_station'))

# 5. Merge with fahrwegverlaeufe and linien to get line info
fahrwege['LineID'] = pd.to_numeric(fahrwege['LineID'], errors='coerce')
fahrwege = fahrwege.dropna(subset=['LineID'])
fahrwege['LineID'] = fahrwege['LineID'].astype(int)

linien['LineID'] = pd.to_numeric(linien['LineID'], errors='coerce')
linien = linien.dropna(subset=['LineID'])
linien['LineID'] = linien['LineID'].astype(int)

stops = pd.merge(stops, fahrwege, left_on='StopID', right_on='StopID', how='left')
stops = pd.merge(stops, linien, left_on='LineID', right_on='LineID', how='left')

# 6. Create final JSON
output = []
for _, row in stops.iterrows():
    if pd.isna(row['StopID']):
        continue
    output.append({
        "stopId": int(row['StopID']),
        "stopName": row['StopText'],
        "line": row['LineText'],
        "direction": row['Direction'],
        "platform": row.get('PlatformText', None)
    })

debug(f"Total stops collected: {len(output)}")

with open("stops.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
debug("Generated stops.json")
