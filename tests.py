import unittest
import bracket


class BracketTestCase(unittest.TestCase):

    def test_correct_matching_bracket(self):
        s = '[ABC[23]][89]'
        i = 0
        matching_bracket = bracket.find_matching_bracket(s, i)
        self.assertEqual(
            matching_bracket,
            8,
            'Asserting index 0 closing on index 8')

    def test_is_not_begin_bracket(self):
        s = ']'
        is_open_bracket = bracket.test_index(s)
        self.assertEqual(
            is_open_bracket,
            False,
            'Asserting that given index is a bracket'
        )

    def test_index_out_of_length(self):
        s = ''
        i = 1
        self.assertEqual(
            bracket.bracket(s, i),
            'Passed index is out of string length',
            'Asserting that index is on range')

    def test_expected_user_outputs(self):
        s = '[ABC[23]][89]'
        i = 4
        self.assertEqual(
            bracket.bracket(s, i),
            'The opening bracket at index: 4, closes at index: 7',
            'Asserting that the correct message is displayed'
        )


if __name__ == '__main__':
    unittest.main()
