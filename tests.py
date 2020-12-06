import unittest

from main import solution


class TestAocDay6(unittest.TestCase):
    def testOneGroupOneAnswer(self):
        self.assertEqual(solution("a"), 1)

    def testOneGroupTwoAnswers(self):
        self.assertEqual(solution("ab"), 2)
