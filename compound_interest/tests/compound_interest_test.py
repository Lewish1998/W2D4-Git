import unittest

from src.compound_interest import *

class CompoundInterestTest(unittest.TestCase):
    
    def test_a(self):
        total_amount = amount_post_investment(rate=0.10, num=12, time=20, principal=100)
        self.assertEqual(732.81, total_amount)

    def test_b(self):
        total_amount = amount_post_investment(rate=0.06, num=12, time=10, principal=100)
        self.assertEqual(181.94, total_amount)

    def test_c(self):
            total_amount = amount_post_investment(rate=0.05, num=12, time=8, principal=100000)
            self.assertEqual(149058.55, total_amount)

    def test_d(self):
        total_amount = amount_post_investment(rate=0.1, num=12, time=1, principal=0)
        self.assertEqual(0.00, total_amount)
    
    def test_e(self):
        total_amount = amount_post_investment(rate=0.0, num=12, time=10, principal=100)
        self.assertEqual(100.00, total_amount)

    # Extention tests

    def test_ext_a(self):
        total = post_investment_monthly_contributions(principal=100, rate=0.05, time=8, monthly=1000, num=12)
        self.assertEqual(118380.16, total)

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

