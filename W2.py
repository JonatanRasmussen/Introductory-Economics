# pylint: disable=W0621, disable=C3001, disable=C0415


#%% w2ex1 Calculate the quantity supplied / produced of product X (function Qsx)
def w2ex1a_quantity_supplied(PX, PZ, const_coeff, PX_coeff, PZ_coeff):
    QX_S = const_coeff + PX_coeff * PX + PZ_coeff * PZ
    return QX_S if QX_S > 0 else 0  # Return 0 if quantity supplied is negative

# w2ex1c Function to determine the supply function and inverse supply function with variable coefficients
def w2ex1c_supply_and_inverse_supply_function(a, b, c, PZ):
    # Supply Function: QX_S = a + b*PX + c*PZ
    # Inverse Supply Function: PX = (QX_S - a - c*PZ) / b
    supply_function = lambda PX: a + b * PX + c * PZ
    inverse_supply_function = lambda QX_S: (QX_S - a - c * PZ) / b
    return supply_function, inverse_supply_function

# w2ex1
PX = 600
PZ = 60
const_term = -30 # coefficient for supply function Qsx
Px_coeff = 2 # coefficient for supply function Qsx
Pz_coeff = -4 # coefficient for supply function Qsx
QX_S = w2ex1a_quantity_supplied(PX, PZ, const_term, Px_coeff, Pz_coeff)
print(f"w2ex1a: The quantity of product X produced when PX = ${PX} and PZ = ${PZ} is: {QX_S}")
supply_function, inverse_supply_function = w2ex1c_supply_and_inverse_supply_function(const_term, Px_coeff, Pz_coeff, PZ)
print(f"w2ex1c: The supply function is QX_S = {const_term} + {Px_coeff}*PX + {Pz_coeff}*PZ")
print(f"w2ex1c: The inverse supply function is PX = (QX_S - {const_term} - {Pz_coeff}*PZ) / {Px_coeff}")
print()


#%% w2ex2 Calculate substitute / complement / normal / inferior / quantity demand QD / inverse demand
# w2ex2ba
def w2ex2a(good_Z_coeff):
    """
    Determine whether good with coefficient coeff are substitutes or complements for good X.
    """

    good_relation = "complement" if good_Z_coeff < 0 else "substitute"
    return good_relation

# w2ex2b Determine if X is an Inferior or a Normal Good
def w2ex2b(M_coeff):
    """
    Determine whether good X is an inferior or normal good.
    """
    good_type = "normal" if M_coeff > 0 else "inferior"
    return good_type

# w2ex2c Calculate QD for Good X When PX = 5230
def w2ex2c(const_coeff, PX_coeff, PX_value, PY_coeff, PY_value, PZ_coeff, PZ_value, M_coeff, M_value):
    """
    Calculate the quantity demanded (QD) for good X given various prices and income.

    Parameters:
        const_coeff (float): Constant term in the demand function for good X.
        PX_coeff (float): Coefficient for PX in the demand function for good X.
        PX_value (float): Current price of good X.
        PY_coeff (float): Coefficient for PY in the demand function for good X.
        PY_value (float): Current price of good Y.
        PZ_coeff (float): Coefficient for PZ in the demand function for good X.
        PZ_value (float): Current price of good Z.
        M_coeff (float): Coefficient for M (income) in the demand function for good X.
        M_value (float): Current average income.

    Returns:
        float: Quantity demanded for good X.
    """
    QD = const_coeff + PX_coeff * PX_value + PY_coeff * PY_value + PZ_coeff * PZ_value + M_coeff * M_value
    return QD

# w2ex2d Determine the Demand and Inverse Demand Functions
def w2ex2d(const_coeff, PX_coeff, PY_coeff, PY_value, PZ_coeff, PZ_value, M_coeff, M_value):
    """
    Determine the demand and inverse demand functions for good X.

    Parameters:
        const_coeff (float): Constant term in the demand function for good X.
        PX_coeff (float): Coefficient for PX in the demand function for good X.
        PY_coeff (float): Coefficient for PY in the demand function for good X.
        PY_value (float): Current price of good Y.
        PZ_coeff (float): Coefficient for PZ in the demand function for good X.
        PZ_value (float): Current price of good Z.
        M_coeff (float): Coefficient for M (income) in the demand function for good X.
        M_value (float): Current average income.

    Returns:
        tuple: Demand function and inverse demand function for good X.
    """
    constant_term = const_coeff + PX_coeff * 0 + PY_coeff * PY_value + PZ_coeff * PZ_value + M_coeff * M_value
    demand_function = f"QD = {constant_term} + ({PX_coeff}) * PX"
    inverse_demand_function = f"PX = {constant_term / (-PX_coeff)} - QD / ({-PX_coeff})"
    return demand_function, inverse_demand_function

# Given constants
const_coeff = 6000  # Constant coefficient
PX_coeff = -0.5  # PX coefficient
PY_coeff = -1  # PY coefficient
PZ_coeff = 9  # PZ coefficient
M_coeff = 0.1  # M coefficient
PX_value = 5230  # Given price for good X
PY_value = 6500  # Price of good Y
PZ_value = 100  # Price of good Z
M_value = 70000  # Average income

# Calculate QD for Exercises 2a and 2b
QD_value = w2ex2c(const_coeff, PX_coeff, PX_value, PY_coeff, PY_value, PZ_coeff, PZ_value, M_coeff, M_value)

# Run each function and store their outputs
output_2a1 = w2ex2a(PY_coeff)
output_2a2 = w2ex2a(PZ_coeff)
output_2b = w2ex2b(M_coeff)
output_2c = QD_value
output_2d = w2ex2d(const_coeff, PX_coeff, PY_coeff, PY_value, PZ_coeff, PZ_value, M_coeff, M_value)

# Print the results
print(f"w2ex2a1: The Good is a {output_2a1} for good X.")
print(f"w2ex2a2: The Good is a {output_2a2} for good X.")
print(f"w2ex2b: Good X is a {output_2b} good.")
print(f"w2ex2c: The quantity demanded for good X is {output_2c}.")
print(f"w2ex2d: The demand function is '{output_2d[0]}' and the inverse demand function is '{output_2d[1]}'.")
print()


#%% w2ex3: Calculate consumer surplus
def w2ex3a(const_coeff, coeff_PX):
    """
    Calculate the inverse demand function based on the demand curve QX = coeff_QX - coeff_PX * PX.

    Parameters:
        coeff_QX (float): The coefficient for QX in the demand function.
        coeff_PX (float): The coefficient for PX in the demand function.

    Returns:
        str: The inverse demand function as a string.
    """
    inverse_demand_function = f"PX = {(const_coeff / coeff_PX)} - (QX / {coeff_PX})"
    return inverse_demand_function

# w2ex3b: Calculate consumer surplus for PX = $45
def w2ex3b(const_coeff, coeff_PX, PX_value):
    """
    Calculate the consumer surplus when PX = $45.

    Parameters:
        coeff_QX (float): The coefficient for QX in the demand function.
        coeff_PX (float): The coefficient for PX in the demand function.
        PX_value (float): The price of good X.

    Returns:
        float: The consumer surplus.
    """
    QD = const_coeff - coeff_PX * PX_value
    CS = 0.5 * (const_coeff / coeff_PX - PX_value) * QD
    return CS

# w2ex3c: Calculate consumer surplus for PX = $30
def w2ex3c(const_coeff, coeff_PX, PX_value):
    """
    Calculate the consumer surplus when PX = $30.

    Parameters:
        coeff_QX (float): The coefficient for QX in the demand function.
        coeff_PX (float): The coefficient for PX in the demand function.
        PX_value (float): The price of good X.

    Returns:
        float: The consumer surplus.
    """
    return w2ex3b(const_coeff, coeff_PX, PX_value)  # Same formula as in w2ex3b

# w2ex3d: General statement on consumer surplus and price
def w2ex3d():
    """
    Provide a general statement on the relationship between consumer surplus and price.

    Returns:
        str: The statement.
    """
    return "If the law of demand holds, a decrease in price leads to an increase in consumer surplus, and vice versa."

# Given coefficients and PX values
const_coeff = 300
coeff_PX = 2
PX_value_45 = 45
PX_value_30 = 30

# Calculate and print the results
print(f"w2ex3a: The inverse demand function is: {w2ex3a(const_coeff, coeff_PX)}")
print(f"w2ex3b: The consumer surplus when PX = $45 is: ${w2ex3b(const_coeff, coeff_PX, PX_value_45)}")
print(f"w2ex3d: {w2ex3d()}")
print()

#%% w2ex4
def w2ex4a(coeff_QD, coeff_PX_QD, coeff_QS, coeff_PX_QS):
    """
    Determine the equilibrium price and quantity based on the demand and supply equations.
    """
    from sympy import symbols, Eq, solve
    PX, QD, QS = symbols('PX QD QS')
    eq_demand = Eq(QD, coeff_QD + coeff_PX_QD * PX)
    eq_supply = Eq(QS, coeff_QS + coeff_PX_QS * PX)
    equilibrium = solve(Eq(eq_demand.rhs, eq_supply.rhs), PX)[0]
    equilibrium_QD = eq_demand.subs(PX, equilibrium).rhs
    return round(float(equilibrium), 2), round(float(equilibrium_QD), 2)

def w2ex4b(coeff_QD, coeff_PX_QD, coeff_QS, coeff_PX_QS, tax_value):
    """
    Determine the new equilibrium price and quantity after a tax is imposed.
    """
    from sympy import symbols, Eq, solve
    PX, QD, QS = symbols('PX QD QS')
    eq_demand = Eq(QD, coeff_QD + coeff_PX_QD * PX)
    eq_supply_tax = Eq(QS, coeff_QS + coeff_PX_QS * (PX - tax_value))
    equilibrium_tax = solve(Eq(eq_demand.rhs, eq_supply_tax.rhs), PX)[0]
    equilibrium_QD_tax = eq_demand.subs(PX, equilibrium_tax).rhs
    return round(float(equilibrium_tax), 2), round(float(equilibrium_QD_tax), 2)

def w2ex4c(tax_value, equilibrium_QD_tax):
    """
    Calculate the total tax revenue after a tax is imposed.
    """
    return round(float(tax_value * equilibrium_QD_tax), 2)

# Given coefficients and tax value
coeff_QD = 14
coeff_PX_QD = -0.5
coeff_QS = -1
coeff_PX_QS = 0.25
tax_value = 12

# Calculate and print the results
equilibrium, equilibrium_QD = w2ex4a(coeff_QD, coeff_PX_QD, coeff_QS, coeff_PX_QS)
print(f"w2ex4a: The equilibrium price is: ${equilibrium}, The equilibrium quantity is: {equilibrium_QD}")
equilibrium_tax, equilibrium_QD_tax = w2ex4b(coeff_QD, coeff_PX_QD, coeff_QS, coeff_PX_QS, tax_value)
print(f"w2ex4b: The new equilibrium price after tax is: ${equilibrium_tax}, The new equilibrium quantity after tax is: {equilibrium_QD_tax}")
tax_revenue = w2ex4c(tax_value, equilibrium_QD_tax)
print(f"w2ex4c: The total tax revenue is: ${tax_revenue}")
print()

#%% # w2ex5: Find the producer surplus and generalized inverse supply curve
def w2ex5a_inverse_supply_curve(const_coeff, Px_coeff):
    constant_term = const_coeff / Px_coeff  # Calculate the constant term
    coefficient_QX_S = 1 / Px_coeff  # Calculate the coefficient for QX_S
    inverse_supply_function_str = f"PX = {constant_term} + {coefficient_QX_S}*QX_S"  # Construct the string
    return inverse_supply_function_str

def w2ex5b_producer_surplus_corrected(QX_S, const_coeff, Px_coeff):
    # Calculate PX for the given QX_S using the inverse supply function
    PX_min = const_coeff / Px_coeff
    PX = PX_min + (1 / Px_coeff) * QX_S
    # Calculate the producer surplus using the formula
    PS = 0.5 * (PX - PX_min) * QX_S
    return PS

# Given coefficients
const_coeff = -520
Px_coeff = 20
QX_S = 400
output5a = w2ex5a_inverse_supply_curve(const_coeff, Px_coeff)
output5b = w2ex5b_producer_surplus_corrected(QX_S, const_coeff, Px_coeff)
print(f"w2ex5a: The generalized inverse supply curve is: {output5a}")
print(f"w2ex5b: The producer surplus for QX_S = {QX_S} is: {output5b}")
print()