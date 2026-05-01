"""
Lesson 3 — Equivalence of Propositions
Practical Exercises (SymPy)

Topics: logical equivalence, simplification, CNF, DNF, De Morgan's laws,
        double negation, absorption, distributivity, satisfiability,
        counting functions (at-least-k-of-n).

Notes by Pr. Zouhair el Hadiq
"""

from sympy import symbols, And, Or, Not, Implies, Equivalent, Xor
from sympy import simplify_logic, to_cnf, to_dnf
from sympy.logic.boolalg import truth_table
from sympy.logic.inference import satisfiable
from itertools import combinations


p, q, r, s, a, b, c, d, e = symbols('p q r s a b c d e')


# ══════════════════════════════════════════════════════════════════════
# Exercise 1 — Logical equivalence via truth tables
# Two formulas are equivalent iff they agree on every assignment.
# Verify: ¬(p ∧ q)  ≡  ¬p ∨ ¬q  (De Morgan 1)
# ══════════════════════════════════════════════════════════════════════

def are_equivalent(expr1, expr2, variables) -> bool:
    for vals, r1 in truth_table(expr1, variables):
        r2 = expr2.subs(dict(zip(variables, vals)))
        if bool(r1) != bool(r2):
            return False
    return True

print("Exercise 1 — De Morgan's first law")
lhs = Not(And(p, q))
rhs = Or(Not(p), Not(q))
print(f"  ¬(p∧q) ≡ ¬p∨¬q : {are_equivalent(lhs, rhs, [p, q])}")
assert are_equivalent(lhs, rhs, [p, q])


# ══════════════════════════════════════════════════════════════════════
# Exercise 2 — De Morgan's second law
# ¬(p ∨ q)  ≡  ¬p ∧ ¬q
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 2 — De Morgan's second law")
lhs = Not(Or(p, q))
rhs = And(Not(p), Not(q))
print(f"  ¬(p∨q) ≡ ¬p∧¬q : {are_equivalent(lhs, rhs, [p, q])}")
assert are_equivalent(lhs, rhs, [p, q])


# ══════════════════════════════════════════════════════════════════════
# Exercise 3 — Double negation
# ¬¬p ≡ p
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 3 — Double negation  ¬¬p ≡ p")
expr = Not(Not(p))
simplified = simplify_logic(expr)
print(f"  simplify_logic(¬¬p) = {simplified}")
assert simplified == p


# ══════════════════════════════════════════════════════════════════════
# Exercise 4 — Absorption laws
# p ∨ (p ∧ q) ≡ p        (OR absorption)
# p ∧ (p ∨ q) ≡ p        (AND absorption)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 4 — Absorption laws")
or_abs  = simplify_logic(Or(p, And(p, q)))
and_abs = simplify_logic(And(p, Or(p, q)))
print(f"  p ∨ (p ∧ q) simplifies to: {or_abs}")
print(f"  p ∧ (p ∨ q) simplifies to: {and_abs}")
assert or_abs  == p
assert and_abs == p
print("  Both absorption laws verified ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 5 — Distributive laws
# p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
# p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 5 — Distributive laws")
dist1_lhs = And(p, Or(q, r))
dist1_rhs = Or(And(p, q), And(p, r))
dist2_lhs = Or(p, And(q, r))
dist2_rhs = And(Or(p, q), Or(p, r))
assert are_equivalent(dist1_lhs, dist1_rhs, [p, q, r])
assert are_equivalent(dist2_lhs, dist2_rhs, [p, q, r])
print("  p ∧ (q ∨ r) ≡ (p∧q) ∨ (p∧r)  ✓")
print("  p ∨ (q ∧ r) ≡ (p∨q) ∧ (p∨r)  ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 6 — Simplifying with simplify_logic
# Reduce a complex expression to its minimal form.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 6 — simplify_logic")
complex_expr = Or(And(p, q), And(p, Not(q)))   # p∧q  ∨  p∧¬q  →  p
simplified = simplify_logic(complex_expr)
print(f"  (p∧q) ∨ (p∧¬q) → {simplified}")
assert simplified == p

complex_expr2 = And(Or(p, q), Or(p, Not(q)))   # p∨q ∧ p∨¬q  →  p
simplified2 = simplify_logic(complex_expr2)
print(f"  (p∨q) ∧ (p∨¬q) → {simplified2}")
assert simplified2 == p


# ══════════════════════════════════════════════════════════════════════
# Exercise 7 — Conjunctive Normal Form (CNF)
# Every propositional formula can be converted to a conjunction of
# disjunctions (clauses).  CNF is the standard input for SAT solvers.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 7 — Conjunctive Normal Form (CNF)")
formulas = [
    Implies(p, q),
    Equivalent(p, q),
    And(Or(p, q), Implies(p, r)),
]
for f in formulas:
    cnf = to_cnf(f)
    print(f"  {f}  →  CNF: {cnf}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 8 — Disjunctive Normal Form (DNF)
# Every formula can also be converted to a disjunction of conjunctions.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 8 — Disjunctive Normal Form (DNF)")
formulas = [
    And(Or(p, q), Not(r)),
    Equivalent(p, And(q, r)),
]
for f in formulas:
    dnf = to_dnf(f)
    print(f"  {f}  →  DNF: {dnf}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 9 — Satisfiability
# A formula is satisfiable if at least one assignment makes it True.
# satisfiable() returns a model (dict) or False.
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 9 — Satisfiability")
formulas = {
    "p ∧ q":           And(p, q),
    "p ∧ ¬p":          And(p, Not(p)),
    "(p→q) ∧ p ∧ ¬q": And(Implies(p, q), p, Not(q)),
    "p ∨ ¬p":          Or(p, Not(p)),
}
for name, f in formulas.items():
    model = satisfiable(f)
    print(f"  {name:25s} : {'SAT ' + str(model) if model else 'UNSAT'}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 10 — Counting function (at-least-k-of-n)
# "At least k of the n variables are True."
# Implement using combinations: at least 2 of {a,b,c,d,e} true iff
# some pair is simultaneously True.
# ══════════════════════════════════════════════════════════════════════

def at_least_k_of(variables: list, k: int):
    """Returns a SymPy formula that is True iff at least k vars are True."""
    return Or(*[And(*combo) for combo in combinations(variables, k)])

print("\nExercise 10 — Counting function (at-least-k-of-n)")
vars5 = [a, b, c, d, e]
f2 = at_least_k_of(vars5, 2)
print(f"  at_least_2_of_5 simplified: {simplify_logic(f2)}")

# Verify: with a=T,b=T,c=F,d=F,e=F the result should be True
model_check = f2.subs({a: True, b: True, c: False, d: False, e: False})
print(f"  a=T,b=T,c=F,d=F,e=F  →  {model_check}")
assert model_check == True

model_check2 = f2.subs({a: True, b: False, c: False, d: False, e: False})
print(f"  a=T,b=F,c=F,d=F,e=F  →  {model_check2}")
assert model_check2 == False


# ══════════════════════════════════════════════════════════════════════
# Exercise 11 — Implication equivalences
# Useful rewriting rules for implications:
#   p → q  ≡  ¬p ∨ q
#   p → q  ≡  ¬q → ¬p  (contrapositive)
#   ¬(p → q) ≡  p ∧ ¬q
# ══════════════════════════════════════════════════════════════════════

print("\nExercise 11 — Implication equivalences")
rules = [
    ("p→q ≡ ¬p∨q",       Implies(p,q),          Or(Not(p),q)),
    ("p→q ≡ ¬q→¬p",      Implies(p,q),          Implies(Not(q),Not(p))),
    ("¬(p→q) ≡ p∧¬q",    Not(Implies(p,q)),     And(p,Not(q))),
]
for name, lhs, rhs in rules:
    ok = are_equivalent(lhs, rhs, [p, q])
    print(f"  {name:25s}: {ok}")
    assert ok
print("All implication equivalences verified ✓")
