import pathlib
def isemp(file):
    if file.read() == "":
        f.seek(0)
        return 1
    else: 
        f.seek(0)
        return 0

def line(line_count, file):
    content = file.readlines()
    print(content)
    return content[line_count - 1]

file_path = pathlib.Path("data.txt")
if file_path.exists():
    print("file exist\n\n")
else: 
    print("file dont exist\n\n")
    exit()

f = open("data.txt", "r")
if isemp(f):
    print("file is empty")
else:
    ans = int(input("Enter line: "))
    content = line(ans, f)
    print(f"line {ans}: {content}")

f.close()
