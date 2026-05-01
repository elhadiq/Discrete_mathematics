"""
Lesson 2 — Propositional Logic
Practical Exercises (SymPy)

Topics: propositions, NOT / AND / OR, Implies, Equivalent,
        truth tables, precedence, converse / contrapositive / inverse,
        tautology, contradiction, logic gates.

Notes by Pr. Zouhair el Hadiq
"""

from sympy import symbols, And, Or, Not, Implies, Equivalent, Xor
from sympy import simplify_logic
from sympy.logic.boolalg import truth_table
from sympy.logic.inference import satisfiable


p, q, r, s = symbols('p q r s')


# ══════════════════════════════════════════════════════════════════════
# Exercise 1 — Basic propositions
# A proposition is a statement with a definite truth value.
# Assign truth values and evaluate compound expressions directly.
# ══════════════════════════════════════════════════════════════════════

print("Exercise 1 — Basic propositions")
expr = And(p, Or(q, Not(p)))
for vals in [(True, True), (True, False), (False, True), (False, False)]:
    result = expr.subs({p: vals[0], q: vals[1]})
    print(f"  p={vals[0]}, q={vals[1]} → {result}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 2 — NOT, AND, OR operators
# Build and evaluate the three primitive connectives.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 2 — NOT / AND / OR")
for pv, qv in [(True, True), (True, False), (False, True), (False, False)]:
    subs = {p: pv, q: qv}
    print(f"  p={pv}, q={qv} | NOT p={Not(p).subs(subs)}  "
          f"p AND q={And(p,q).subs(subs)}  p OR q={Or(p,q).subs(subs)}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 3 — Implication (Implies)
# p → q  is False only when p is True and q is False.
# Print the full truth table for p → q.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 3 — Implication truth table")
impl = Implies(p, q)
print("  p   | q   | p → q")
print("  ------------------")
for vals, result in truth_table(impl, [p, q]):
    print(f"  {vals[0]!s:5}| {vals[1]!s:5}| {result}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 4 — Biconditional (Equivalent / ↔)
# p ↔ q  is True exactly when p and q have the same truth value.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 4 — Biconditional (p ↔ q)")
bicond = Equivalent(p, q)
print("  p   | q   | p ↔ q")
print("  ------------------")
for vals, result in truth_table(bicond, [p, q]):
    print(f"  {vals[0]!s:5}| {vals[1]!s:5}| {result}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 5 — Operator precedence
# Precedence (high → low): NOT > AND > OR > Implies > Equivalent.
# Evaluate ¬p ∧ q ∨ r  with and without explicit parentheses.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 5 — Operator precedence")
# SymPy respects Python operator precedence via function calls;
# parentheses in the function-call sense are explicit.
expr_a = Or(And(Not(p), q), r)    # (¬p ∧ q) ∨ r
expr_b = And(Not(p), Or(q, r))    # ¬p ∧ (q ∨ r)  — different!
vals = {p: True, q: False, r: True}
print(f"  (¬p ∧ q) ∨ r  = {expr_a.subs(vals)}")
print(f"  ¬p ∧ (q ∨ r)  = {expr_b.subs(vals)}")
assert expr_a.subs(vals) != expr_b.subs(vals), "Precedence matters!"
print("  Precedence matters ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 6 — Converse, Contrapositive, Inverse
# Given p → q:
#   Converse      : q → p
#   Contrapositive: ¬q → ¬p   (logically equivalent to p → q)
#   Inverse       : ¬p → ¬q
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 6 — Converse / Contrapositive / Inverse")
original       = Implies(p, q)
converse       = Implies(q, p)
contrapositive = Implies(Not(q), Not(p))
inverse        = Implies(Not(p), Not(q))

print(f"  original       simplified: {simplify_logic(original)}")
print(f"  contrapositive simplified: {simplify_logic(contrapositive)}")
# They must simplify to the same thing
assert simplify_logic(original) == simplify_logic(contrapositive)
print("  original ≡ contrapositive ✓")
# Converse and inverse are equivalent to each other (but not original)
assert simplify_logic(converse) == simplify_logic(inverse)
print("  converse ≡ inverse ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 7 — Tautology detection
# A tautology is True for every assignment.
# Check: p ∨ ¬p  and  (p → q) → (¬q → ¬p)
# ══════════════════════════════════════════════════════════════════════

def is_tautology(expr) -> bool:
    """True iff expr cannot be False (its negation is unsatisfiable)."""
    return not satisfiable(Not(expr))

print("\nExercise 7 — Tautology check")
candidates = {
    "p ∨ ¬p":                Or(p, Not(p)),
    "(p→q) → (¬q→¬p)":      Implies(Implies(p,q), Implies(Not(q),Not(p))),
    "p ∧ ¬p":                And(p, Not(p)),
    "(p∨q) → p":             Implies(Or(p,q), p),
}
for name, expr in candidates.items():
    print(f"  {name:30s}: tautology={is_tautology(expr)}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 8 — Contradiction detection
# A contradiction is False for every assignment.
# ══════════════════════════════════════════════════════════════════════

def is_contradiction(expr) -> bool:
    return not satisfiable(expr)

print("\nExercise 8 — Contradiction check")
candidates = {
    "p ∧ ¬p":           And(p, Not(p)),
    "p ∨ ¬p":           Or(p, Not(p)),
    "(p→q) ∧ p ∧ ¬q":  And(Implies(p,q), p, Not(q)),
}
for name, expr in candidates.items():
    print(f"  {name:30s}: contradiction={is_contradiction(expr)}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 9 — XOR (exclusive or)
# p XOR q is True iff exactly one of p, q is True.
# Verify: p XOR q  ≡  (p ∨ q) ∧ ¬(p ∧ q)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 9 — Exclusive OR (XOR)")
xor_direct = Xor(p, q)
xor_expanded = And(Or(p, q), Not(And(p, q)))
# Are they logically equivalent?
assert is_tautology(Equivalent(xor_direct, xor_expanded))
print("  p XOR q  ≡  (p ∨ q) ∧ ¬(p ∧ q)  verified ✓")
print("  Truth table for p XOR q:")
for vals, result in truth_table(xor_direct, [p, q]):
    print(f"    {vals[0]!s:5} XOR {vals[1]!s:5} = {result}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 10 — Logic gates (NAND, NOR)
# NAND: ¬(p ∧ q)   NOR: ¬(p ∨ q)
# NAND and NOR are each functionally complete (any formula can be built
# from NAND alone or NOR alone).
# Demonstrate: NOT p ≡ p NAND p
#              p AND q ≡ (p NAND q) NAND (p NAND q)
# ══════════════════════════════════════════════════════════════════════

def NAND(a, b): return Not(And(a, b))
def NOR(a, b):  return Not(Or(a, b))

print("\nExercise 10 — Logic gates (NAND / NOR)")
not_via_nand  = NAND(p, p)
and_via_nand  = NAND(NAND(p, q), NAND(p, q))
or_via_nor    = NOR(NOR(p, p), NOR(q, q))

assert is_tautology(Equivalent(not_via_nand, Not(p)))
assert is_tautology(Equivalent(and_via_nand, And(p, q)))
assert is_tautology(Equivalent(or_via_nor,   Or(p, q)))
print("  NOT p ≡ p NAND p                       ✓")
print("  p AND q ≡ (p NAND q) NAND (p NAND q)  ✓")
print("  p OR q  ≡ NOR(NOR(p,p), NOR(q,q))     ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 11 — Three-variable truth table with a complex formula
# Evaluate  (p → q) ∧ (q → r) → (p → r)
# This is hypothetical syllogism — it should be a tautology.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 11 — Hypothetical syllogism as tautology (3 variables)")
hyp_syl = Implies(And(Implies(p, q), Implies(q, r)), Implies(p, r))
print(f"  Is tautology: {is_tautology(hyp_syl)}")
print("  Full truth table:")
print("  p     | q     | r     | result")
print("  " + "-" * 35)
for vals, result in truth_table(hyp_syl, [p, q, r]):
    print(f"  {vals[0]!s:5} | {vals[1]!s:5} | {vals[2]!s:5} | {result}")
