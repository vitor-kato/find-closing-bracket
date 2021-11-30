#!/usr/bin/python3
import csv


def test_index(index):
    """
    Checks if the given index matches a open bracket
    """
    if index is not "[":
        return False

    return True


def find_matching_bracket(string, index):
    """
    Given a string and a index for a open bracket
    retuns the index for the closing bracket
    """
    counter = 0

    for i in range(index, len(string)):
        if string[i] is "[":
            counter += 1

        elif string[i] is "]":
            counter -= 1

            if not counter:
                return i


def bracket(string, index):
    """
    Returns formated feedback to the user
    after performing the bracket search
    """
    try:
        isbracket = test_index(string[index])

        if not isbracket:
            return "Passed index is not a opening bracket"

        matching = find_matching_bracket(string, index)

        return f"The opening bracket at index: {index}, closes at index: {matching}"

    except IndexError:
        return "Passed index is out of string length"
    except Exception as e:
        print(f"Unexpected error... {e}")


if __name__ == "__main__":
    print(bracket("[ABC[23]][89]", 0))
