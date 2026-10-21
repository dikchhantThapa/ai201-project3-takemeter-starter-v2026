import csv

PATH = "labels.csv"

with open(PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

def save():
    with open(PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        writer.writeheader()
        writer.writerows(rows)

for i in range(40, len(rows)):
    print("\n" + "=" * 70)
    print(f"REVIEW {i - 39}/{len(rows) - 40}")
    print("=" * 70)
    print(rows[i]["text"])
    print()
    print(f"AI label: {rows[i]['label']}")

    while True:
        choice = input("[Enter] keep  [a] analysis  [n] non_analysis: ").strip().lower()
        if choice == "":
            break
        elif choice == "a":
            rows[i]["label"] = "analysis"
            break
        elif choice == "n":
            rows[i]["label"] = "non_analysis"
            break
        else:
            print("Press Enter, a, or n.")

    rows[i]["note"] = "AI pre-labeled; reviewed"
    save()

print("\nDone. All AI pre-labeled rows were reviewed.")
counts = {}
for row in rows:
    counts[row["label"]] = counts.get(row["label"], 0) + 1
print(counts)
