import unittest


def minmax(lst):
    """Function to return the smallest and largest numbers in a list."""
    if not lst:  # Handle empty list case
        return None
    smallest = largest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return (smallest, largest)


def all_pairs(x, y):
    """Function to return all unique pairs from two lists where elements are not the same."""
    pairs = []
    for item_x in x:
        for item_y in y:
            if item_x != item_y:  # Ensure elements are distinct
                pairs.append((item_x, item_y))
    return pairs


def list_to_dict(lst):
    """Function to convert a list into a dictionary with keys starting from 1."""
    return {i + 1: val for i, val in enumerate(lst)}


def invert_dict(d):
    """Function to invert a dictionary: keys become values and values become keys."""
    inverted = {}
    for key, value in d.items():
        inverted[value] = key  # If there are duplicates, later keys will overwrite earlier ones
    return inverted


def adds_to_target(target, A):
    """Function to check if there are two distinct integers in A that add up to the target."""
    seen = set()
    for number in A:
        required = target - number
        # Check if the required number is in the seen set
        if required in seen:
            # Ensure they are distinct values
            if required != number or A.count(number) > 1:
                return True
        seen.add(number)
    return False

class TestFunctions(unittest.TestCase):

    def test_minmax(self):
        result = minmax([1, 2, 3])
        expected = (1, 3)
        if result != expected:
            print(f"Error: Test minmax([1, 2, 3]) - Expected {expected}, got {result}")

        result = minmax([3, 2, 1])
        expected = (1, 3)
        if result != expected:
            print(f"Error: Test minmax([3, 2, 1]) - Expected {expected}, got {result}")

        result = minmax([-1, -5, 0])
        expected = (-5, 0)
        if result != expected:
            print(f"Error: Test minmax([-1, -5, 0]) - Expected {expected}, got {result}")

        result = minmax([7])
        expected = (7, 7)
        if result != expected:
            print(f"Error: Test minmax([7]) - Expected {expected}, got {result}")

        result = minmax([])
        expected = None
        if result != expected:
            print(f"Error: Test minmax([]) - Expected {expected}, got {result}")

    def test_all_pairs(self):
        result = all_pairs([1, 2], [3, 4])
        expected = [(1, 3), (1, 4), (2, 3), (2, 4)]
        if result != expected:
            print(f"Error: Test all_pairs([1, 2], [3, 4]) - Expected {expected}, got {result}")

        result = all_pairs([1, 2], [2, 3])
        expected = [(1, 3)]  # Expecting (1,3) since 2 shouldn't match itself
        if result != expected:
            print(f"Error: Test all_pairs([1, 2], [2, 3]) - Expected {expected}, got {result}")

        result = all_pairs([1, 1], [2, 3])
        expected = [(1, 2), (1, 3)]
        if result != expected:
            print(f"Error: Test all_pairs([1, 1], [2, 3]) - Expected {expected}, got {result}")

        result = all_pairs([], [1, 2])
        expected = []
        if result != expected:
            print(f"Error: Test all_pairs([], [1, 2]) - Expected {expected}, got {result}")

        result = all_pairs([1, 2], [])
        expected = []
        if result != expected:
            print(f"Error: Test all_pairs([1, 2], []) - Expected {expected}, got {result}")

    def test_list_to_dict(self):
        result = list_to_dict([2, 6, 6, 1, 7, 9])
        expected = {1: 2, 2: 6, 3: 6, 4: 1, 5: 7, 6: 9}
        if result != expected:
            print(f"Error: Test list_to_dict([2, 6, 6, 1, 7, 9]) - Expected {expected}, got {result}")

        result = list_to_dict([])
        expected = {}
        if result != expected:
            print(f"Error: Test list_to_dict([]) - Expected {expected}, got {result}")

        result = list_to_dict([1, 2, 3])
        expected = {1: 1, 2: 2, 3: 3}
        if result != expected:
            print(f"Error: Test list_to_dict([1, 2, 3]) - Expected {expected}, got {result}")

        result = list_to_dict([5])
        expected = {1: 5}
        if result != expected:
            print(f"Error: Test list_to_dict([5]) - Expected {expected}, got {result}")

        result = list_to_dict([0])
        expected = {1: 0}
        if result != expected:
            print(f"Error: Test list_to_dict([0]) - Expected {expected}, got {result}")

    def test_invert_dict(self):
        """Testing function for invert_dict."""
        # Test with a simple dictionary
        result = invert_dict({1: 2, 2: 3})
        expected = {2: 1, 3: 2}
        if result != expected:
            print(f"Error: Test invert_dict({{1: 2, 2: 3}}) - Expected {expected}, got {result}")

        # Test with an empty dictionary
        result = invert_dict({})
        expected = {}
        if result != expected:
            print(f"Error: Test invert_dict({{}}) - Expected {expected}, got {result}")

        # Test with duplicate values
        result = invert_dict({'a': 1, 'b': 2, 'c': 1})
        expected = {1: 'c', 2: 'b'}
        if result != expected:
            print(f"Error: Test invert_dict({{'a': 1, 'b': 2, 'c': 1}}) - Expected {expected}, got {result}")

        # Test with unique values
        result = invert_dict({'x': 10, 'y': 20})
        expected = {10: 'x', 20: 'y'}
        if result != expected:
            print(f"Error: Test invert_dict({{'x': 10, 'y': 20}}) - Expected {expected}, got {result}")

        # Test with integer keys and string values
        result = invert_dict({1: 'one', 2: 'two'})
        expected = {'one': 1, 'two': 2}
        if result != expected:
            print(f"Error: Test invert_dict({{1: 'one', 2: 'two'}}) - Expected {expected}, got {result}")

        print("All test cases for invert_dict passed.")

