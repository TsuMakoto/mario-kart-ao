# -*- coding: utf-8 -*-

from .context import mario_kart_ai

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(mario_kart_ai.hmm())


if __name__ == '__main__':
    unittest.main()
