def is_prime(number):
    """
    The function first checks if the number is less than or equal to 1 (not prime),
    equal to 2 or 3 (prime), or divisible by 2 or 3 (not prime).
    It then tests divisibility by all numbers of the form 6k ± 1 up to the square root of the number.

    Parameters:
    number (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """

    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if number <= 3:
        return True   # Direct check for 2 and 3, which are prime
    if number % 2 == 0:
        return False  # Exclude all even numbers greater than 2
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False  # If number is divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors were found, it is prime

def generate_primes(n_max):
    """
    Generate a list of prime numbers up to n_max using the Sieve of Eratosthenes.

    Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve = [True] * (n_max + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes
    for i in range(2, int(n_max**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False  # Mark multiples of i as non-prime
    primes = [i for i, prime in enumerate(sieve) if prime]

    return primes


def is_anagram(word_one, word_two):
    """
    Checks pairs of words in a list to determine if they are anagrams of each other.

    This function checks if both words have the same length.
    It checks if all letters in `word_one` are present in `word_two`.
    It does not account for the frequency of letters.
    It does not ignore spaces, punctuation, or case differences.

    Parameters:
    anagram_list (list): A list of strings where each string is a word to be compared.

    Returns:
    bool: True if all adjacent pairs in the list are anagrams, False if any pair is not.
    """

    word_one = word_one.lower()
    word_two = word_two.lower ()
    if len(word_one) != len(word_two):
        return False
    if word_one == word_two:
        return True

    for letter in word_one:
        if letter not in word_two:
            return False

    return True

def is_anagram_set(anagram_list):
    """
    Check if every adjacent pair of words in a list are anagrams of each other.

    The function uses `is_anagram` to compare each pair of adjacent words.
    It assumes the list has at least one word.
    It does **not** ignore spaces, punctuation, or case differences.

    Parameters:
    anagram_list (list of str): A list of strings where each string is a word
                                    that is to be checked against its adjacent pair.

    Returns:
    bool: True if all adjacent pairs in the list are anagrams, False if any pair is not.
    """
    # Normalize the words in the list to lowercase
    normalized_list = [word.lower() for word in anagram_list]

    for i in range(len(normalized_list) - 1):
        if is_anagram(normalized_list[i], normalized_list[i + 1]):
            print(anagram_list[i], anagram_list[i + 1])  # Print original words
        else:
            print("False:", anagram_list[i], anagram_list[i + 1])  # Print original words
            return False

    return True


def is_palindrome(word):
    """
    Determine if two words are palindromic inverses of each other.

    Parameters:
        word (str): The first word.

    Returns:
        bool: True if `word_one` is the same in reverse, False otherwise.
    """
    normalized_word = word.lower()  # Convert to lowercase
    return normalized_word == normalized_word[::-1]


def zigzag(s, k):
    """
    Arrange a string into a zigzag pattern across k lines.

    Parameters:
    s (str): The input string to be converted into zigzag pattern.
    k (int): The number of lines to span the zigzag pattern.

    Returns:
    str: A string representing the zigzag pattern.
    """
    if k == 1 or k >= len(s):
        return s  # No zigzag needed (return original input)

    # Initialize variables
    rows = [""] * k
    row = 0  # Current row
    step = 1  # Direction of traversal
    pos = 0  # Current position in the original string

    # List to keep track of the current length of each row
    row_lengths = [0] * k

    for char in s:
        # Calculate spaces needed before the character
        spaces_needed = pos - row_lengths[row]
        rows[row] += " " * spaces_needed + char
        row_lengths[row] = pos + 1  # Update the length of the current row

        # Move to the next row
        if row == 0:
            step = 1
        elif row == k - 1:
            step = -1
        row += step
        pos += 1

    # Join the rows with newline characters
    result = "\n".join(row.rstrip() for row in rows)
    return result


def test_is_prime():
    prime = generate_primes(7500)
    prime_set = set(prime)
    prime_sm_list = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False
    assert is_prime(97) == True
    assert is_prime(7500) == False

    for n in prime_sm_list:
        assert is_prime(n) == True
    for n in prime:
        assert is_prime(n) == (n in prime_set)


def test_is_anagram():
    assert is_anagram("bored", "robed") == True
    assert is_anagram("dusty", "study") == True
    assert is_anagram("hello", "mellow") == False
    assert is_anagram("player", "slayer") == False
    assert is_anagram_set(["chants", "snatch", "stanch"]) == True
    assert is_anagram_set(["footballer", "cyclist", "touchdown"]) == False
    assert is_anagram_set([]) == True


def test_is_palindrome():
    assert is_palindrome("civic") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("wife") == False
    assert is_palindrome("radar") == True
    assert is_palindrome("modem") == False


def test_zigzag():
    """
    Test cases for the zigzag function.
    """
    # Test Case 1: Basic functionality with k=3 (should return expected output)
    input_string = "ZigZagString"
    k = 3
    expected_output = "Z   a   r\n i Z g t i g\n  g   S   n"
    assert zigzag(input_string, k) == expected_output, "Test 1 Passed"

    # Test Case 2: Edge case with k greater than length of string (should return original string)
    input_string = "hail"
    k = 5
    expected_output = "hail"
    assert zigzag(input_string, k) == expected_output, "Test 2 Failed"

    # Test Case 3: Edge case with k=1 (should return the original string)
    input_string = "JeffBezos"
    k = 1
    expected_output = "JeffBezos"
    assert zigzag(input_string, k) == expected_output, "Test 3 Failed"

    # Test Case 4: Empty string input (should return empty string)
    input_string = ""
    k = 1
    expected_output = ""
    assert zigzag(input_string, k) == expected_output, "Test 4 Failed"


