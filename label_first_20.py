import pandas as pd

PATH = "labels.csv"

df = pd.read_csv(PATH, keep_default_na=False)

for i in range(20):
    print("\n" + "=" * 70)
    print(f"POST {i + 1}/20")
    print("=" * 70)
    print(df.loc[i, "text"])
    print()

    while True:
        choice = input("[a] analysis  [n] non_analysis: ").strip().lower()

        if choice == "a":
            label = "analysis"
            break
        elif choice == "n":
            label = "non_analysis"
            break
        else:
            print("Enter a or n.")

    df.loc[i, "label"] = label
    df.loc[i, "note"] = "cold"

    # Save after every answer so progress is never lost.
    df.to_csv(PATH, index=False)

print("\nDone. First 20 are cold-labeled.")