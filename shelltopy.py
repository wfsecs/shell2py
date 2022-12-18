filename = input('Script file: ')

f = open("script.py", "w")
f.write("import os \n")

with open(filename, 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        f.write(f"os.system('{line}') \n")

f.close()
