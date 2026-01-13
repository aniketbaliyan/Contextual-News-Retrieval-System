import json

with open("../data/raw/news_data1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total articles:", len(data))
print("First article:")
print(data[0])
