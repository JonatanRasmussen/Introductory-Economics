# pylint: disable=W0621


#%% w1ex1 Calculate the Present Value of cash flow
def w1ex1_present_value_of_cash_flows(cash_flow, rate, periods):
    """
    Calculate the Present Value of a series of cash flows.

    Parameters:
        cash_flow (float): The amount of cash flow for each period.
        rate (float): The discount rate (or opportunity cost) as a decimal. E.g., for 5%, it would be 0.05.
        periods (int): The number of periods over which the cash flows occur.

    Returns:
        float: The Present Value of the series of cash flows.
    """
    pv = 0  # Initialize Present Value to 0

    for n in range(1, periods + 1):
        pv += cash_flow / ((1 + rate) ** n)

    return round(pv, 1)

# w1ex1
cash_flow = 200000  # $200,000 at the end of each year
rate = 0.05  # 5% opportunity cost
periods = 4  # 4 years
pv = w1ex1_present_value_of_cash_flows(cash_flow, rate, periods)
print(f"w1ex1: The Present Value of the series of cash flows is: ${pv}")
print()

#%% w1ex2 Calculate the Present Value of a firm before / after paying out dividends
def w1ex2a_present_value_of_firm_pre_dividend_payout(current_profits, discount_rate, growth_rate):
    """
    Calculate the Present Value of a firm with profits expected to grow indefinitely at a constant rate.

    Parameters:
        current_profits (float): The firm's current profits.
        discount_rate (float): The opportunity cost or discount rate as a decimal. E.g., for 7%, it would be 0.07.
        growth_rate (float): The constant growth rate of profits as a decimal. E.g., for 5%, it would be 0.05.

    Returns:
        float: The Present Value of the firm.
    """
    # Ensure that growth rate is less than the discount rate
    if growth_rate >= discount_rate:
        return "Growth rate should be less than the discount rate."

    pv_firm = (current_profits * (1 + discount_rate)) / (discount_rate - growth_rate)
    return round(pv_firm, 1)

def w1ex2b_present_value_of_firm_post_dividend_payout(current_profits, discount_rate, growth_rate):
    """
    Calculate the Present Value of a firm with profits expected to grow indefinitely at a constant rate,
    immediately after current profits have been paid out as dividends.

    Parameters:
        current_profits (float): The firm's current profits.
        discount_rate (float): The opportunity cost or discount rate as a decimal. E.g., for 7%, it would be 0.07.
        growth_rate (float): The constant growth rate of profits as a decimal. E.g., for 5%, it would be 0.05.

    Returns:
        float: The Present Value of the firm immediately after paying out dividends.
    """
    # Ensure that growth rate is less than the discount rate
    if growth_rate >= discount_rate:
        return "Growth rate should be less than the discount rate."

    pv_firm_ex_dividend = (current_profits * (1 + growth_rate)) / (discount_rate - growth_rate)
    return round(pv_firm_ex_dividend, 1)

# w1ex2
current_profits = 200000  # $200,000 current profits
discount_rate = 0.07  # 7% opportunity cost
growth_rate = 0.05  # 5% constant growth rate
pv_firm_pre = w1ex2a_present_value_of_firm_pre_dividend_payout(current_profits, discount_rate, growth_rate)
print(f"w1ex2a: The Present Value of the firm before paying out dividends is: ${pv_firm_pre}")
pv_firm_post = w1ex2b_present_value_of_firm_post_dividend_payout(current_profits, discount_rate, growth_rate)
print(f"w1ex2b: The Present Value of the firm after paying out dividends is: ${pv_firm_post}")
print()

#%% w1ex3 Calculate the Present Value of a Perpetuity (stock that pays a perpetual dividend)
def w1ex3_present_value_of_perpetuity(dividend, interest_rate):
    """
    Calculate the Present Value of a preferred stock that pays a perpetual dividend.

    Parameters:
        dividend (float): The amount of perpetual dividend paid at the end of each year.
        interest_rate (float): The interest rate as a decimal. E.g., for 8%, it would be 0.08.

    Returns:
        float: The Present Value of the preferred stock.
    """
    pv_perpetuity = dividend / interest_rate
    return round(pv_perpetuity, 1)

# w1ex3
dividend = 150  # $150 at the end of each year
interest_rate = 0.08  # 8% interest rate
pv_perpetuity = w1ex3_present_value_of_perpetuity(dividend, interest_rate)
print(f"w1ex3: The Present Value of the preferred stock that pays a perpetual dividend is: ${pv_perpetuity}")
print()

#%% w1ex4 Calculate for Q: Net benefit, Marginal benefit, Max benefit, Total cost, Marginal cost, Max net benefit
# w1ex4X Function to calculate the Marginal Net Benefit when Q is given
def w1ex4x_marginal_net_benefit(Q, Ba, Bb, Bc, Ca, Cb, Cc):
    MB_Q = 2 * Ba * Q + Bb + Bc*0 # Marginal Net Benefit
    MC_Q = 2 * Ca * Q + Cb + Cc*0 # Marginal Net Benefit
    MNB_Q = MB_Q - MC_Q  # Net Benefit
    return MNB_Q

# w1ex4a Function to calculate the Net Benefit when Q is given
def w1ex4a_net_benefit(Q, Ba, Bb, Bc, Ca, Cb, Cc):
    B_Q = Ba * Q*Q + Bb * Q + Bc # Total Benefit
    C_Q = Ca * Q*Q + Cb * Q + Cc # Total Cost
    NB_Q = B_Q - C_Q  # Net Benefit
    return NB_Q

# w1ex4b Function to calculate the Marginal Benefit when Q is given
def w1ex4b_marginal_benefit(Q, Ba, Bb, Bc):
    MB_Q = 2 * Ba * Q + Bb + Bc*0  # Calculating the Marginal Benefit by taking the derivative of B(Q)
    return MB_Q

# w1ex4c Function to maximize the Total Benefit when Q is given
from scipy.optimize import minimize_scalar # type: ignore
def w1ex4c_maximize_total_benefit(Ba, Bb, Bc):
    # Define the function for Total Benefit, but negate it since we're using minimize_scalar
    def neg_total_benefit(Q):
        return -(Ba * Q**2 + Bb * Q + Bc)  # Total Benefit function negated
    # Optimize
    result = minimize_scalar(neg_total_benefit)
    Q_star = result.x  # The level of Q that maximizes Total Benefit
    return round(Q_star, 1)

# w1ex4d Function to calculate the Total Cost when Q is given
def w1ex4d_total_cost(Q, Ca, Cb, Cc):
    return Ca * Q**2 + Cb * Q + Cc  # Total Cost function

# w1ex4e: Function to calculate the Marginal Cost when Q is given
def w1ex4e_marginal_cost(Q, Ca, Cb, Cc):
    MC_Q = 2 * Ca * Q + Cb + Cc * 0  # Calculating the Marginal Cost by taking the derivative of C(Q)
    return MC_Q

# w1ex4f: Function to maximize the Total Cost when Q is given
def w1ex4f_maximize_total_cost(Ca):
    # Total costs are maximized when marginal costs are equal to zero:
    if 2 * Ca == 0:
        return "Total costs are unbounded."
    else:
        return 0  # In this specific function, marginal cost is never zero unless Ca = 0.

# w1ex4g: Function to maximize Net Benefits when Q is given
def w1ex4g_maximize_net_benefit(Ba, Bb, Bc, Ca, Cb, Cc):
    # Define the function for Net Benefit, but negate it since we're using minimize_scalar
    def neg_net_benefit(Q):
        return -((Ba * Q**2 + Bb * Q + Bc) - (Ca * Q**2 + Cb * Q + Cc))  # Net Benefit function negated
    # Optimize
    result = minimize_scalar(neg_net_benefit)
    Q_star_net_benefit = result.x  # The level of Q that maximizes Net Benefit
    return round(Q_star_net_benefit, 1)

# w1ex4
Ba = -1 # Second degree term in BenefitQ function
Bb = 10 # First degree term in BenefitQ function
Bc = 0 # Constant term in BenefitQ function
Ca = 1 # Second degree term in CostQ function
Cb = 0 # First degree term in CostQ function
Cc = 2 # Constant term in CostQ function
Q_values = [2, 5]  # Given Q values

marginal_net_benefits = [w1ex4x_marginal_net_benefit(Q, Ba, Bb, Bc, Ca, Cb, Cc) for Q in Q_values]
print(f"w1ex4x: The Marginal Net Benefits for {Q_values} are: {marginal_net_benefits}.")
net_benefits = [w1ex4a_net_benefit(Q, Ba, Bb, Bc, Ca, Cb, Cc) for Q in Q_values]
print(f"w1ex4a: The Net Benefits for {Q_values} are: {net_benefits}.")
marginal_benefits = [w1ex4b_marginal_benefit(Q, Ba, Bb, Bc) for Q in Q_values]
print(f"w1ex4b: The Marginal Benefits for {Q_values} are: {marginal_benefits}.")
Q_star = w1ex4c_maximize_total_benefit(Ba, Bb, Bc)
print(f"w1ex4c: Total benefit is maximized when Q_star has value {Q_star}.")
total_costs = [w1ex4d_total_cost(Q, Ca, Cb, Cc) for Q in Q_values]
print(f"w1ex4d: The Total cost for {Q_values} are: {total_costs}.")
marginal_costs = [w1ex4e_marginal_cost(Q, Ca, Cb, Cc) for Q in Q_values]
print(f"w1ex4e: The Marginal Costs for {Q_values} are: {marginal_costs}.")
Q_star_maximized_cost = w1ex4f_maximize_total_cost(Ca)
print(f"w1ex4f: Total cost is maximized when Q_star has value {Q_star_maximized_cost}.")
Q_star_max_net_benefit = w1ex4g_maximize_net_benefit(Ba, Bb, Bc, Ca, Cb, Cc)
print(f"w1ex4g: Net benefit is maximized when Q_star has value {Q_star_max_net_benefit}.")
print()

