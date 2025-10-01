import json

tasks = [
    {"task": "study", "done": False},
    {"task": "workout", "done": True},
    {"task": "eat", "done": True},
    {"task": "bath", "done": False},
    {"task": "meditate", "done": False},
]
with open("tasks.json", "w") as f:
    json.dump(tasks, f)
inc = list()
with open("tasks.json", "r") as f:
    content = json.load(f)
    for i in content:
         if list(i.values())[1] == False:
                inc.append(i)
print("+--- INCOMPLETE TASKS ---+")
for i in inc:
     print(f"{i["task"]}: incomplete")

