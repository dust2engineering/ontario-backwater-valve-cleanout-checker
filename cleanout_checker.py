#!/usr/bin/env python3
"""Ontario backwater valve + cleanout checker (OBC 2024, 7.4.6.4 and 7.4.7).
Usage:
  python3 cleanout_checker.py --drain-nps 4
  python3 cleanout_checker.py --backwater --fixtures-below-street yes --single-dwelling yes
"""
import argparse
def cleanout(nps):
    if nps < 3: return ("same size as the drain", 7.5, 15)
    if nps <= 4: return ("NPS 3", 15, 30)
    return ("NPS 4", 26, 52)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drain-nps", type=float, default=None)
    ap.add_argument("--backwater", action="store_true")
    ap.add_argument("--fixtures-below-street", choices=["yes", "no"], default="no")
    ap.add_argument("--single-dwelling", choices=["yes", "no"], default="no")
    a = ap.parse_args()
    if a.drain_nps:
        size, one, two = cleanout(a.drain_nps)
        print(f"Drain NPS {a.drain_nps:g}: minimum cleanout {size}; maximum spacing {one:g} m (one-way rodding) / {two:g} m (two-way). [Table 7.4.7.2, OBC 2024]")
        if a.drain_nps >= 8:
            print("Building sewer NPS 8 or larger: the cleanout shall be a maintenance hole, at every junction and change of slope, size or direction. [7.4.7.1 / 7.4.7.2]")
    if a.backwater:
        print("Backwater valves - 7.4.6.4:")
        print(" - A valve that obstructs free air circulation is NOT permitted on a building drain or sewer, except a normally-open type (CAN/CSA-B70/B181.1/B181.2/B182.1) on a building drain serving not more than one dwelling unit.")
        if a.fixtures_below_street == "yes":
            print(" - Fixtures below the level of the adjoining street: install a backwater valve on each fixture drain - OR, for a house on a municipal sanitary sewer, one valve protecting all fixtures below the cover level of the upstream sanitary maintenance hole. Several fixtures on one floor may share a valve on their branch.")
        else:
            print(" - No fixture below street level reported: Sentence (3) protection is triggered where the drain or branch may be subject to backflow - confirm the local flood level with the municipality.")
if __name__ == "__main__":
    main()
