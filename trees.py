"""
streettrees2.py

Output a CSV file of the sidewalk trees on Degraw st in Brooklyn,
"""

import sys
import csv   #Comma-Separated Values
import urllib.request

#Database is at
#https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35
url = "https://data.cityofnewyork.us/api/views/5rq2-4hqu/rows.csv"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error, file = sys.stderr)
    sys.exit(1)

#lines is a list of sequences of bytes.
lines = infile.readlines()
infile.close()

try:
    #Change lines into a list of strings of characters.
    lines = [line.decode("utf-8") for line in lines]
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(lines[0], end = "") #1st line in the CSV file is a line of column headers.

for line in lines[1:]:          #Each time around the loop, line is a string.
    reader = csv.reader([line]) #[line] is a list containing one string
    fields = next(reader)       #fields is a list of strings.

    if (fields[26] == "11231"
        and fields[7] == "Alive"
        and fields[25].endswith("DE GRAW STREET")
        and int(fields[25].split(maxsplit = 1)[0]) >= 100
        and int(fields[25].split(maxsplit = 1)[0]) <= 200):
        print(line, end = "")

sys.exit(0)
