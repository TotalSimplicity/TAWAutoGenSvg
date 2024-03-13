import random
import csvparser

# Read the SVG template from file
with open("emptytag.txt", "r") as f:
    design = f.read()

# Parse CSV data
prefixes, names, titles = csvparser.parseCsv()

# Maximum characters allowed per line
masteri = 0

sheetnum = 1

def genSheet():
    global masteri
    global sheetnum
    i = 0
    # Copy the template for each sheet
    sheet_design = design
    while i <= 15:
        name = names[masteri]
        prefix = prefixes[masteri]
        title = titles[masteri]
        # Replace placeholders with actual data
        sheet_design = sheet_design.replace("NAME", name, 1)
        sheet_design = sheet_design.replace("PREFIX", prefix, 1)
        sheet_design = sheet_design.replace("TITLE", title, 1)
        i += 1
        masteri += 1
        print(masteri)
        if masteri == len(names):
            break
    # Write the filled sheet to a file
    with open(f"sheets/{sheetnum}filledsheet.svg", "w") as f:
        f.write(sheet_design)
        sheetnum+=1

# Generate sheets until reaching the maximum count
while masteri < len(names):
    genSheet()
