#!/usr/bin/env python3
"""List lesson steps whose `asOf` date (YYYY-MM) is more than 12 months old.

Prints a notice and never fails the run: an old date means a person should recheck
the fact, not that the build is broken.
"""
import datetime
import glob
import json

today = datetime.date.today()
now = today.year * 12 + today.month
old, dated = [], 0
for path in sorted(glob.glob("content/lessons/*.json")):
    lesson = json.load(open(path, encoding="utf-8"))
    for unit in lesson["units"] + [lesson["test"]]:
        for step in unit["steps"]:
            if "asOf" in step:
                dated += 1
                year, month = map(int, step["asOf"].split("-")[:2])
                if now - (year * 12 + month) > 12:
                    old.append(f"{step['id']} ({step['asOf']})")
print(f"asOf check: {dated} dated steps, {len(old)} older than 12 months")
for item in old:
    print("  recheck", item)
