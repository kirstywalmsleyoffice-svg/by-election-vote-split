import random

# ---------- SETTINGS ----------
true_rate = 0.17    # pretend this is the real rate
contests = 11       # how many contests in each pretend October
seen = 5            # what we actually saw
runs = 10000        # how many pretend Octobers to play out
# ------------------------------

def one_october(rate, n):
    flips = 0
    for i in range(n):
        if random.random() < rate:
            flips = flips + 1
    return flips

as_many = 0
for run in range(runs):
    if one_october(true_rate, contests) >= seen:
        as_many = as_many + 1

print("If the true rate were", int(true_rate * 100), "%,")
print(as_many, "of", runs, "pretend Octobers had", seen, "or more flips")
print("That's", round(as_many / runs * 100, 1), "%")

input("Press Enter to close")