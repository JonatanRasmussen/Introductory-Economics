# pylint: disable=W0621, disable=C3001, disable=C0415


# Week 3 Exercises
#%% w3ex1 Demand Curve and Elasticities

# Exercise 1a: Own price elasticity at a given Px
def w3ex1a(Px, const_coeff, Px_coeff, Pz_coeff, Pz):
    Qxd = const_coeff - Px_coeff * Px - Pz_coeff * Pz
    elasticity = (Px_coeff * Px) / Qxd
    return Qxd, round(elasticity, 2)

# Exercise 1b: Own price elasticity at a different Px
def w3ex1b(Px, const_coeff, Px_coeff, Pz_coeff, Pz):
    return w3ex1a(Px, const_coeff, Px_coeff, Pz_coeff, Pz)  # Reusing the function from 1a

# Exercise 1c: Cross-price elasticity
def w3ex1c(Pz, Qxd, Pz_coeff):
    cross_elasticity = (Pz_coeff * Pz) / Qxd
    return round(cross_elasticity, 2)

# Test the functions
const_coeff = 1200  # Constant term in the demand function
Px_coeff = 3  # Coefficient for Px in the demand function
Pz_coeff = 0.1  # Coefficient for Pz in the demand function

Px = 140  # Given Px for 1a
Pz = 300  # Given Pz for 1a and 1b
Qxd = 140
Px_new_value = 240  # Given Px for 1b

Qxd, elasticity = w3ex1a(Px, const_coeff, Px_coeff, Pz_coeff, Pz)
print(f"w3ex1a: Quantity demanded at Px = $140 is {Qxd}, and own price elasticity is {elasticity}")
cross_elasticity = w3ex1c(Pz, Qxd, Pz_coeff)
print(f"w3ex1c: Cross price elasticity at Px = $140 is {cross_elasticity}")
print()

#%% w3ex2 Elasticity of demand
import math

# Exercise 2a: Own price elasticity of demand
def w3ex2a(coeff_ln_Px):
    own_price_elasticity = coeff_ln_Px
    return own_price_elasticity

# Exercise 2b: Cross-price elasticity of demand
def w3ex2b(coeff_ln_Py):
    cross_price_elasticity = coeff_ln_Py
    return cross_price_elasticity

# Exercise 2c: Income elasticity of demand
def w3ex2c(coeff_ln_M):
    income_elasticity = coeff_ln_M
    return income_elasticity

# Exercise 2d: Advertising elasticity of demand
def w3ex2d(coeff_ln_A):
    advertising_elasticity = coeff_ln_A
    return advertising_elasticity

# Given coefficients
coeff_ln_Px = -1.5  # Coefficient for ln(Px)
coeff_ln_Py = 2     # Coefficient for ln(Py)
coeff_ln_M = -0.5   # Coefficient for ln(M)
coeff_ln_A = 1      # Coefficient for ln(A)

# Exercise 2a
own_price_elasticity = w3ex2a(coeff_ln_Px)
print(f"w3ex2a: The own price elasticity of demand is {own_price_elasticity}")

# Exercise 2b
cross_price_elasticity = w3ex2b(coeff_ln_Py)
print(f"w3ex2b: The cross-price elasticity of demand is {cross_price_elasticity}")

# Exercise 2c
income_elasticity = w3ex2c(coeff_ln_M)
print(f"w3ex2c: The income elasticity of demand is {income_elasticity}")

# Exercise 2d
advertising_elasticity = w3ex2d(coeff_ln_A)
print(f"w3ex2d: The advertising elasticity of demand is {advertising_elasticity}")
print()

#%% w3ex3 Function to calculate the change in total revenue

def w3ex3(Rx, Ry, Eqx_Px, Eqy_Py, delta_Px):

    # Calculate the change in total revenue based on the given formula

    delta_TR = (Rx * (1 + Eqx_Px) + Ry * Eqy_Py) * delta_Px

    return delta_TR

Rx = 40000  # Revenue from product X
Ry = 90000  # Revenue from product Y
Eqx_Px = -1.5  # Own price elasticity of demand for product X
Eqy_Py = -1.8  # Cross-price elasticity of demand for product Y with respect to X
delta_Px = 0.02  # 2% increase in the price of product X

# Calculate the change in total revenue
change_in_total_revenue = w3ex3(Rx, Ry, Eqx_Px, Eqy_Py, delta_Px)
print(f"w3ex3: The change in total revenue is {change_in_total_revenue}")
print()

#%% w3ex4 Broken
# Function to solve Exercise 4a: Writing an equation that summarizes the demand for the firm's product.
def w3ex4a(intercept, coef_price, coef_income):
    return f'Qd = {intercept} + ({coef_price} * Px) + ({coef_income} * M)'

# Function to solve Exercise 4b: Checking which coefficients are statistically significant at the 5% level.
def w3ex4b(p_value_intercept, p_value_price, p_value_income):
    significant_at_5_percent = {}
    significant_at_5_percent['Intercept'] = p_value_intercept < 0.05
    significant_at_5_percent['Price'] = p_value_price < 0.05
    significant_at_5_percent['Income'] = p_value_income < 0.05
    return significant_at_5_percent

# Function to solve Exercise 4c: Commenting on how well the regression line fits the data.
def w3ex4c(r_square, adjusted_r_square, f_statistic):
    comments = {
        'R-Square': f"The R-Square is {r_square}, indicating that the model explains {round(r_square * 100, 2)}% of the total variation in demand for X.",
        'Adjusted R-Square': f"The adjusted R-Square is {adjusted_r_square}, which is only marginally lower, suggesting that the R-Square is not the result of an excessive number of estimated coefficients relative to the sample size.",
        'F-Statistic': f"The F-statistic is {f_statistic}, suggesting that the overall regression is statistically significant better than the 5 percent level."
    }
    return comments

# Calculations for Exercise 4a, 4b, and 4c
exercise_4a = w3ex4a(58.87, -1.64, 1.11)
exercise_4b = w3ex4b(0.00, 0.6, 0.00)
exercise_4c = w3ex4c(0.14, 0.13, 'better than the 5 percent level')

print(f"w3ex4a: {exercise_4a}")
print(f"w3ex4b: The coefficients that are statistically significant at the 5% level are {', '.join([k for k, v in exercise_4b.items() if v])}.")
print(f"w3ex4c: {exercise_4c['R-Square']} {exercise_4c['Adjusted R-Square']} {exercise_4c['F-Statistic']}")
print()

#%% w3ex5 Elasticity (read coefficient)
# Define the function for Exercise 5a
def w3ex5a(b_hat):
    # Own price elasticity of demand is simply the coefficient (estimate) of ln Px
    Eqx_Px = b_hat

    # Determine whether demand is elastic, inelastic, or unitary elastic
    demand_type = "elastic" if abs(Eqx_Px) > 1 else "inelastic" if abs(Eqx_Px) < 1 else "unitary elastic"

    return Eqx_Px, demand_type

# Define the function for Exercise 5b
def w3ex5b(c_hat):
    # Income elasticity of demand is simply the coefficient (estimate) of M
    Eqx_M = c_hat

    # Determine whether the good is a normal or inferior good
    good_type = "normal" if Eqx_M > 0 else "inferior"

    return Eqx_M, good_type

# Given values
a_hat = 7.42
b_hat = -2.18
c_hat = 0.34
M = 55000
Px_4 = 4.39

# Compute the own price elasticity of demand and the income elasticity of demand
own_price_elasticity, demand_type = w3ex5a(b_hat)
income_elasticity, good_type = w3ex5b(c_hat)
print(f"w3ex5a: The own price elasticity of demand is {own_price_elasticity}, indicating that the demand is {demand_type}.")
print(f"w3ex5b: The income elasticity of demand is {income_elasticity}, indicating that the good is a {good_type} good.")
print()

#%% w3ex6 Finding the price to maximize revenue
# Importing required libraries
# Define the function to solve Exercise 6: Finding the price to maximize revenue.
def w3ex6():
    from sympy import symbols, solve, Eq
    # Define variables
    P = symbols('P')
    # Define the equation for elasticity
    equation = Eq(-1, -1.5 * (P / (150000 - 1.5 * P)))

    # Solve the equation
    price_to_maximize_revenue = solve(equation, P)
    return price_to_maximize_revenue[0]

# Calculations and print statements
exercise_6 = w3ex6()
print(f"w3ex6: The price to maximize revenue is ${exercise_6}.")
print()
