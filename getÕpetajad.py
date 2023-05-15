import requests
from bs4 import BeautifulSoup
import json
import os
import re

def replace_last_name_with_value(string):
    # Extract the last name and the value within brackets
    pattern = r"\s(\w+)\s*\((\w+)\)"
    match = re.search(pattern, string)

    if match:
        last_name = match.group(1)
        value_in_brackets = match.group(2)

        # Replace the last name with the value within brackets
        replaced_string = string.replace(last_name, value_in_brackets)
        return replaced_string.split(" (")[0]

    return string  # Return the original string if no match is found

def search_by_nimi(nimi_value):
    with open("mentions.txt", 'r') as file:
        for line in file:
            json_data = json.loads(line)
            if json_data['nimi'] == nimi_value:
                return json_data
    return None

url = "https://www.htg.tartu.ee/tootajad"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <u> tags and extract the text between them
u_tags = soup.find_all("u")
text_array = list(set([tag.get_text().strip() for tag in u_tags]))

# Print the extracted text array
# print(text_array)

# tuleb lahutada kõik mainimised nendest, mis on nende õpilastena mentions.txt-is

õpetajad = []



for õpetaja in text_array:
    if õpetaja == "Tööleping peatatud":
        continue
    print(õpetaja)
    obj = {"nimi": õpetaja, "summa": 0, "mentions":[]}

    nimi = õpetaja.split(" (")[0]

    mainimisiÕpilasena = 0
    if "(" in õpetaja: # kui on neiupõlvenimi
        
        vananimi = replace_last_name_with_value(õpetaja)

        result = search_by_nimi(nimi)
        if result is not None:
            mainimisiÕpilasena = result["summa"]
        
        for filename in os.listdir("./infolehed3"):
            file_path = os.path.join("./infolehed3", filename)
        
            # Check if the current item is a file
            if os.path.isfile(file_path):        
                f = open("./infolehed3/" + filename, "r")
                cntnt = f.read()
                f.close()
                cnt = cntnt.count(nimi)
                cnt += cntnt.count(vananimi)
                if (cnt == 0):
                    continue
                obj["mentions"].append([cnt, filename])
                obj["summa"] += cnt
        obj["summa"] -= mainimisiÕpilasena
        õpetajad.append(obj)
        



    else: # ühe perekonnanimega
        result = search_by_nimi(nimi)
        if result is not None:
            mainimisiÕpilasena = result["summa"]
        
        for filename in os.listdir("./infolehed3"):
            file_path = os.path.join("./infolehed3", filename)
        
            # Check if the current item is a file
            if os.path.isfile(file_path):        
                f = open("./infolehed3/" + filename, "r")
                cntnt = f.read()
                f.close()
                cnt = cntnt.count(nimi)
                if (cnt == 0):
                    continue
                obj["mentions"].append([cnt, filename])
                obj["summa"] += cnt

        obj["summa"] -= mainimisiÕpilasena
        õpetajad.append(obj)
    # print(obj)  

def key_func(obj):
    return obj["summa"]


sorteeritud = sorted(õpetajad, key=key_func)
sorteeritud.reverse()

fend = open("teacherMentions.txt", "w")
for õp in sorteeritud:
    fend.write(json.dumps(õp) + "\n")
fend.close()
print("DONE writing")