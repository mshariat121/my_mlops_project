import unittest

from my_module import normalize_data


class TestDataPreprocessing(unittest.TestCase):

    def test_normalize_data(self):

        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        expected_result = [
            [-1.22474487, -1.22474487, -1.22474487],
            [0.0, 0.0, 0.0],
            [1.22474487, 1.22474487, 1.22474487],
        ]

        self.assertEqual(normalize_data(data), expected_result)


if __name__ == "__main__":

    unittest.main()
