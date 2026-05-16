"""
Lesson 1 — Introduction to Discrete Mathematics
Practical Exercises (pure Python)

Topics: integers, divisibility, primes, modular arithmetic,
        counting, sequences, basic combinatorics.

Notes by Pr. Zouhair el Hadiq
"""

from math import gcd, isqrt
from itertools import combinations, product


# ══════════════════════════════════════════════════════════════════════
# Exercise 1 — Even vs Odd
# Discrete mathematics works on integers, not continuous values.
# Write a function that classifies any integer as even or odd.
# ══════════════════════════════════════════════════════════════════════

def classify(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"

assert classify(0)  == "even"
assert classify(7)  == "odd"
assert classify(-4) == "even"

print("Exercise 1 — Even / Odd")
print([classify(n) for n in range(-3, 6)])
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']


# ══════════════════════════════════════════════════════════════════════
# Exercise 2 — Primality test
# A prime is divisible only by 1 and itself — a purely discrete concept.
# Implement an efficient primality test using trial division up to √n.
# ══════════════════════════════════════════════════════════════════════

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % k != 0 for k in range(3, isqrt(n) + 1, 2))

primes_under_30 = [n for n in range(2, 30) if is_prime(n)]
print("\nExercise 2 — Primes < 30")
print(primes_under_30)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# ══════════════════════════════════════════════════════════════════════
# Exercise 3 — Modular arithmetic
# Clocks, checksums and cryptography all use mod.
# Compute a + b, a - b, a * b modulo m and verify the distributive law:
#   (a + b) mod m == ((a mod m) + (b mod m)) mod m
# ══════════════════════════════════════════════════════════════════════

def mod_ops(a: int, b: int, m: int) -> dict:
    return {
        "add": (a + b) % m,
        "sub": (a - b) % m,
        "mul": (a * b) % m,
    }

a, b, m = 17, 9, 5
ops = mod_ops(a, b, m)
print("\nExercise 3 — Modular arithmetic (a=17, b=9, m=5)")
print(ops)
# Verify distributive law for addition
assert ops["add"] == ((a % m) + (b % m)) % m
print("Distributive law verified ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 4 — Greatest Common Divisor & Least Common Multiple
# GCD is the building block of integer arithmetic.
# Implement LCM from GCD and verify: gcd(a,b) * lcm(a,b) = a * b
# ══════════════════════════════════════════════════════════════════════

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

pairs = [(12, 8), (100, 75), (17, 13)]
print("\nExercise 4 — GCD / LCM")
for a, b in pairs:
    g, l = gcd(a, b), lcm(a, b)
    print(f"  gcd({a},{b})={g}  lcm({a},{b})={l}  product={g*l}=={a*b}: {g*l == a*b}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 5 — Fibonacci sequence
# A classic discrete recurrence: F(n) = F(n-1) + F(n-2).
# Generate the first n Fibonacci numbers iteratively (no recursion).
# ══════════════════════════════════════════════════════════════════════

def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print("\nExercise 5 — Fibonacci (first 12 terms)")
print(fibonacci(12))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# ══════════════════════════════════════════════════════════════════════
# Exercise 6 — Counting divisors
# For a given integer n, list all its positive divisors and count them.
# Observe that perfect squares have an odd number of divisors.
# ══════════════════════════════════════════════════════════════════════

def divisors(n: int) -> list[int]:
    return sorted(k for k in range(1, n + 1) if n % k == 0)

print("\nExercise 6 — Divisors")
for n in [12, 16, 17, 36]:
    d = divisors(n)
    print(f"  divisors({n}) = {d}  count={len(d)}  perfect_square={isqrt(n)**2==n}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 7 — Combinations (Binomial coefficient)
# C(n, k) counts the number of size-k subsets of an n-element set.
# Implement it and verify Pascal's identity: C(n,k) = C(n-1,k-1) + C(n-1,k)
# ══════════════════════════════════════════════════════════════════════

def C(n: int, k: int) -> int:
    """Binomial coefficient n-choose-k."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

print("\nExercise 7 — Binomial coefficient C(n,k)")
print(f"C(5,2) = {C(5,2)}")   # 10
print(f"C(6,3) = {C(6,3)}")   # 20
# Verify Pascal's identity
for n in range(2, 7):
    for k in range(1, n):
        assert C(n, k) == C(n-1, k-1) + C(n-1, k), f"Pascal fails at n={n},k={k}"
print("Pascal's identity verified for all C(n,k), 2 ≤ n ≤ 6 ✓")


# ══════════════════════════════════════════════════════════════════════
# Exercise 8 — Listing subsets (power set)
# The power set of S is the set of all subsets of S.
# For |S|=n, the power set has 2^n elements.
# ══════════════════════════════════════════════════════════════════════

def power_set(s: list) -> list:
    result = []
    for k in range(len(s) + 1):
        result.extend(combinations(s, k))
    return [set(sub) for sub in result]

S = [1, 2, 3]
ps = power_set(S)
print("\nExercise 8 — Power set of {1,2,3}")
print(ps)
print(f"Size = {len(ps)} = 2^{len(S)}")
# 8 subsets: {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}


# ══════════════════════════════════════════════════════════════════════
# Exercise 9 — Sieve of Eratosthenes
# Efficiently find all primes up to N using a boolean sieve.
# Count how many primes exist below 1000.
# ══════════════════════════════════════════════════════════════════════

def sieve(N: int) -> list[int]:
    is_p = [True] * (N + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(N) + 1):
        if is_p[i]:
            for j in range(i * i, N + 1, i):
                is_p[j] = False
    return [i for i, p in enumerate(is_p) if p]

primes_1000 = sieve(1000)
print("\nExercise 9 — Sieve of Eratosthenes")
print(f"Primes ≤ 1000: {len(primes_1000)}")   # 168
print(f"Largest prime ≤ 1000: {primes_1000[-1]}")   # 997


# ══════════════════════════════════════════════════════════════════════
# Exercise 10 — Discrete sequences & their properties
# Arithmetic and geometric sequences are fundamental discrete structures.
# Generate both, then check the sum formula for arithmetic sequences:
#   sum = n/2 * (first + last)
# ══════════════════════════════════════════════════════════════════════

def arithmetic(start: int, step: int, n: int) -> list[int]:
    return [start + i * step for i in range(n)]

def geometric(start: int, ratio: int, n: int) -> list[int]:
    return [start * ratio**i for i in range(n)]

arith = arithmetic(3, 4, 8)   # 3, 7, 11, 15, 19, 23, 27, 31
geom  = geometric(2, 3, 6)    # 2, 6, 18, 54, 162, 486

print("\nExercise 10 — Discrete sequences")
print(f"Arithmetic (start=3, step=4, n=8): {arith}")
predicted_sum = len(arith) * (arith[0] + arith[-1]) // 2
print(f"Sum formula: {predicted_sum}  actual: {sum(arith)}  match: {predicted_sum == sum(arith)}")
print(f"Geometric  (start=2, ratio=3, n=6): {geom}")


# ══════════════════════════════════════════════════════════════════════
# Exercise 11 — Truth table without SymPy (brute force)
# Enumerate all combinations of n boolean variables and evaluate
# a compound expression.  Shows the discrete nature of logic.
# ══════════════════════════════════════════════════════════════════════

def brute_truth_table(expr_fn, var_names: list[str]) -> None:
    """Print a truth table for a boolean function of n variables."""
    header = " | ".join(var_names) + " || result"
    print(header)
    print("-" * len(header))
    for vals in product([False, True], repeat=len(var_names)):
        result = expr_fn(*vals)
        row = " | ".join(str(v)[0] for v in vals) + f"  || {result}"
        print(row)

print("\nExercise 11 — Brute-force truth table: (p → q) ↔ (¬p ∨ q)")
brute_truth_table(
    lambda p, q: (not p or q) == (not p or q),   # always True (tautology)
    ["p", "q"]
)
print("\n  (p AND q) OR (NOT p AND NOT q)  — same as p ↔ q")
brute_truth_table(
    lambda p, q: (p and q) or (not p and not q),
    ["p", "q"]
)
