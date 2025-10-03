import pathlib

ans = input("Enter filename to open (.txt): ")
file_path = pathlib.Path(f"{ans}.txt")
if file_path.exists():
    print(f"file {ans}.txt found")
    with open(f"{ans}.txt", "r")as f:
        print("contents: ")
        print(f.read())
else: print("file {ans}.txt not found")