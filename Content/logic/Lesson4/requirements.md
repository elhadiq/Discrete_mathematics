# Lesson 4 — Predicates &amp; Quantifiers · Completion requirements

This file is the **gap analysis** of the current `lesson4_predicates.html`.
For each item below, please copy the **statement, definition or proof** from your
logic textbook (Rosen, Velleman, Mendelson, Cori–Lascar, Lalement, …) and paste it
under the matching heading.  Once filled in, the lesson will be extended.

For every entry, please provide:

- a **rigorous definition / statement** (mathematical, not Python),
- 1–2 **examples** (positive and a counter-example when relevant),
- a **proof** if the item is a theorem,
- the **reference** (book + page) — for the bibliography of the site.

Legend: ✓ already in the lesson · ✗ missing · ◐ present but should be deepened.

---

## 1. Foundational definitions

| # | Item | Status | What I need from you |
|---|------|--------|----------------------|
| 1.1 | **Predicate / propositional function** (formal definition: a map from a domain $D$ to $\{T,F\}$) | ◐ | Formal definition + arity ($n$-ary predicate). |
| 1.2 | **Arity** ($0$-ary, unary $P(x)$, binary $R(x,y)$, $n$-ary) | ✗ | Definition + one example each. |
| 1.3 | **Domain of discourse / universe $U$** | ✗ | Definition and why the truth value of $\forall x\,P(x)$ depends on $U$. |
| 1.4 | **Term** vs **atomic formula** vs **well-formed formula (wff)** | ✗ | Inductive grammar of a first-order language. |
| 1.5 | **Free variable** vs **bound variable**, **scope** of a quantifier | ✗ | Definition + a labelled example like $\exists x\,(P(x) \wedge Q(x,y))$. |
| 1.6 | **Closed formula (sentence)** vs **open formula** | ✗ | One-line definitions. |
| 1.7 | **Substitution** $\varphi[t/x]$ &amp; capture-avoiding substitution / **α-renaming** | ✗ | Definition + an example where naïve substitution captures a variable. |
| 1.8 | **Interpretation / model / structure** $\mathcal{M} = (U, \cdot^{\mathcal{M}})$ | ✗ | Definition; talk about $|\mathcal{M}| \models \varphi$. |

---

## 2. Quantifiers — already covered (just confirm)

| # | Item | Status |
|---|------|--------|
| 2.1 | Universal quantifier $\forall$ | ✓ |
| 2.2 | Existential quantifier $\exists$ | ✓ |
| 2.3 | Uniqueness quantifier $\exists!$ | ✓ |
| 2.4 | Negation: De Morgan for quantifiers | ✓ |
| 2.5 | Distribution of $\forall / \exists$ over $\wedge / \vee$ | ✓ |
| 2.6 | Nested quantifiers (semantics table) | ✓ |

What's **missing** under quantifiers:

| # | Item | Status | What I need from you |
|---|------|--------|----------------------|
| 2.7 | **Formal expansion of uniqueness**: $\exists!\,x\,P(x) \;\Leftrightarrow\; \exists x\bigl(P(x) \wedge \forall y(P(y) \to y = x)\bigr)$ | ✗ | The equivalence + a worked proof showing the two directions. |
| 2.8 | **Bounded quantifiers** $\forall x \in A\,P(x)$ and $\exists x \in A\,P(x)$ | ✗ | The two expansions: $\forall x(x \in A \to P(x))$ and $\exists x(x \in A \wedge P(x))$. Explain *why* the connective differs. |
| 2.9 | **Vacuous truth** — when $U = \varnothing$: $\forall x\,P(x)$ is True, $\exists x\,P(x)$ is False. | ✗ | Statement + one-line proof + standard example ("all unicorns can fly"). |
| 2.10 | **Quantifier order** — when can $\forall, \exists$ be swapped? | ✗ | Statements: $\forall x\,\forall y \equiv \forall y\,\forall x$; $\exists x\,\exists y \equiv \exists y\,\exists x$; $\exists y\,\forall x\,P(x,y) \Rightarrow \forall x\,\exists y\,P(x,y)$ (one direction only). Plus a **counter-example** for the converse, e.g. $P(x,y) := (y = x+1)$ on $\mathbb{Z}$. |
| 2.11 | **Validity, satisfiability, contingency** of a first-order formula | ✗ | Three formal definitions + one example of each. |
| 2.12 | **Logical equivalence** $\varphi \equiv \psi$ (true in every interpretation) | ✗ | Definition + how it differs from "true in one interpretation". |

---

## 3. Equality

| # | Item | Status | What I need from you |
|---|------|--------|----------------------|
| 3.1 | Equality $=$ as a logical primitive | ◐ | Mention that $=$ is a special binary predicate built into the logic. |
| 3.2 | **Axioms of equality**: reflexivity $x = x$, symmetry $x = y \to y = x$, transitivity $(x = y \wedge y = z) \to x = z$ | ✗ | The three axioms with names. |
| 3.3 | **Leibniz / substitutability**: $(x = y) \to (P(x) \leftrightarrow P(y))$ | ✗ | Statement + a small worked example. |

---

## 4. Normal forms &amp; transformation rules

| # | Item | Status | What I need from you |
|---|------|--------|----------------------|
| 4.1 | **Prenex normal form (PNF)** | ✗ | Definition + statement of the theorem: every wff is equivalent to one in PNF; sketch of the algorithm (rename → push $\neg$ in → pull quantifiers out). |
| 4.2 | One full **worked example** of PNF conversion | ✗ | E.g. $(\forall x\,P(x)) \to (\exists y\,Q(y))$ → PNF. |
| 4.3 | **Skolemization** | ✗ | Definition + standard example: $\forall x\,\exists y\,P(x,y) \rightsquigarrow \forall x\,P(x,f(x))$ for a fresh Skolem function $f$. State that Skolemization preserves satisfiability (not equivalence). |
| 4.4 | **Conjunctive / Disjunctive normal forms** in first-order logic | ✗ | Definitions (after prenex, body is in CNF or DNF). |

---

## 5. Rules of inference (preview of Lesson 5 — *only* the quantifier ones)

For each rule, please provide the **schema** and **one short proof / use-case**:

| # | Rule | Status | What I need from you |
|---|------|--------|----------------------|
| 5.1 | **Universal Instantiation (UI)**: $\forall x\,P(x) \vdash P(c)$ | ✗ | Statement + an example. |
| 5.2 | **Universal Generalization (UG)**: $P(c) \vdash \forall x\,P(x)$ where $c$ is **arbitrary** | ✗ | Statement + the *side condition* on $c$ (not used elsewhere as a constant). |
| 5.3 | **Existential Instantiation (EI)**: $\exists x\,P(x) \vdash P(c)$ for a **new** constant $c$ | ✗ | Statement + the side condition. |
| 5.4 | **Existential Generalization (EG)**: $P(c) \vdash \exists x\,P(x)$ | ✗ | Statement + a simple example. |

(These four also belong in Lesson 5; cross-reference them.)

---

## 6. Standard theorems to prove (please supply the textbook proofs)

| # | Statement | What I need |
|---|-----------|-------------|
| 6.1 | $\forall x \in \mathbb{R}\;(x^2 \geq 0)$ | Direct proof. |
| 6.2 | $\forall n \in \mathbb{Z}\;(n \text{ even} \Leftrightarrow n^2 \text{ even})$ | Two-direction proof (one direct, one contrapositive). |
| 6.3 | $\exists x \in \mathbb{R}\;(x^2 = 2)$ | Constructive existence: exhibit $x = \sqrt{2}$ and prove $\sqrt{2} \in \mathbb{R}$. |
| 6.4 | $\neg\,\exists x \in \mathbb{Z}\;(x^2 &lt; 0)$ | Direct proof via the trichotomy of $\mathbb{Z}$ — or as a corollary of 6.1. |
| 6.5 | **ε–δ definition of continuity** as a quantifier sentence: $\forall \varepsilon &gt; 0\;\exists \delta &gt; 0\;\forall x\;(|x - a| &lt; \delta \to |f(x) - f(a)| &lt; \varepsilon)$ | The full statement + one tiny example (e.g. $f(x) = 2x$ is continuous at $a = 1$). |
| 6.6 | **No surjection $\mathbb{N} \to \mathcal{P}(\mathbb{N})$** (Cantor, by diagonalisation) | The full proof — classical quantifier proof by contradiction. |
| 6.7 | **Russell's "paradox"** in the language of predicates: $R = \{x \mid x \notin x\}$ | The two-line argument why $R \in R \Leftrightarrow R \notin R$. Use it to motivate restricted comprehension. |

---

## 7. Worked translation examples (please supply 6–10)

The lesson currently shows only 3 translations. Please supply more, ideally one
for each of these patterns (please include the **natural-language sentence** *and*
the **expected first-order rendering**):

- 7.1 "Every student attended every lecture." ($\forall\forall$)
- 7.2 "Some student attended every lecture." ($\exists\forall$)
- 7.3 "Every student attended some lecture." ($\forall\exists$)
- 7.4 "There is a lecture that every student attended." ($\exists\forall$ — distinguish from 7.2)
- 7.5 "No student missed every lecture." (negation pushed)
- 7.6 "Between any two distinct rationals, there is a rational." ($\forall\forall\exists$ — density of $\mathbb{Q}$)
- 7.7 "$\mathbb{Z}$ has no upper bound." ($\neg\,\exists\,\forall$)
- 7.8 "Every prime greater than 2 is odd." (bounded $\forall$ + implication)

---

## 8. Counter-examples (please supply)

A complete lesson should include **explicit counter-examples** for tempting but
false equivalences:

| # | Tempting equivalence | What I need |
|---|----------------------|-------------|
| 8.1 | $\forall x\,(P(x) \vee Q(x)) \overset{?}{\equiv} \forall x\,P(x) \vee \forall x\,Q(x)$ | Counter-example on $U = \mathbb{Z}$ with $P(x) := (x \geq 0)$, $Q(x) := (x \leq 0)$ or similar. |
| 8.2 | $\exists x\,(P(x) \wedge Q(x)) \overset{?}{\equiv} \exists x\,P(x) \wedge \exists x\,Q(x)$ | Counter-example. |
| 8.3 | $\forall x\,\exists y\,P(x,y) \overset{?}{\equiv} \exists y\,\forall x\,P(x,y)$ | Counter-example (e.g. $P(x,y) := (y = x + 1)$). |

---

## 9. Bibliography (please supply)

Give me, for each item you provide, the **reference**:

- Author, Title, Edition, Year, Publisher.
- Chapter / section / page.

Suggested references your school may use:
- Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, §1.3–1.5.
- D. J. Velleman, *How To Prove It*, ch. 2.
- E. Mendelson, *Introduction to Mathematical Logic*, ch. 2.
- R. Cori &amp; D. Lascar, *Mathematical Logic*, vol. 1.
- R. Lalement, *Logique, réduction, résolution*.

---

## 10. Practical format for the answers

To make insertion into the HTML lesson straightforward, please paste the answers
in a single Markdown block per section, like this:

```
### 1.5 Free vs bound variables
Definition: …
Scope: …
Example: in $\exists x\,(P(x) \wedge Q(x,y))$, the variable $x$ is bound by …; $y$ is free.
Reference: Rosen 8e, §1.4, p. 47.
```

That's all I need — once you've filled in the items above, I'll fold them
into `lesson4_predicates.html` (and add matching exercises in
`exercises_lesson4.html` / `_enonces.html`) keeping the same orange/darkblue
theme and the existing slideshow controls.
