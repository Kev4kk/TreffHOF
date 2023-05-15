import json
import matplotlib.pyplot as plt

# Set the backend to Agg
plt.switch_backend("Agg")

# Path to the text file
file_path = "mentions.txt"

# List to store the "summa" values
summa_values = []

# Read the text file line by line
with open(file_path, "r") as file:
    for line in file:
        try:
            json_object = json.loads(line)
            summa = json_object.get("summa")
            if summa is not None:
                summa_values.append(summa)
        except json.JSONDecodeError:
            print("Invalid JSON string:", line)

# Create the bar chart
plt.bar(range(len(summa_values)), summa_values)

# Add labels and title
plt.xlabel("Indeks")
plt.ylabel("Mainimisi infolehes")
plt.title("Tulpdiagramm: indeks vs mainimisi infolehes")

# Save the plot to a file
plt.savefig("bar_chart.png")

# Close the plot
plt.close()

# Path to the text file
file_path = "teacherMentions.txt"

# List to store the "summa" values
summa_values = []

# Read the text file line by line
with open(file_path, "r") as file:
    for line in file:
        try:
            json_object = json.loads(line)
            summa = json_object.get("summa")
            if summa is not None:
                summa_values.append(summa)
        except json.JSONDecodeError:
            print("Invalid JSON string:", line)

# Create the bar chart
plt.bar(range(len(summa_values)), summa_values)

# Add labels and title
plt.xlabel("Indeks")
plt.ylabel("Mainimisi infolehes")
plt.title("Tulpdiagramm: indeks vs mainimisi infolehes")

# Save the plot to a file
plt.savefig("bar_chart_teachers.png")

# Close the plot
plt.close()