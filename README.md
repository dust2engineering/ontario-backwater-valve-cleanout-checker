# Ontario Backwater Valve & Cleanout Checker (OBC 7.4.6.4 / 7.4.7)

Two Part 7 rule sets that changed in the 2024 Ontario Building Code and are widely misremembered from the old code: backwater valve requirements (7.4.6.4 — the gate-valve option is gone) and cleanout size, spacing and locations (7.4.7 — including the new Table 7.4.7.2, which differs from the National Plumbing Code).

**Live web tool:** https://dust2engineering.github.io/ontario-backwater-valve-cleanout-checker/web/

## How it works

- Cleanouts: enter the drain size and get the minimum cleanout size and the maximum spacing for one-way and two-way rodding from Table 7.4.7.2.
- Backwater valves: the checker walks Sentences 7.4.6.4.(1) to (5) — the air-circulation prohibition, the normally-open single-dwelling exception, and the two Sentence (3) protection options (per-fixture valves below street level, or one valve below the upstream maintenance-hole cover for houses).
- Locations: the 7.4.7.1 list is included as data — note the 2024 tightening at inside leaders (1 m, not 3 m) and the relaxed first-maintenance-hole distance (75 m, not 30 m).

## Data in this repository

- `backwater-cleanout-data.json` — 7.4.6.4 sentences, the 7.4.7.1 location list, Table 7.4.7.2, maintenance-hole rules and 7.4.7.4 access rules as machine-readable JSON.
- Verified verbatim from the official 2024 Building Code Compendium, Part 7 (O. Reg. 163/24), and cross-checked against municipal 2024-change summaries. The NPC cleanout table differs (same-size cleanouts for NPS 3–4); this tool uses Ontario's NPS 3.

## Command line

```bash
python3 cleanout_checker.py --drain-nps 4 --backwater --fixtures-below-street yes
```

## Worked examples

- [example-restaurant-drain.txt](examples/example-restaurant-drain.txt)
- [example-house-backwater.txt](examples/example-house-backwater.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Plumbing. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
