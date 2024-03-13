import csv


def parseCsv():
    prefixes = []
    names = []
    titles = []
    with open("staff.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Iterate through each row in the CSV file
        for row in reader:
            # Append each element in the row to its corresponding column array
            prefixes.append(row[0])
            names.append(row[1])
            titles.append(row[2])

    # Now you have data in separate arrays for each column
    return prefixes, names, titles