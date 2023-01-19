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

    answer = principal*(1+ rate/num)**(num*time)
    return round(answer,2)


# P(1 + r/n)<sup>nt</sup>
# PMT × {[(1 + r/n)^(nt) - 1] / (r/n)}
def post_investment_monthly_contributions(principal, rate, num, time, monthly):
    step_1 = amount_post_investment(principal, rate, num, time)
    step_2 = monthly * (((1+rate/num)**(num*time)-1)/(rate/num))
    answer = step_1 + step_2
    return answer

    # Small mistake here ^^ Time for bed