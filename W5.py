# pylint: disable=W0621, disable=C3001, disable=C0415

#%% Week 5 Exercise 3: Market Concentration Measures

# Exercise 3a: Four-Firm Concentration Ratio
def w5ex3a(market_shares):
    # Sort the market shares in descending order
    sorted_shares = sorted(market_shares, reverse=True)
    # Take the top 4 largest market shares
    top_4_shares = sorted_shares[:4]
    # Calculate the Four-Firm Concentration Ratio
    cr4 = sum(top_4_shares)
    return cr4

# Exercise 3b: Herfindahl-Hirschman Index (HHI)
def w5ex3b(market_shares):
    # Calculate the HHI
    hhi = sum([share ** 2 for share in market_shares]) * 10000
    return hhi

# Initialize market share percentages for the eight firms
market_shares = [0.2, 0.2, 0.16, 0.16, 0.09, 0.08, 0.06, 0.05]

# Exercise 3a
output_3a = w5ex3a(market_shares)
print(f"w5ex3a: Four-Firm Concentration Ratio: {output_3a}")

# Exercise 3b
output_3b = w5ex3b(market_shares)
print(f"w5ex3b: Herfindahl-Hirschman Index (HHI): {output_3b}")
