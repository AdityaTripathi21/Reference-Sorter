# script to format references

import re


# Function takes in a reference string and produces 3 keys, author surname, year, year suffix, and the string as a 4-tuple
def parser(entry):
    author_key = entry.split(",")[0].strip().lower()

    match = re.search(r"\b(\d{4})([a-z]?)\b", entry)
    if match:
        year = int(match.group(1)) # if year was 2024a, match.group(0) would be entire string
        suffix = match.group(2)
    else:
        year = float("inf")
        suffix = ""

    return (author_key, year, suffix, entry)

# function that takes the 4-tuple and returns a 3-tuple for the sort keys
def sort_key(item):
    return (item[0], item[1], item[2])

# open the file to read
with open("references.txt", encoding="utf-8-sig") as f: # utf-8-sig gets rid of BOM characters (invisible characters)
    text = f.read()

# entries - array that stores each ref 
entries = []
seen = set() # set for getting rid of duplicate refs in O(1)

for e in text.split("\n"):
    cleaned = e.strip()
    if cleaned and cleaned not in seen:
        entries.append(cleaned)
        seen.add(cleaned)

# parsed - array that stores each parsed ref, basically an array of 4-tuples
parsed = []
for e in entries:
    parsed.append(parser(e))

parsed.sort(key=sort_key)

# array that stores the sorted refs
sorted = []

for p in parsed:
    sorted.append(p[3])

for s in sorted:
    print(s)
    print()

# writing to a file (output)
with open("sorted_references.txt", "w") as f:
    for s in sorted:
        f.write(s + "\n\n")

