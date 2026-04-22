import json

with open("data.json") as f:
    data = json.load(f)

print("TYPE:", type(data))

if isinstance(data, dict):
    print("TOP KEYS:", list(data.keys())[:10])