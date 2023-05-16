import json
import os
failinimi = "mentions"
f = open(failinimi+".txt", encoding="utf-8")

obj = []
for rida in f:
    obj.append(json.loads(rida))

f.close()

json_data = json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
with open(failinimi+".json", "w", encoding="utf-8") as file:
    file.write(json_data)


os.system(f"sed -i 's/$/,/' {failinimi}.json")