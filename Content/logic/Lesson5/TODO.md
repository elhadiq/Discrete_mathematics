# TODO — `exercises_lesson5.html`

Audit of `exercises_lesson5.html` (391 lines, 13 blocks: 1 reference table + 12 exercises) against the conventions now used in `lesson5_inference.html` (formal WFFs only, natural-deduction fraction layout, no English-language scenario words). **Nothing has been changed yet**; this file is the work-plan.

Conventions to apply everywhere:

1. **Only propositional / predicate variables** ($p, q, r, s, t, u, P(x), H(x), …$) — no scenario words such as *Swim, Gym, Swimsuit, SellRock, Get7000, Have10000, BuyCar, Savings, Socrates, Cheat, Director, Detention, Octave*.
2. **Natural-deduction layout** — every inference rule and proof step shown as $\dfrac{\text{premises}}{\text{conclusion}}$ inside a `.rule-card`.
3. **No literal `$` in prose** — currency or anything that looks like math must use `USD`, words, or be expressed via formal variables.
4. **MathJax delimiters paired** — after the rewrite, run the parity check used on `lesson5_inference.html` (count of `$` outside `<script>` must be even).
5. **CSS reuse** — `.rule-grid`, `.rule-card`, `.rule-name`, `.proof-list`, `.lbl`, `.just`, `.qed` are already defined in `lesson5_inference.html`; copy them into the exercises stylesheet (or extract a shared CSS file).

---

## Critical bugs (must fix first)

### B1 — Ex 9 has literal `$` in prose
Lines ~316–319 contain `\$7000`, `\$3000`, `\$10000` *inside the natural-language `<li>` text*, not inside math mode. MathJax interprets the first `\$` as the start of an inline math block and breaks rendering (same bug as the original slide 7).
**Fix**: replace the whole exercise per item 9 below — no `$` characters in prose at all.

---

## Per-block changes

### Reference table (Ref) — at top
- Currently a 3-column `<table>` (Rule · Premises · Conclusion).
- **Switch to the same `.rule-grid` layout as slide 5** of the lesson:
  - Each rule a `.rule-card` showing $\dfrac{\text{premises}}{\text{conclusion}}$ and the rule name in small caps underneath.
  - Eight cards: Modus Ponens, Modus Tollens, Hypothetical Syllogism, Disjunctive Syllogism, Addition, Simplification, Conjunction, Resolution.

### Helper note (the `valid` function)
- Keep as is — it is generic.

### Ex 1 — Modus Ponens
- The plain-English line **"if it's raining and rain implies wet ground, what can you conclude?"** must be removed.
- Replace the "Premises … Conclusion …" block with the fraction card $\dfrac{p,\; p \to q}{q}$.

### Ex 2 — Modus Tollens
- Keep symbolic; replace the inference-block with the fraction $\dfrac{\neg q,\; p \to q}{\neg p}$.
- The contrapositive hint can stay (no scenario, no `$` in prose).

### Ex 3 — Hypothetical Syllogism
- Replace inference-block with $\dfrac{p \to q,\; q \to r}{p \to r}$.
- Already abstract — no other change.

### Ex 4 — Disjunctive Syllogism
- Remove the rain/snow plain-language example.
- Replace inference-block with $\dfrac{p \vee q,\; \neg p}{q}$.

### Ex 5 — Addition & Simplification
- Replace the inference-block with two fraction cards:
  - $\dfrac{p}{p \vee q}$ — Addition
  - $\dfrac{p \wedge q}{p}$ — Simplification

### Ex 6 — Conjunction & Resolution
- Replace inference-block with two fraction cards:
  - $\dfrac{p,\; q}{p \wedge q}$ — Conjunction
  - $\dfrac{p \vee q,\; \neg p \vee r}{q \vee r}$ — Resolution

### Ex 7 — All eight rules in one sweep
- Abstract; keep the spirit (dict + assertion loop).
- The eight `(premises, conclusion)` tuples should be displayed using fraction cards in the statement (re-using the Ref grid).

### Ex 8 — Multi-Step Inference (currently "Swimming")
- **Remove** the Swim/Gym/Swimsuit scenario.
- Restate exactly as slide 6 of the lesson:
  - Variables $p, q, r$.
  - Hypotheses $H_1: p \vee q$ and $H_2: p \to r$.
  - Goal: derive $r \vee q$ via the Resolution rule (after rewriting $p \to r$ as $\neg p \vee r$).
- The Python check should use `p, q, r = symbols('p q r')`, not `Swim, Gym, Swimsuit`.

### Ex 9 — Multi-Step Inference (currently "NFT and Car")
- **Remove** all currency / NFT vocabulary.
- Restate exactly as slides 7–8 of the lesson:
  - Variables $p, q, r, s, t, u$.
  - Hypotheses: $H_1: p \to q$, $H_2: q \to r$, $H_3: (r \wedge s) \to t$, $H_4: t \to u$, $H_5: s$.
  - Goal: derive $p \to u$.
- Display the full proof as a numbered `.proof-list` with each derived step as a fraction.
- The Python entailment check uses `p, q, r, s, t, u`.

### Ex 10 — Affirming the Consequent (fallacy)
- The symbolic part is already abstract — keep $\dfrac{p \to q,\; q}{p}$ but display it as a `.rule-card` with a "✗ INVALID" label.
- **Remove** the "If it rains, the ground is wet" hint or rephrase as "Find a model where the premises are true but the conclusion is false: $p = \text{F}$, $q = \text{T}$."

### Ex 11 — Quantified Rules
- **Remove** `socrates` / `H` ("human") / `M` ("mortal") naming.
- Use the same abstract setup as slide 9 of the lesson:
  - Unary predicates $H, L$, constant $o$ (or use $P$, $c$).
  - Hypotheses $H_1: \forall x\,(H(x) \to L(x))$ and $H_2: H(o)$.
  - Goal: $L(o)$.
- Proof = Universal Instantiation then Modus Ponens, each as a fraction.

### Ex 12 — Exam & Director — Full Worked Example
- **Remove** the Cheat / Director / Detention / Octave vocabulary.
- Restate exactly as slide 10 of the lesson:
  - Abbreviations $p := \exists x\, C(x)$, $q := \exists x\, D(x)$, $r := \exists x\, E(x)$.
  - Hypotheses $H_1: \neg p \to \neg q$, $H_2: D(o)$, $H_3: \neg p \vee r$.
  - Goal: derive $r$.
- Display the proof as a `.proof-list` with the four inferred steps in fraction form:
  1. $D(o)$ — $H_2$
  2. $\dfrac{D(o)}{\exists x\, D(x)} \equiv q$ — Existential Generalization
  3. $\dfrac{\neg p \to \neg q,\; q}{p}$ — Modus Tollens
  4. $\dfrac{\neg p \vee r,\; p}{r}$ — Disjunctive Syllogism

---

## Bonus / nice-to-have

- Add a final exercise on the **negation of an inference rule** (e.g., the converse of Modus Ponens — Affirming the Consequent is one; the converse of Hypothetical Syllogism is another) to reinforce the distinction valid vs. invalid.
- Add an exercise on **side conditions** for UG and EI (use a Python counter-example showing what goes wrong if the freshness/arbitrariness condition is dropped).
- Add a final **"prove the goal using only inference rules"** challenge where the student must write down the proof tree (not just run SymPy).

---

## Verification checklist after the rewrite

Run this snippet from the Lesson 5 folder:

```bash
python3 - <<'PY'
import re
text = open('exercises_lesson5.html', encoding='utf-8').read()
clean = re.sub(r'<script.*?</script>', '', text, flags=re.S)
n = clean.count('$')
print(f"Dollar signs outside <script>: {n}  (even? {n % 2 == 0})")
bad = [w for w in ('Swim','Gym','Swimsuit','SellRock','Get7000','Have10000',
                   'BuyCar','Savings','Socrates','socrates','Cheat','Director',
                   'Detention','Octave','NFT','Rock','ETH','USD') if w in clean]
print(f"Leftover scenario vocabulary: {bad or 'none ✓'}")
PY
```

Expected after rewrite:
- `$` count outside `<script>` is **even**.
- Leftover scenario vocabulary is **empty**.

---

*Generated for the Lesson 5 rewrite. Do not modify `exercises_lesson5.html` until each item above is addressed.*
