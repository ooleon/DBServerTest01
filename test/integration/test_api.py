import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True != False)  # add assertion here

"""
    def test_debtors(self, sample_contracts, renegotiated_ids):
        # print(sample_contracts.count())
        self.assertEqual(True, True != False)  # add assertion here
"""

if __name__ == '__main__':
    unittest.main()
