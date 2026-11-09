import sys
import pandas as pd

# ---------- SETTINGS ----------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSkXostJ8Wzd1rppachcXMPt4z95OgFC6nSPaADRUE_ceqY3WrS0K0xxlQf5RgfW1Bcd4IbKVORz-Zl/pub?gid=0&single=true&output=csv"
analyse = "reform"
splitter = "restore"
share = 1.0
number_columns = ["reform", "winner", "restore"]
known_parties = ["Lab", "Con", "LD", "Grn", "Ref", "Ind", "SNP", "PC"]
# ------------------------------

seats = pd.read_csv(url)
problems = 0

# CHECK 1: blank cells
for name in seats[seats.isna().any(axis=1)]["name"]:
    print("CHECK: blank cell in the row for", name)
    problems += 1

# CHECK 2: text where a number should be
for col in number_columns:
    as_numbers = pd.to_numeric(seats[col], errors="coerce")
    for name in seats[as_numbers.isna() & seats[col].notna()]["name"]:
        print("CHECK:", col, "is not a number for", name)
        problems += 1
    seats[col] = as_numbers

# CHECK 3: numbers that can't be right
for name in seats[seats[analyse] > seats["winner"]]["name"]:
    print("CHECK:", analyse, "has more votes than the winner in", name)
    problems += 1

# CHECK 4: party labels we don't recognise
for name in seats[~seats["party"].isin(known_parties)]["name"]:
    print("CHECK: unrecognised party label for", name)
    problems += 1

# CHECK 5: the same seat entered twice
for name in seats[seats["name"].duplicated()]["name"]:
    print("CHECK:", name, "appears more than once")
    problems += 1

if problems > 0:
    print()
    print(problems, "problem(s) found. Fix the sheet before trusting any results.")
    input("Press Enter to close")
    sys.exit()

print("Checks passed:", len(seats), "rows look clean")

# Leave out contests the test doesn't suit
stv = seats[seats["system"] == "STV"]
for name in stv["name"]:
    print("Leaving out", name, "(STV: transfers already counted)")
seats = seats[seats["system"] != "STV"].copy()

# ---------- THE ANALYSIS (same as last session) ----------
seats["gap"] = seats["winner"] - seats[analyse]
seats["switched"] = seats[splitter] * share

stood = seats[seats[splitter] > 0]
lost = stood[stood["gap"] > 0]
flips = lost[lost["switched"] > lost["gap"]]

print()
print(flips[["date", "name", "party", "gap", splitter]].to_string(index=False))
print()
print(splitter, "stood in", len(stood), "contests;", analyse, "lost", len(lost), "of them")
print(len(flips), "of", len(stood), "would flip if", int(share * 100), "% of", splitter, "voters had backed", analyse)

input("Press Enter to close")