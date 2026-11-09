import csv
import urllib.request
import matplotlib.pyplot as plt

# ---------- SETTINGS ----------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSkXostJ8Wzd1rppachcXMPt4z95OgFC6nSPaADRUE_ceqY3WrS0K0xxlQf5RgfW1Bcd4IbKVORz-Zl/pub?gid=0&single=true&output=csv"
analyse = "reform"      # the party we are analysing (a column heading)
splitter = "restore"    # the party whose vote might have split it (a column heading)
share = 0.25             # share of splitter voters assumed to switch: 1.0 = all, 0.5 = half
only_stood = True       # True = only show seats where the splitter stood
# ------------------------------

text = urllib.request.urlopen(url).read().decode("utf-8")
seats = list(csv.DictReader(text.splitlines()))

stood = 0
rows = []
for s in seats:
    if int(s[splitter]) > 0:
        stood = stood + 1
    gap = int(s["winner"]) - int(s[analyse])
    switched = int(s[splitter]) * share
    if gap > 0:
        if int(s[splitter]) > 0 or only_stood == False:
            rows.append((gap, s["name"], switched))

rows.sort()

names = []
gaps = []
switches = []
flagged = 0
for gap, name, switched in rows:
    names.append(name)
    gaps.append(gap)
    switches.append(switched)
    if switched > gap:
        flagged = flagged + 1

plt.figure(figsize=(12, 7))
plt.barh(names, gaps, label="Margin " + analyse + " lost by")
plt.barh(names, switches, alpha=0.5, label=splitter + " voters switching (" + str(int(share * 100)) + "%)")
plt.gca().invert_yaxis()
plt.legend()
plt.title("Where the " + splitter + " split could have cost " + analyse + " the seat\n"
          + str(flagged) + " of " + str(stood) + " contests where " + splitter + " stood would flip if "
          + str(int(share * 100)) + "% of its voters had backed " + analyse)
plt.xlabel("Votes")
plt.tight_layout()
plt.savefig("C:/Users/UserPC/Downloads/restore_chart.png", dpi=150)
plt.show()