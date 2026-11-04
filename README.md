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

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

r/cooking

A community where home cooks post recipes, ask for help, and talk about
technique and ingredients. My classifier sorts posts by what the post is
*doing* — not by whether it's any good. Three candidate distinctions I saw
while reading:

- **Help requests** — the poster has a specific problem and wants it solved
  ("how do I make tofu flavourful?", "where should I probe a ribeye?").
- **Showcases** — the poster shares something they made or a swap they tried
  ("my fajita soup recipe", "mayo in meatballs — don't knock it").
- **Discussions** — open questions inviting the community to share opinions or
  favorites ("what's your favorite spice?", "hand-pulled vs cut noodles?").

---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `help`

**Definition:** The poster has a specific cooking problem or question and wants a concrete answer or fix. The person is asking about their own dish or problem. 


**Example 1:**
>  *How to make tofu flavourful?* — 
> I know, I know. Age old question. I’ve tried crumbling it, shredding it, marinating overnight, even freezing it then cutting it once thawed. No matter what I do, I can’t make my tofu flavourful.
> My only success was when I made a coconut curry with tofu, but then every bite of tofu also had some sauce/soup. I want to eat more tofu that just curries though. What more can I do?

> https://www.reddit.com/r/Cooking/comments/1x4wksg/how_to_make_tofu_flavourful/




**Example 2:**
> *Where should I probe a ribeye?* — 
> Hey all,
> Every time I cook a ribeye on the stovetop (stainless steel pan, sear, flip, baste in butter), it ends up medium when I’m aiming for medium rare.
> The weird part is the temperature readings. When I probe the middle of the steak I always get a low number, but the fat cap reads much higher. Tonight I pulled it when the center hit 108°F and the cap was already at 137°F. After a 5-minute rest it was a perfect medium when I cut into it. 
> These big temperature swings seem to only happen with ribeyes. Is this a common thing, or am I doing something wrong?
> I’m starting to think I should just probe the cap from now on, since the center reading never seems to line up with the final doneness.

> https://www.reddit.com/r/Cooking/comments/1x4kewz/where_should_i_probe_a_ribeye/


### `showcase`

**Definition:** The poster shares a dish, recipe, result, or swap they made or tried, presented as a statement rather than a question.

**Example 1:**
> *My "fajita soup" recipe* — 
> Fajita soup
> 2 lb ground chicken
> 4-6 cups chicken stock
> 1 Onion diced
> 2 packets taco seasoning
> 2 cups rice
> 1 can Goya black beans
> 5-6 cloves of garlic
> 1-3 green peppers, chopped
> 2 tablespoons olive oil
> Juice of 2 limes
> Small dash of Beer to add liquid/acidity to meat
> Brown ground chicken with olive oil in a large Dutch oven and add taco seasoning. Add the juice of 1 of the limes and add beer. Once browned, remove chicken and add another tablespoon of oil to begin cooking onion, garlic, and green peppers with the other lime until onions are golden/translucent. Add rice, beans, and chicken stock and then bring to a boil. Simmer for about 15 minutes or until rice is cooked and liquid has largely evaporated. Garnish with cilantro and tortilla chips. Can add cheese or sour cream as desired.
> What do you all think? I came up with this recipe and mostly did it without precise measurements so these are estimates.

> https://www.reddit.com/r/Cooking/comments/1xbbiul/my_fajita_soup_recipe/

**Example 2:**
> *Mayo in meatballs* — 
> "Don’t knock it until you try it. I once recently out of eggs and needed a quick substitute. This was the best thing I could think of at the time thinking mayo is made out of eggs anyway!!! It ended up turning out amazing and I probably will do it again ! know it sounds super weird and probably super American LOL but if you are out of eggs and in a pinch I approve this swap 🙂"


> https://www.reddit.com/r/Cooking/comments/1xaonvl/mayo_in_meatballs/



### `discussion`

**Definition:** The poster asks an open-ended question inviting the community to share opinions, favorites, or experiences, with no single correct answer. The person is asking a general question to everyone.

**Example 1:**
>  *What's your favorite spice?* — 
> "Mine is definitely chilli pepper. I add it to everything."

> https://www.reddit.com/r/Cooking/comments/1x4i6ro/whats_your_favorite_spice/

**Example 2:**
> *Which is better: hand pulled noodles or cut noodles?* — 
> Weither for pan fried noodles or soup noodles, which is better, hand pulled noodles (like la mian or biangbiang or any other type) or the ones cut by hand? Like what difference it makes between the 2? Is it chewiness, or does any of the 2 holds sauce better, or what?

> https://www.reddit.com/r/Cooking/comments/1x4ix03/which_is_better_hand_pulled_noodles_or_cut_noodles/






### The hardest boundary

**Which two labels:** showcase vs discussion

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->

Classify by the point of the post. If the main idea if that the poster is presenting their own dish, recipe, or result, it is `showcase`, even if it ends with "what do you think?". If the main idea is inviting others to contribute theirs, it is `discussion`. A title phrased "what's your favorite X?" is `discussion` even when the poster also shares their own answer.

---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**
All the posts came from r/Cooking. I collected 87 real posts for this milestone. Each row is the post title and the first part of the body. 


**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
I labelled the first 15 posts as "cold", just by myself using my own rules for labeling. For the remaining 72 posts, I used an AI tool to pre-label them first. Then, I went over all of them and fixed any label that I felt was wrong. These are marked as "pre_label"

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| help | 23 | 26% |
| showcase | 28 | 32% |
| discussion | 36 | 42% |
| **Total** | 87 | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*  "What's your favorite use for the $5 Costco chicken?"


> *Could have been:* showcase or discussion

> *I chose, because:* "discussion" - the main point is asking the group to share their uses. My rule says a "what's your favorite X?" kind of questions as discussion.

**2.**
> *The post:*  "What's my Potato Salad Missing?"

> *Could have been:* showcase or help

> *I chose, because:* "help" - they want a fix for their own dish, not just to show it off. 

**3.**
> *The post:* "What can I do with teriyaki sauce?"

> *Could have been:* help or discussion

> *I chose, because:* "discussion" - the is no single right answer, and it is an open-ended ask for ideas from the group, not a specific problem to solve.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

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
