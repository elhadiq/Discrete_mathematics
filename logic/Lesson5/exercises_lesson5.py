"""
Lesson 5 — Rules of Inference
Practical Exercises (SymPy + Z3)

Topics: verifying propositional inference rules (modus ponens, modus
        tollens, hypothetical syllogism, disjunctive syllogism,
        addition, simplification, conjunction, resolution),
        multi-step inference, quantified rules (universal /
        existential instantiation & generalization).

Notes by Pr. Zouhair el Hadiq
"""

from sympy import symbols, And, Or, Not, Implies
from sympy.logic.inference import satisfiable
from z3 import (
    DeclareSort, Function, BoolSort, Const, ForAll, Exists,
    Implies as Imp, And as zAnd, Not as zNot, Or as zOr,
    Solver, sat, unsat,
)


p, q, r, s = symbols('p q r s')


# ══════════════════════════════════════════════════════════════════════
# Helper
# ══════════════════════════════════════════════════════════════════════

def valid(premises_conj, conclusion) -> bool:
    """True iff the argument is valid (premises ⊢ conclusion)."""
    return not satisfiable(And(premises_conj, Not(conclusion)))


# ══════════════════════════════════════════════════════════════════════
# Exercise 1 — Modus Ponens
# Premises: p,  p → q     Conclusion: q
# ══════════════════════════════════════════════════════════════════════

print("Exercise 1 — Modus Ponens")
ok = valid(And(p, Implies(p, q)), q)
print(f"  p, p→q ⊢ q : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 2 — Modus Tollens
# Premises: ¬q,  p → q     Conclusion: ¬p
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 2 — Modus Tollens")
ok = valid(And(Not(q), Implies(p, q)), Not(p))
print(f"  ¬q, p→q ⊢ ¬p : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 3 — Hypothetical Syllogism
# Premises: p→q,  q→r     Conclusion: p→r
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 3 — Hypothetical Syllogism")
ok = valid(And(Implies(p, q), Implies(q, r)), Implies(p, r))
print(f"  p→q, q→r ⊢ p→r : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 4 — Disjunctive Syllogism
# Premises: p ∨ q,  ¬p     Conclusion: q
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 4 — Disjunctive Syllogism")
ok = valid(And(Or(p, q), Not(p)), q)
print(f"  p∨q, ¬p ⊢ q : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 5 — Addition and Simplification
# Addition:     p ⊢ p ∨ q
# Simplification: p ∧ q ⊢ p
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 5 — Addition & Simplification")
ok_add  = valid(p, Or(p, q))
ok_simp = valid(And(p, q), p)
print(f"  p ⊢ p∨q       : {ok_add}")
print(f"  p∧q ⊢ p       : {ok_simp}")
assert ok_add and ok_simp


# ══════════════════════════════════════════════════════════════════════
# Exercise 6 — Conjunction and Resolution
# Conjunction: p, q ⊢ p ∧ q
# Resolution:  p∨q,  ¬p∨r  ⊢  q∨r
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 6 — Conjunction & Resolution")
ok_conj = valid(And(p, q), And(p, q))
ok_res  = valid(And(Or(p, q), Or(Not(p), r)), Or(q, r))
print(f"  p, q ⊢ p∧q                      : {ok_conj}")
print(f"  p∨q, ¬p∨r ⊢ q∨r (Resolution)   : {ok_res}")
assert ok_conj and ok_res


# ══════════════════════════════════════════════════════════════════════
# Exercise 7 — Verify ALL eight rules in one sweep
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 7 — All eight inference rules")
rules = {
    "Modus Ponens":           (And(p, Implies(p,q)),             q),
    "Modus Tollens":          (And(Not(q), Implies(p,q)),        Not(p)),
    "Hypothetical Syllogism": (And(Implies(p,q), Implies(q,r)),  Implies(p,r)),
    "Disjunctive Syllogism":  (And(Or(p,q), Not(p)),             q),
    "Addition":               (p,                                 Or(p,q)),
    "Simplification":         (And(p,q),                          p),
    "Conjunction":            (And(p,q),                          And(p,q)),
    "Resolution":             (And(Or(p,q), Or(Not(p),r)),        Or(q,r)),
}
for name, (prems, conc) in rules.items():
    result = valid(prems, conc)
    print(f"  {name:25s}: {result}")
    assert result, f"Rule failed: {name}"
print("All eight rules verified ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 8 — Multi-step inference (swimming example)
# Premises:  Swim ∨ Gym,   Swim → Swimsuit
# Conclusion: Swimsuit ∨ Gym     (via Resolution)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 8 — Multi-step: Swimming example")
Swim, Gym, Swimsuit = symbols('Swim Gym Swimsuit')
premises = And(Or(Swim, Gym), Implies(Swim, Swimsuit))
conclusion = Or(Swimsuit, Gym)
ok = valid(premises, conclusion)
print(f"  Swim∨Gym, Swim→Swimsuit ⊢ Swimsuit∨Gym : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 9 — Multi-step inference (NFT / car purchase)
# Premises (chained):
#   SellRock → Get7000
#   Get7000 ∧ Savings → Have10000
#   Have10000 → BuyCar
#   SellRock,  Savings
# Conclusion: BuyCar
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 9 — Multi-step: NFT → car")
SellRock, Get7000, Have10000, BuyCar, Savings = symbols(
    'SellRock Get7000 Have10000 BuyCar Savings')
premises = And(
    SellRock,
    Implies(SellRock, Get7000),
    Savings,
    Implies(And(Get7000, Savings), Have10000),
    Implies(Have10000, BuyCar),
)
ok = valid(premises, BuyCar)
print(f"  SellRock, chain of implications ⊢ BuyCar : {ok}")
assert ok


# ══════════════════════════════════════════════════════════════════════
# Exercise 10 — Invalid argument (identify the flaw)
# Affirming the consequent (NOT a valid rule):
#   Premises: p → q,  q     Conclusion: p   ← INVALID
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 10 — Invalid: Affirming the consequent")
ok = valid(And(Implies(p, q), q), p)
print(f"  p→q, q ⊢ p : {ok}  (should be False — this is a fallacy)")
assert not ok
# Show a counterexample
model = satisfiable(And(And(Implies(p, q), q), Not(p)))
print(f"  Counterexample: {model}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 11 — Quantified rules with Z3
# Universal Instantiation:  ∀x H(x)→M(x),  H(socrates)  ⊢ M(socrates)
# Existential Generalization: M(socrates) ⊢ ∃x M(x)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 11 — Quantified inference rules (Z3)")
Person   = DeclareSort('Person')
socrates = Const('socrates', Person)
x        = Const('x', Person)
H = Function('H', Person, BoolSort())
M = Function('M', Person, BoolSort())

# Universal Instantiation: ∀x H(x)→M(x) + H(socrates) ⊢ M(socrates)
s = Solver()
s.add(ForAll([x], Imp(H(x), M(x))))
s.add(H(socrates))
s.add(zNot(M(socrates)))          # assume negation
print(f"  Universal Instantiation — refutation: {s.check()}")
assert s.check() == unsat

# Existential Generalization: M(socrates) ⊢ ∃x M(x)
s2 = Solver()
s2.add(M(socrates))
s2.add(zNot(Exists([x], M(x))))   # assume ¬∃x M(x)
print(f"  Existential Generalization — refutation: {s2.check()}")
assert s2.check() == unsat
print("Both quantified rules verified ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 12 — Exam & director (full worked example)
# Premises:
#   ¬ExCheat → ¬ExDirector
#   ExDirector   (Octave met the director)
#   ¬ExCheat ∨ ExDetention
# Conclusion: ExDetention
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 12 — Exam & Director")
ExCheat, ExDirector, ExDetention = symbols('ExCheat ExDirector ExDetention')
premises = And(
    Implies(Not(ExCheat), Not(ExDirector)),
    ExDirector,
    Or(Not(ExCheat), ExDetention),
)
ok = valid(premises, ExDetention)
print(f"  Premises ⊢ ExDetention : {ok}")
assert ok
print("Someone gets a detention — derived by modus tollens + disj. syllogism ✓")
