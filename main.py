import requests
from bs4 import BeautifulSoup
import os
import json

# Folder path
folder_path = './infolehed2'

sf = open("students.txt", "r")
students = []

for rida in sf:
    spl = rida.split("_")
    if (spl[1] == "x"):
        continue
    students.append([f"{spl[2]} {spl[1]}", spl[0]])
    # print(students[-1])

i = -1
studentMentions = []
for student in students:
    i+=1
    print(student)
    mentions = []
    # Iterate over all filenames in the folder
    for filename in os.listdir(folder_path):
        # Full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            # Process the file
            # print(filename)
            f = open("./infolehed2/" + filename, "r")
            cntnt = f.read()
            f.close()
            cnt = cntnt.count(student[0])
            if (cnt == 0):
                continue
            mentions.append([cnt, filename])
    jsON = {"nimi": student[0], "aasta": student[1], "mentions": mentions}
    studentMentions.append(jsON)

def key_func(obj):
    return sum(subarray[0] for subarray in obj["mentions"])

print("DONE counting")

sorteeritud = sorted(studentMentions, key=key_func)
sorteeritud.reverse()
fend = open("mentions.txt", "w")
for student in sorteeritud:
    student["summa"] = key_func(student)
    fend.write(json.dumps(student) + "\n")

fend.close()
print("DONE writing")


