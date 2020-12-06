import unittest

from main import CalculateGroupCount


class TestAocDay6(unittest.TestCase):
    def testOneGroupOneAnswer(self):
        answer_list = "a"

        group_answer_count = CalculateGroupCount(answer_list)

        self.assertEqual(group_answer_count, 1)

    def testOneGroupTwoAnswers(self):
        answer_list = "ab"

        group_answer_count = CalculateGroupCount(answer_list)

        self.assertEqual(group_answer_count, 2)

    def testOneGroupTwoPeopleDifferetAnswers(self):
        answer_list = "a\nb"

        group_answer_count = CalculateGroupCount(answer_list)

        self.assertEqual(group_answer_count, 2)

    def testOneGroupTwoPeopleSameAnswers(self):
        answer_list = "a\na"

        group_answer_count = CalculateGroupCount(answer_list)

        self.assertEqual(group_answer_count, 1)

