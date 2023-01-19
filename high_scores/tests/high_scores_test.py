import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    scores = [34, 86, 23, 12, 93, 37, 83]
    
    
    def test_latest_score(self):
        self.assertEqual(83, latest(self.scores))

    def test_personal_best(self):
        self.assertEqual(93, personal_best(self.scores))

    def test_test_top_three(self):
        self.assertEqual((93, 86, 83), personal_top_three(self.scores))

    def test_order_high_to_low(self):
        self.assertEqual([93, 86, 83, 37, 34, 23, 12], reverse_scores_list(self.scores))

    def test_top_three_when_tie(self):
        scores = [10, 10, 9, 8, 8, 7, 4, 2]
        self.assertEqual([10, 9, 8] ,top_three_with_a_tie(scores))


    def test_top_three_when_there_are_less_than_three_or_even_if_there_is_only_one_number(self):
        scores = (3, 5)
        self.assertEqual([5, 3], top_3_2_numbers(scores))

    
