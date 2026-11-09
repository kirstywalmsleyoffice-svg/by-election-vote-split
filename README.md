# By-election vote split tracker

**Question:** In UK council by-elections, how often is Restore Britain's vote bigger than Reform UK's losing margin, so that Restore's presence could plausibly have changed the result?

## Result (October 2026)

Restore stood in 10 first-past-the-post council by-elections. Reform lost 8 of them.

| Share of Restore voters assumed to switch to Reform | Results that would change |
|---|---|
| All | 5 of 10 |
| Half | 4 of 10 |
| A quarter | 3 of 10 |

With only 10 contests the uncertainty is large: the underlying rate is plausibly anywhere from about one in four to three in four. I report counts rather than percentages until the sample is bigger.

## Method

- For each seat Reform lost: gap = winner's votes minus Reform's votes.
- A seat is flagged if (Restore's votes × assumed switching share) is bigger than the gap.
- The data is checked before analysis: blanks, non-numbers, impossible values, unrecognised party labels and duplicate seats stop the program.
- Scottish contests (STV) are excluded, because voters' transfers are already counted.

## Limitations

- **The key assumption is untested.** We don't know how Restore voters would have voted if Restore hadn't stood: they might have backed Reform, someone else, or stayed home. The switching share is a dial, not evidence.
- **Small sample.** One month of results.
- **Selection.** Restore chooses where to stand, so these contests may not be typical.

## Files

- `pandas_tracker.py` — the main analysis, with data checks
- `simulate.py` — a simulation checking how often a result like this could arise by chance
- `chart.py` — bar chart of losing margins against Restore's vote
- `seats_2026-11-09.csv` — data snapshot used for the results above

Data entered by hand from council declarations of results.
