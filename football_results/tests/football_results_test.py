import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    def test_home_score(self):
        scores = {"home_score": 0, "away_score": 1}
        self.assertEqual('Away win', get_result(scores))

    def test_results(self):
        scores = [
    {"home_score": 0,
    "away_score": 1},
    {"home_score": 1,
    "away_score": 0},
    {"home_score": 0,
    "away_score": 0}
]
        self.assertEqual('Away win', get_results(scores))









    # def test_list_of_results(self):
    #     scores = {
    #         {"home_score": 0, "away_score": 1}, 
    #         {"home_score": 1, "away_score": 0}, 
    #         {"home_score": 1, "away_score": 1}
    #         }
    #     self.assertEqual({'Away win', 'Home win', 'Draw'}, get_results(scores))



    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
