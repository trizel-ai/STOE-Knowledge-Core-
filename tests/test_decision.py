import unittest
from decision_logic import analyze_vs_series

class TestDecisionLogic(unittest.TestCase):
    def test_vs_above_threshold(self):
        # Test case: high ∇S values over 90 days
        test_data = [6.6] * 91
        result = analyze_vs_series(test_data)
        self.assertEqual(result["status"], "ALERT")

    def test_vs_below_threshold(self):
        # Test case: stable low ∇S values
        test_data = [5.9] * 91
        result = analyze_vs_series(test_data)
        self.assertEqual(result["status"], "NORMAL")

    def test_vs_edge_case(self):
        # Edge case: critical value just reached
        test_data = [6.5] * 45 + [6.3] * 46
        result = analyze_vs_series(test_data)
        self.assertEqual(result["status"], "NORMAL")

if __name__ == '__main__':
    unittest.main()
