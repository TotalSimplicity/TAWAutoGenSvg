import random
import csvparser

with open("emptytag.txt", "r") as f:
    design = f.read()

prefixes, names, titles = csvparser.parseCsv()

masteri = 0

platesPerSheet = 7

sheetnum = 1

def genSheet():
    global masteri
    global sheetnum
    i = 0
    sheet_design = design
    while i <= platesPerSheet:
        name = names[masteri]
        prefix = prefixes[masteri]
        title = titles[masteri]
        sheet_design = sheet_design.replace("NAME", name, 1)
        sheet_design = sheet_design.replace("PREFIX", prefix, 1)
        sheet_design = sheet_design.replace("TITLE", title, 1)
        i += 1
        masteri += 1
        print(prefix + name)
        if masteri == len(names):
            break
    with open(f"sheets/{sheetnum}filledsheet.svg", "w") as f:
        f.write(sheet_design)
        sheetnum+=1

while masteri <= len(names):
    genSheet()
