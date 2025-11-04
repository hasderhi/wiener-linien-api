import json
from collections import defaultdict

# load clean stops file
with open("stops_clean.json", "r", encoding="utf-8") as f:
    stops = json.load(f)

groups = defaultdict(set)

for stop in stops:
    name = stop["stopName"].strip()
    sid = stop["stopId"]
    if sid:
        groups[name].add(sid)

# convert to list format
result = [
    {
        "name": name,
        "stops": sorted(list(ids))
    }
    for name, ids in groups.items()
]

# sort alphabetically by station name
result.sort(key=lambda x: x["name"].lower())

# save
with open("stops_grouped.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Grouped {len(result)} stations into stops_grouped.json")
