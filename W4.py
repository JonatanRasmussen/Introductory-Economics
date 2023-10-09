# pylint: disable=W0621, disable=C3001, disable=C0415

import math
from sympy import symbols, solve, Eq

# Week 4 Exercises
#%% w4ex1 Production Function and Labor Productivity

# Exercise 1a: Calculate average product of labor (APL) when K=81 and L=16 or L=256
def w4ex1a(K, L):
    Q = (K ** (3/4)) * (L ** (1/4))
    APL = Q / L
    return round(APL, 3)

# Exercise 1b: Marginal product of labor (MPL) when K=81 and L=16 or L=81
def w4ex1b(K, L):
    MPL = (1/4) * (K ** (3/4)) * (L ** (-3/4))
    return round(MPL, 3)

# Exercise 1c: Units of labor to maximize profits, when P=200 and w=50
def w4ex1c():
    L = symbols('L')
    equation = Eq(200 * (1/4) * 81 ** (3/4) * L ** (-3/4), 50)
    labor_to_maximize_profit = solve(equation, L)[0]
    return labor_to_maximize_profit

# Adding test cases for the given code as per the Problem Set 4 - Exercise Solutions document

# Exercise 1a
K = 81
L = 16
print(f"w4ex1a: For K = {K} and L = {L}, APL = {w4ex1a(K, L)}")
print(f"w4ex1c: Units of labor to maximize profits: {w4ex1c()}")
print()

#%% w4ex3 Cost Function Analysis

#%% w4ex3 Cost Function Analysis

# Exercise 3a: Fixed cost of producing 10 units of output
def w4ex3a(coeff_0):
    return coeff_0  # FC is constant

# Exercise 3b: Variable cost of producing 10 units of output
def w4ex3b(coeff_1, coeff_2, coeff_3, Q):
    return coeff_1 * Q + coeff_2 * Q ** 2 + coeff_3 * Q ** 3

# Exercise 3c: Total cost of producing 10 units of output
def w4ex3c(coeff_0, coeff_1, coeff_2, coeff_3, Q):
    return coeff_0 + w4ex3b(coeff_1, coeff_2, coeff_3, Q)

# Exercise 3d: Average fixed cost of producing 10 units of output
def w4ex3d(coeff_0, Q):
    return coeff_0 / Q

# Exercise 3e: Average variable cost of producing 10 units of output
def w4ex3e(coeff_1, coeff_2, coeff_3, Q):
    return w4ex3b(coeff_1, coeff_2, coeff_3, Q) / Q

# Exercise 3f: Average total cost of producing 10 units of output
def w4ex3f(coeff_0, coeff_1, coeff_2, coeff_3, Q):
    return w4ex3c(coeff_0, coeff_1, coeff_2, coeff_3, Q) / Q

# Exercise 3g: Marginal cost when Q = 10
def w4ex3g(coeff_1, coeff_2, coeff_3, Q):
    return coeff_1 + 2 * coeff_2 * Q + 3 * coeff_3 * Q ** 2

# Initialize coefficients and Q
coeff_0 = 100
coeff_1 = 20
coeff_2 = 15
coeff_3 = 10
Q = 10

# Exercise 3a
output_3a = w4ex3a(coeff_0)
print(f"w4ex3a: Fixed cost of producing {Q} units of output: {output_3a}")

# Exercise 3b
output_3b = w4ex3b(coeff_1, coeff_2, coeff_3, Q)
print(f"w4ex3b: Variable cost of producing {Q} units of output: {output_3b}")

# Exercise 3c
output_3c = w4ex3c(coeff_0, coeff_1, coeff_2, coeff_3, Q)
print(f"w4ex3c: Total cost of producing {Q} units of output: {output_3c}")

# Exercise 3d
output_3d = w4ex3d(coeff_0, Q)
print(f"w4ex3d: Average fixed cost of producing {Q} units of output: {output_3d}")

# Exercise 3e
output_3e = w4ex3e(coeff_1, coeff_2, coeff_3, Q)
print(f"w4ex3e: Average variable cost of producing {Q} units of output: {output_3e}")

# Exercise 3f
output_3f = w4ex3f(coeff_0, coeff_1, coeff_2, coeff_3, Q)
print(f"w4ex3f: Average total cost of producing {Q} units of output: {output_3f}")

# Exercise 3g
output_3g = w4ex3g(coeff_1, coeff_2, coeff_3, Q)
print(f"w4ex3g: Marginal cost when Q = {Q}: {output_3g}")
print()

#%% w4ex4 Cost Function Analysis for Multi-Product Firm

import sympy as sp

# Exercise 4a: Are there economies of scope?
def w4ex4a(coeff_f, coeff_alpha, coeff_q1_sq, coeff_q2_sq, q1, q2):
    cost_separate = 2 * coeff_f + coeff_q1_sq * q1**2 + coeff_q2_sq * q2**2
    cost_together = coeff_f + coeff_alpha * q1 * q2 + coeff_q1_sq * q1**2 + coeff_q2_sq * q2**2
    return cost_separate - cost_together

# Exercise 4b: Are there cost complementarities?
def w4ex4b(coeff_alpha, coeff_q1_sq, coeff_q2_sq, q1, q2):
    q1_sym, q2_sym = sp.symbols('q1 q2')
    cost_function = coeff_f - coeff_alpha * q1_sym * q2_sym + coeff_q1_sq * q1_sym**2 + coeff_q2_sq * q2_sym**2
    mc1 = sp.diff(cost_function, q1_sym)
    dmc1_dq2 = sp.diff(mc1, q2_sym)
    return dmc1_dq2.subs({q1_sym: q1, q2_sym: q2})

# Exercise 4c: Effect of selling rights for product 2
def w4ex4c(coeff_q1_sq, q1):
    q1_sym = sp.symbols('q1')
    cost_function_q2_zero = coeff_f + coeff_q1_sq * q1_sym**2
    mc1_q2_zero = sp.diff(cost_function_q2_zero, q1_sym)
    return mc1_q2_zero.subs(q1_sym, q1)

# Initialize coefficients and quantities
coeff_f = 90
coeff_alpha = -0.5
coeff_q1_sq = 0.4
coeff_q2_sq = 0.3
q1 = 10
q2 = 10

# Exercise 4a
output_4a = w4ex4a(coeff_f, coeff_alpha, coeff_q1_sq, coeff_q2_sq, q1, q2)
print(f"w4ex4a: Economies of scope exist? {'Yes' if output_4a > 0 else 'No'} (Output: {output_4a})")

# Exercise 4b
output_4b = w4ex4b(coeff_alpha, coeff_q1_sq, coeff_q2_sq, q1, q2)
print(f"w4ex4b: Cost complementarities exist? {'Yes' if output_4b < 0 else 'No'} (Output: {output_4b})")

# Exercise 4c
output_4c = w4ex4c(coeff_q1_sq, q1)
print(f"w4ex4c: Marginal cost of product 1 if product 2 is sold: {output_4c}")
print()

