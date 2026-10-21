# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does
TakeMeter classifies public posts/comments from r/DotA2 into two categories: `analysis` and `non_analysis`. The goal is to distinguish posts that support a Dota 2 claim with concrete reasoning or evidence from posts that do not provide supporting reasoning or evidence. The classifier will be fine-tuned on posts collected and labeled from r/DotA2.
<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->



---

## Label Taxonomy
### `analysis`

**Definition:** Makes a Dota 2 claim and supports it with a specific reason, statistic, mechanic explanation, patch detail, item/build reasoning, or other concrete evidence.

**Example 1:**
> looks like you always take mid since you have low win rates with most mid heroes and high win rate with supports try letting invoker have mid and they might do better

**Example 2:**
> phoenix is the ridiculously good counter to lone druid that most people do nt know about the reason is the spirit bear attacks do not count on the egg ... so lone will have to use his hero attacks if he wants to destroy the egg

### `non_analysis`

**Definition:** Does not support a Dota 2 claim with concrete reasoning or evidence; includes reactions, questions, requests, suggestions, jokes, complaints, praise, predictions, and unsupported opinions.

**Example 1:**
> as an alliance fanboy i just wan na give big props to vega they played amazing and i wish them the best of luck against eg sucks vega wont go to shanghai

**Example 2:**
> sorry i have to mention my special friend brunz who was the asshole invoker at the end i forgot to put him in the credits and he was upset

### The hardest boundary

**Which two labels:** `analysis` and `non_analysis`

**The decision rule I used every time:** If a post makes a claim and gives concrete reasoning or evidence supporting that claim, I label it `analysis`. Otherwise, I label it `non_analysis`.

---


## The Dataset

**Where the posts came from:**  
I used historical public r/DotA2 comments from a public Reddit dataset. I sampled longer comments so that there was enough context to apply my taxonomy consistently.

**How I labelled them:**  
I created a dataset of 150 posts. I labelled 20 posts completely cold without AI assistance. I had AI assistance on an earlier group of 20 while I was refining the taxonomy, and AI pre-labelled the remaining 110 posts. I then read and reviewed every AI pre-labelled post and either kept or corrected its label.

I used 150 examples rather than the requested 200 because I reached the assignment's minimum submission size while working under the available time. The notebook warns about this, and I would collect more examples in a larger version of the project.

**Counts per label:**

| Label | Count | Share |
|---|---:|---:|
| `analysis` | 93 | 62% |
| `non_analysis` | 57 | 38% |
| **Total** | **150** | **100%** |

**Three hard cases**

**1.**
> **The post:** "if i m not playing pubs i pick the remaining position in ranked games ... it seems when people do nt get carry roles they go jungle instead and ruin the game"

> **Could have been:** `analysis` or `non_analysis`

> **I chose, because:** I chose `non_analysis` because although it makes a claim about player behavior, it does not provide concrete evidence or specific examples supporting that claim.

**2.**
> **The post:** "you know how i got that challenge ... two autowins and the last one i rushed hard with leshrac max edict"

> **Could have been:** `analysis` or `non_analysis`

> **I chose, because:** I chose `analysis` because the writer explains how the challenge was completed and supports the explanation with specific events from the matches, even though the evidence is anecdotal.

**3.**
> **The post:** "i m unsure why everyone in here is saying the admins ca nt do this ... the teams agreed to this scheduling system ..."

> **Could have been:** `analysis` or `non_analysis`

> **I chose, because:** This was difficult because it contains reasoning about the tournament rules, but I originally labelled it `non_analysis`. It showed me that distinguishing an argued opinion from a general reaction can be subjective.

## The Training Run

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate `2e-5`, batch size 16, seed 42, maximum sequence length 128.

**Anything I changed from the defaults, and why:**  
I did not change the training hyperparameters from the notebook defaults. I only changed the label list to match my taxonomy: `analysis` and `non_analysis`.

**Split sizes:**  
104 training examples, 23 validation examples, and 23 test examples. The test split contained 14 `analysis` examples and 9 `non_analysis` examples.

The model was trained on CPU.

The completed training run achieved 0.609 overall accuracy and 0.378 macro F1. The `analysis` label had an F1 of 0.757, while `non_analysis` had an F1 of 0.000. I am recording these results without changing my acceptance criteria because those criteria were written before training.


---

## How I Used AI

**Moment 1**

- **What I asked for:** I asked AI to help me think through a simple taxonomy for Dota 2 posts and to stress-test the boundary between supported analysis and unsupported reactions or opinions.
- **What came back:** AI suggested starting with `analysis` and `reaction`, but while labelling posts I noticed that many posts were questions, jokes, requests, or suggestions that did not fit `reaction` well.
- **What I changed:** I broadened the second label to `non_analysis` and used a simpler rule: a claim with concrete supporting reasoning or evidence is `analysis`; otherwise it is `non_analysis`.

**Moment 2**

- **What I asked for:** I used AI to help pre-label a portion of the collected r/DotA2 posts after I had defined my taxonomy and completed a cold-labeling batch.
- **What came back:** AI produced suggested `analysis` or `non_analysis` labels for the remaining examples.
- **What I changed:** I reviewed each AI-pre-labelled row myself and kept or corrected the suggested label based on my written decision rule.

**Pre-labelling disclosure:**  
AI was used to assist with 20 early examples while I refined the taxonomy and to pre-label 110 additional examples. I separately labelled 20 examples cold without AI assistance. I manually reviewed all 110 pre-labelled examples before using the dataset for training.


<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
