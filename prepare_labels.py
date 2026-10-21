import pandas as pd

SOURCE = "data/dota2_source.csv"
OUTPUT = "labels.csv"

columns = [
    "text",
    "id",
    "subreddit",
    "meta",
    "time",
    "author",
    "ups",
    "downs",
    "authorlinkkarma",
    "authorkarma",
    "authorisgold",
]

df = pd.read_csv(
    SOURCE,
    header=None,
    names=columns,
    on_bad_lines="skip",
    encoding_errors="ignore",
)

df["text"] = df["text"].astype(str).str.strip()

# Remove junk / unusable entries
df = df[
    (df["text"].str.len() >= 150)
    & (df["text"].str.len() <= 1000)
    & (~df["text"].isin(["[deleted]", "[removed]", "nan"]))
]

df = df.drop_duplicates(subset=["text"])

sample = df.sample(n=200, random_state=42)

labels = pd.DataFrame({
    "text": sample["text"].tolist(),
    "label": [""] * 200,
    "note": [""] * 200,
})

labels.to_csv(OUTPUT, index=False)

print(f"Wrote {len(labels)} rows to {OUTPUT}")
print(labels.head())