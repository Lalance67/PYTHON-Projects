import csv
grades = {
    "Lance": [90,85,80], 
    "Nate": [75,70,80]
    }
with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "grades"])
    for name, g in grades.items():
        writer.writerow([name, *g])
with open("grades.csv", "r") as f:
    content = csv.reader(f)
    for row in content:
        print(*row)