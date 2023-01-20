# class CompoundInterest:
#     def __init__(self, principal, rate_of_interest, years_invested, number_of_times_interest_compounded_per_year):
#         self.principal = principal
#         self.rate_of_interest = rate_of_interest
#         self.years_invested = years_invested
#         self.number_of_times_interest_compounded_per_year = number_of_times_interest_compounded_per_year

# PEMDAS
def amount_post_investment(principal, rate, num, time):
    # a = num * time
    # b = 1 + rate / num
    # c = b ** a 
    # d = principal * c
    # return round(d, 2)

    answer = principal*(1+ rate/num)**(num*time) # drier than above
    return round(answer,2)


# P(1 + r/n)<sup>nt</sup>
# PMT × {[(1 + r/n)^(nt) - 1] / (r/n)}
def post_investment_monthly_contributions(principal, rate, num, time, monthly):
    answer = (amount_post_investment(principal, rate, num, time)) + (monthly * (((1+rate/num)**(num*time)-1)/(rate/num)))

    return round(answer, 2)
# answer works but only with deposits being made at end. 
# Answer has deposits at beginning
