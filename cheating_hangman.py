from collections import defaultdict
import random

def mask_word(word, guessed):
    """Returns word with all letters not in guessed replaced with hyphens.
     Args:
        word (str): the word to mask
        guessed (set): the guessed letters
    Returns:
        str: the masked word
        """
    masked_word = ""  # Initialize an empty string to build the masked word
    for letter in word:  # Iterate through each letter in the input word
        if letter in guessed:  # Check if the letter has been guessed
            masked_word += letter  # If guessed, add the letter to masked_word
        else:
            masked_word += "-"  # If not guessed, add a hyphen instead
    return masked_word

def partition(words, guessed):
    """Generates the partitions of the set words based upon guessed letters. Partition the set of words based on the guessed letters.
    Args:
        words (set): the word set
        guessed (set): the guessed letters
    Returns:
        dict: The partitions
        """
    partitions = defaultdict(set)
    for word in words:
        hint = mask_word(word, guessed)
        partitions[hint].add(word)
    return partitions

def max_partition(partitions):
    """Returns the hint for the largest partite set.
    Args:
        partitions (dict): partitions from partition function
    Returns:
        str: hint for the largest partite set
        """
    max_size = 0
    best_hint = None
    tie_breaker = []

    for hint, part in partitions.items():
        size = len(part)
        revealed = sum(1 for c in hint if c != "-")

        if (size > max_size or
                (size == max_size and (best_hint is None or revealed < sum(1 for c in best_hint if c != "-")))):
            max_size = size
            best_hint = hint
            tie_breaker = [hint]
        elif size == max_size and sum(1 for c in hint if c != "-") == sum(1 for c in best_hint if c != "-"):
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
    with open(file_path, 'r') as file:
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

        if hint == chosen_hint:
            incorrect_guesses += 1
            print(f"I'm sorry '{guess}' is not in the word.")
        else:
            hint = chosen_hint
            words = partitions[hint]

        if '-' not in hint:  # Player has guessed the word
            print(f"You win! The word was '{hint}'.")
            return  # Exit the game after winning

    # Player has lost after max incorrect guesses
    print(f"You lost. The correct word was '{random.choice(tuple(words))}'.")

def test_mask_word():
    #Test 1
    try:
        assert mask_word("quiz", {"q", "u"}) == "qu--", "Test failed: Partial guess"
        assert mask_word("quiz", {"q", "u", "i", "z"}) == "quiz", "Test failed: Full guess"
        assert mask_word("quiz", set()) == "----", "Test failed: No guess"
    except AssertionError as e:
        print(e)

    #Test 2
    try:
        assert mask_word("quiz", {"q", "u"}) == "qu--", "Test failed: Partial guess for 'quiz'"
        assert mask_word("shiv", {"s", "h", "i", "v"}) == "shiv", "Test failed: Full guess for 'shiv'"
        assert mask_word("wave", {"w"}) == "w---", "Test failed: Partial guess for 'wave'"
        assert mask_word("wave", set()) == "----", "Test failed: No guess for 'wave'"
    except AssertionError as e:
        print(e)

    #Test 3
    try:
        assert mask_word("quiz", {"z"}) == "---z", "Test failed: Last letter guessed in 'quiz'"
        assert mask_word("shiv", {"i"}) == "--i-", "Test failed: Middle letter guessed in 'shiv'"
        assert mask_word("wave", {"a", "e"}) == "-a-e", "Test failed: Multiple letters guessed in 'wave'"
        assert mask_word("quiz", {"q", "u", "i"}) == "qui-", "Test failed: First three letters guessed in 'quiz'"
    except AssertionError as e:
        print(e)

def test_partition():
    # Test 1:
    words = {"quiz", "shiv", "wave"}
    guessed = {"q"}
    expected = {"q---": {"quiz"}, "----": {"shiv", "wave"}}
    try:
        assert partition(words, guessed) == expected, "Test failed: Partition mismatch"
    except AssertionError as e:
        print(e)

    # Test 2:
    words = {"quiz", "shiv", "wave"}
    guessed = {"i", "w"}
    expected = {"----": {"shiv"}, "w---": {"wave"}, "q---": {"quiz"}}
    try:
        assert partition(words, guessed) == expected, "Test failed: Partition mismatch"
    except AssertionError as e:
        print(e)

    # Test 3:
    words = {"quiz", "shiv", "wave"}
    guessed = {"q", "s", "v"}
    expected = {"q---": {"quiz"}, "---i-": {"shiv"}, "--a--": {"wave"}}
    try:
        assert partition(words, guessed) == expected, "Test failed: Partition mismatch"
    except AssertionError as e:
        print(e)

def test_max_partition():
    # Test 1: Largest set
    partitions = {
        "q---": {"quiz"},
        "----": {"shiv", "wave"},
        "-a-e": {"wave"}
    }
    try:
        assert max_partition(partitions) == "----", "Test failed: Largest partition"
    except AssertionError as e:
        print(e)

    # Test 2:Tie breaking/Largest set
    partitions = {
        "-i--": {"shiv", "quiz"},
        "-a-e": {"wave"},
    }
    try:
        assert max_partition(partitions) == "-i--", "Test failed: Tie-breaking"
    except AssertionError as e:
        print(e)

# Test 3: Tie breaking/Largest set x 2
    partitions = {
        "-i--": {"quiz", "shiv"},
        "--i-": {"jive", "wave"},
    }
    try:
        chosen = max_partition(partitions)
        assert chosen in {"-i--", "--i-"}, "Test failed: Partition tie-breaking"
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    play_game()