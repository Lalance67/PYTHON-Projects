import csv

grades = {
    "Lance": [90,81,96],
    "Nate": [83, 95, 90]
}
ar = list()
with open("grades.csv", "w", newline = "") as f:
    write = csv.writer(f)
    for name, g in grades.items():
        write.writerow([name, *g])

with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    
    for row in reader: 
        ar.append(row)
        print(row)
avg = list()
for row in ar:
    ints = [int(item) for item in row if item.isdigit()]
    avg.append(sum(ints) / len(list(ints)))
print(*avg)
