import random
import unittest
from collections import defaultdict
from itertools import cycle
from unittest.mock import patch


def mask_word(word, guessed):
    """Returns word with all letters not in guessed replaced with hyphens."""
    masked_word = ""  # Initialize an empty string to build the masked word
    for letter in word:  # Iterate through each letter in the input word
        if letter in guessed:  # Check if the letter has been guessed
            masked_word += letter  # If guessed, add the letter to masked_word
        else:
            masked_word += "-"  # If not guessed, add a hyphen instead
    return masked_word


def partition(words, guessed):
    """Generates the partitions of the set words based upon guessed letters."""
    partitions = defaultdict(set)
    for word in words:
        hint = mask_word(word, guessed)
        partitions[hint].add(word)
    return partitions


def max_partition(partitions):
    """Returns the hint for the largest partite set."""
    max_size = 0
    best_hint = None
    tie_breaker = []

    for hint, part in partitions.items():
        size = len(part)
        revealed = sum(1 for c in hint if c != "-")

        if size > max_size or (
            size == max_size
            and (best_hint is None or revealed < sum(1 for c in best_hint if c != "-"))
        ):
            max_size = size
            best_hint = hint
            tie_breaker = [hint]
        elif size == max_size and sum(1 for c in hint if c != "-") == sum(
            1 for c in best_hint if c != "-"
        ):
            tie_breaker.append(hint)

    if len(tie_breaker) > 1:
        best_hint = random.choice(tie_breaker)

    return best_hint


def read_words(file_path="C:\\Users\\Dave Rowan\\Documents\\words.txt", length=None):
    """Read words from a file and filter by the specified length.

    Args:
        file_path (str): The path to the words file.
        length (int): The desired word length. If None, all words are returned.

    Returns:
        set: A set of words of the specified length.
    """
    with open(file_path, "r") as file:
        if length:
            return {line.strip() for line in file if len(line.strip()) == length}
        return {line.strip() for line in file}


def play_game():
    """Main game loop for playing Hangman."""
    print("Starting the game...")
    try:
        word_length = int(input("What word length? "))
    except ValueError:
        print("Invalid input! Please enter a valid number for word length.")
        return

    word_length = abs(word_length) if word_length < 1 else word_length

    # Read and filter words from the file
    words = read_words(length=word_length)
    if not words:
        print("No words of the specified length found.")
        return

    guessed = set()
    incorrect_guesses = 0
    max_incorrect = 5
    hint = "-" * word_length

    while incorrect_guesses < max_incorrect:
        print(f"\nYou have {max_incorrect - incorrect_guesses} guesses remaining.")
        print(f"Guessed letters: {guessed}.")
        print(f"Current hint: {hint}.")

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue
        if guess in guessed:
            print("That letter has already been guessed.")
            continue

        guessed.add(guess)
        partitions = partition(words, guessed)
        chosen_hint = max_partition(partitions)

        # Assess if the guess was correct or not
        if hint == chosen_hint:
            incorrect_guesses += 1
            print(f"I'm sorry '{guess}' is not in the word.")
        else:
            hint = chosen_hint
            words = partitions[hint]

        if "-" not in hint:  # Player has guessed the word
            print(f"You win! The word was '{hint}'.")
            return  # Exit the game after winning

    # Player has lost after max incorrect guesses
    print(f"You lost. The correct word was '{random.choice(tuple(words))}'.")


def test_mask_word():
    try:
        assert mask_word("quiz", {"q", "u"}) == "qu--", "Test failed: Partial guess"
        assert (
            mask_word("quiz", {"q", "u", "i", "z"}) == "quiz"
        ), "Test failed: Full guess"
        assert mask_word("quiz", set()) == "----", "Test failed: No guess"
    except AssertionError as e:
        print(e)


def test_partition():
    # Test case: Partition based on guessed letters
    words = {"quiz", "shiv", "wave"}
    guessed = {"q"}
    expected = {"q---": {"quiz"}, "----": {"shiv", "wave"}}
    try:
        assert partition(words, guessed) == expected, "Test failed: Partition mismatch"
    except AssertionError as e:
        print(e)


def test_max_partition():
    # Test case 1: Largest partition (by number of words)
    partitions = {"q---": {"quiz"}, "----": {"shiv", "wave"}, "-a-e": {"wave"}}
    try:
        assert max_partition(partitions) == "----", "Test failed: Largest partition"
    except AssertionError as e:
        print(e)

    # Test case 2: Tie-breaking (based on fewer revealed letters)
    partitions = {
        "-i--": {"shiv", "quiz"},
        "-a-e": {"wave"},
    }
    try:
        assert max_partition(partitions) == "-i--", "Test failed: Tie-breaking"
    except AssertionError as e:
        print(e)

    @patch("builtins.input", side_effect=cycle(["4", "x", "y", "z", "q", "e"]))
    @patch("builtins.print")
    @patch(
        "builtins.open",
        new_callable=lambda: unittest.mock.mock_open(read_data="abcd\nbcde\ncdef"),
    )
    def test_lose_game(self, mock_open, mock_print, mock_input):
        # Test losing the game after 5 incorrect guesses
        play_game()
        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("You lost. The correct word was", output)

    @patch("builtins.input", side_effect=cycle(["4", "a", "a", "b", "b", "c", "d"]))
    @patch("builtins.print")
    @patch(
        "builtins.open",
        new_callable=lambda: unittest.mock.mock_open(read_data="abcd\nbcde\ncdef"),
    )
    def test_repeated_guesses(self, mock_open, mock_print, mock_input):
        # Test repeated guesses and ensure warnings are shown
        play_game()
        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("That letter has already been guessed.", output)

    @patch("builtins.input", side_effect=cycle(["4", "a", "b", "c", "d"]))
    @patch("builtins.print")
    @patch(
        "builtins.open",
        new_callable=lambda: unittest.mock.mock_open(read_data="abcd\nbcde\ncdef"),
    )
    def test_win_game(self, mock_open, mock_print, mock_input):
        # Test winning the game with correct guesses
        play_game()
        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("You win! The word was 'abcd'.", output)


if __name__ == "__main__":
    test_max_partition()
    test_mask_word()
    play_game()