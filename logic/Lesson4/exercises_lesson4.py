"""
Lesson 4 — Predicates and Quantifiers
Practical Exercises (Python lambdas + Z3)

Topics: predicates over finite domains, universal quantifier (∀),
        existential quantifier (∃), negation of quantifiers,
        nested quantifiers, quantifier elimination, region membership.

Notes by Pr. Zouhair el Hadiq
"""

from z3 import (
    Real, Reals, Int, Ints, Bool, BoolSort,
    ForAll, Exists, And, Or, Not, Implies,
    Solver, Goal, Tactic, sat, unsat,
    prove, Function, DeclareSort, Const,
)
import math


# ══════════════════════════════════════════════════════════════════════
# Exercise 1 — Predicate over a finite domain
# Define P(x): "x is even" for x in {1,...,10}.
# Evaluate P at every point and list the witnesses.
# ══════════════════════════════════════════════════════════════════════

print("Exercise 1 — Predicate over finite domain")
domain = list(range(1, 11))
P = lambda x: x % 2 == 0
witnesses = [x for x in domain if P(x)]
print(f"  P(x) = 'x is even', domain = {domain}")
print(f"  P is True for: {witnesses}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 2 — Universal quantifier over a finite domain
# ∀x P(x): manually check that P holds for every element.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 2 — Universal quantifier (finite domain)")
domain = list(range(1, 6))
P_pos = lambda x: x > 0          # ∀x: x > 0 on {1..5} → True
P_even = lambda x: x % 2 == 0    # ∀x: x even on {1..5} → False

print(f"  ∀x>0 on {domain}: {all(P_pos(x) for x in domain)}")
print(f"  ∀x even on {domain}: {all(P_even(x) for x in domain)}")
# Show the counterexample
counterex = next((x for x in domain if not P_even(x)), None)
print(f"  Counterexample for ∀x even: x = {counterex}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 3 — Existential quantifier over a finite domain
# ∃x P(x): True if at least one element satisfies P.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 3 — Existential quantifier (finite domain)")
domain = list(range(-5, 6))
P_neg = lambda x: x < 0
P_gt10 = lambda x: x > 10

print(f"  ∃x<0 in {domain}: {any(P_neg(x) for x in domain)}")
print(f"  ∃x>10 in {domain}: {any(P_gt10(x) for x in domain)}")
witness = next((x for x in domain if P_neg(x)), None)
print(f"  Witness for ∃x<0: x = {witness}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 4 — Z3: universal quantifier over reals
# ∀x∈ℝ: x² ≥ 0   (always true)
# ∀x∈ℝ: x² > 0   (false; x=0 is a counterexample)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 4 — Z3: ∀x: x² ≥ 0  and  ∀x: x² > 0")
x = Real('x')
print("  prove(∀x: x²≥0):", end=" ")
prove(ForAll([x], x**2 >= 0))     # prints 'proved'

s = Solver()
s.add(Not(ForAll([x], x**2 > 0)))  # find counterexample
print("  ∀x: x²>0 is", "valid" if s.check() == unsat else "NOT valid")
if s.check() == sat:
    print(f"  Counterexample: x = {s.model()[x]}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 5 — Z3: existential quantifier over reals
# ∃x∈ℝ: x² = 2   (true — x = √2)
# ∃x∈ℤ: x² = 2   (false — no integer solution)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 5 — Z3: ∃x: x² = 2 (real vs integer)")
xr = Real('xr')
xi = Int('xi')

s_real = Solver()
s_real.add(xr**2 == 2)
print(f"  ∃x∈ℝ: x²=2 → {s_real.check()}")   # sat

s_int = Solver()
s_int.add(xi**2 == 2)
print(f"  ∃x∈ℤ: x²=2 → {s_int.check()}")    # unsat


# ══════════════════════════════════════════════════════════════════════
# Exercise 6 — Negation of quantifiers
# ¬∀x P(x) ≡ ∃x ¬P(x)
# ¬∃x P(x) ≡ ∀x ¬P(x)
# Demonstrate both directions with Z3.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 6 — Negation of quantifiers")
x = Real('x')
# ¬(∀x: x>0)  ≡  ∃x: x≤0
s1 = Solver()
s1.add(x <= 0)       # witness for ∃x: ¬(x>0)
print(f"  ¬(∀x: x>0) has witness x≤0: {s1.check()}, x={s1.model()[x] if s1.check()==sat else 'N/A'}")

# ¬(∃x: x²<0)  ≡  ∀x: x²≥0
s2 = Solver()
s2.add(x**2 < 0)
print(f"  ¬(∃x: x²<0) — no witness exists: {s2.check()}")   # unsat


# ══════════════════════════════════════════════════════════════════════
# Exercise 7 — Quantifier elimination with Z3 Tactic('qe')
# Find the values of parameter a for which ∃(x,y): x²+a·y²≤1 ∧ x-y≥2
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 7 — Quantifier elimination (Tactic 'qe')")
x, y, a = Reals('x y a')
g = Goal()
g.add(Exists([x, y], And(x**2 + a*y**2 <= 1, x - y >= 2)))
qe = Tactic('qe')
result = qe(g)
print("  ∃(x,y): x²+a·y²≤1 ∧ x-y≥2  eliminates to:")
print(f"  {result[0]}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 8 — Nested quantifiers
# ∀x ∃y: x + y = 0  (over ℝ: always true, y = -x)
# ∃x ∀y: x + y = 0  (false: no single x works for all y)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 8 — Nested quantifiers")
x, y = Reals('x y')

# ∀x ∃y: x+y=0  — should be provable
print("  prove(∀x ∃y: x+y=0):", end=" ")
prove(ForAll([x], Exists([y], x + y == 0)))

# ∃x ∀y: x+y=0  — should NOT be provable (find counterexample)
s = Solver()
s.add(Not(Exists([x], ForAll([y], x + y == 0))))
print(f"  ∃x ∀y: x+y=0 is {'valid' if s.check()==unsat else 'NOT valid (order matters!)'}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 9 — Predicates with two variables (binary relation)
# R(x, y): "x divides y" over domain {1..6} × {1..6}.
# Find all pairs where R holds, count them.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 9 — Binary predicate R(x,y): 'x divides y'")
domain = range(1, 7)
R = lambda x, y: y % x == 0
pairs = [(x, y) for x in domain for y in domain if R(x, y)]
print(f"  Pairs (x,y) where x|y: {pairs}")
print(f"  Total: {len(pairs)}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 10 — Z3: predicate over a declared sort
# "Every human is mortal."  H(x) → M(x) for all x.
# Socrates is human.  Conclude Socrates is mortal.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 10 — Z3: Every human is mortal (Socrates)")
Person   = DeclareSort('Person')
socrates = Const('socrates', Person)
x_p      = Const('x', Person)
H = Function('H', Person, BoolSort())
M = Function('M', Person, BoolSort())

s = Solver()
s.add(ForAll([x_p], Implies(H(x_p), M(x_p))))   # ∀x: H(x)→M(x)
s.add(H(socrates))                                # H(socrates)
s.add(Not(M(socrates)))                           # assume ¬M(socrates)
result = s.check()
print(f"  Assuming ¬Mortal(Socrates): {result}")
print(f"  Conclusion: Mortal(Socrates) is {'derivable' if result==unsat else 'not derivable'} ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 11 — Region membership (Z3)
# Region R1: x² + y² ≤ 4        (disk of radius 2)
# Region R2: x² + y² ≤ 1        (disk of radius 1)
# Show R2 ⊆ R1, i.e., ¬∃(x,y): R2 ∧ ¬R1  should be unsat.
# Also find a point in R1 but not R2.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 11 — Region inclusion R2 ⊆ R1 (Z3)")
x, y = Reals('x y')
R1 = x**2 + y**2 <= 4    # big disk
R2 = x**2 + y**2 <= 1    # small disk

# R2 ⊆ R1?
s_incl = Solver()
s_incl.add(And(R2, Not(R1)))    # point in R2 but not R1
print(f"  ∃(x,y) in R2 but not R1: {s_incl.check()}")  # unsat  → R2 ⊆ R1
print("  R2 ⊆ R1 confirmed ✓")

# Point in R1 but not R2
s_diff = Solver()
s_diff.add(And(R1, Not(R2)))
print(f"  ∃(x,y) in R1 but not R2: {s_diff.check()}")  # sat
if s_diff.check() == sat:
    m = s_diff.model()
    print(f"  Example point: x={m[x]}, y={m[y]}")
