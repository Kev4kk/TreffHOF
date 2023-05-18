import json

# Dictionary to store the summa values for each aasta
summa_values = {}
summa_kokku = {}
# Read the text file line by line
i = -1
with open('mentions.txt', 'r') as file:
    for line in file:
        i += 1
        # Parse each line as a JSON string
        json_data = json.loads(line)
        # Extract the aasta and summa values
        aasta = json_data['aasta']
        summa = json_data['summa']

        # Store the summa value for the corresponding aasta
        if aasta in summa_values:
            summa_values[aasta].append([json_data["nimi"], summa, i])
            summa_kokku[aasta]+= summa
        else:
            summa_values[aasta] = [[json_data["nimi"], summa, i]]
            summa_kokku[aasta] = summa

# Calculate the average summa for each aasta
average_values = {}
# print(summa_values.items())
for aasta, values in summa_values.items():
    if (len(values) <= 1):
        continue
    # print(values)
    sum_of_second_elements = sum(val[1] for val in values)
    average_values[aasta] = sum_of_second_elements / (len(values) - 1)


# Sort the average values in descending order
sorted_averages = sorted(average_values.items(), key=lambda x: x[1], reverse=True)
print("[")
# Print the average values in descending order
for aasta, average in sorted_averages:
    print("{" + f'"aasta": "{aasta}", "keskmine":{average}, "kokku": {summa_values[aasta]}' + "},")

print("]")
