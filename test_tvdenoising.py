import unittest

import tvdenoising


class TestTVDenoising(unittest.TestCase):
    def test_smoke(self):
        tvdenoising.tv_1d([0, 1, 0], 1)


if __name__ == "__main__":
    unittest.main()
