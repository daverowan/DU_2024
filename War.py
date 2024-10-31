import random

suits = ['H', 'D', 'C', 'S']
values = list(range(2, 15))  # 2-14 (Ace is 14. Range is 2 to 14)
deck = [(value, suit) for value in values for suit in suits]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    shuffled_deck = shuffle_deck(deck.copy())
    return shuffled_deck[:26], shuffled_deck[26:]


def play_hand(player1_deck, player2_deck):
    winner = None
    common_pool = []
    while winner is None:
        if not player1_deck or not player2_deck:
            return None  # Game ends in a tie if player runs out of cards

        card1 = player1_deck.pop(0)
        card2 = player2_deck.pop(0)
        common_pool.extend([card1, card2])

        if card1[0] > card2[0]:
            winner = 1
        elif card1[0] < card2[0]:
            winner = 2

    # Shuffle common pool before awarding to winner
    random.shuffle(common_pool)

    if winner == 1:
        player1_deck.extend(common_pool)
    else:
        player2_deck.extend(common_pool)

    return winner

def play_game():
    player1_deck, player2_deck = deal_cards(deck)
    rounds = 0
    while player1_deck and player2_deck:
        winner = play_hand(player1_deck, player2_deck)
        if winner is None:
            return rounds, None  # Draw
        rounds += 1
    if not player1_deck:
        return rounds, 2  # Player 2 wins
    else:
        return rounds, 1  # Player 1 wins

def run_simulations(num_games):
    total_hands = 0
    player1_wins = 0
    player2_wins = 0
    draws = 0

    for _ in range(num_games):
        hands, winner = play_game()
        total_hands += hands
        if winner == 1:
            player1_wins += 1
        elif winner == 2:
            player2_wins += 1
        else:
            draws += 1

    average_hands = total_hands / num_games if num_games > 0 else 0
    return average_hands, player1_wins, player2_wins, draws

def run_tests():
    print("Running Tests...")
    # Test play_hand function
    p1 = [(2, 'H')]  # Player 1 has a 2 of Hearts
    p2 = [(3, 'H')]  # Player 2 has a 3 of Hearts
    result = play_hand(p1, p2)  # Player 2 should win

    # Check if the result (the winner) is correct
    assert result == 2, "Error: Player 2 should win!"
    print("All tests passed!")

if __name__ == "__main__":
    num_games = 1000  # Number of games to simulate
    run_tests()      # Execute the tests first
    print(f"\nRunning {num_games} games...")
    avg_length, p1_wins, p2_wins, draws = run_simulations(num_games)  # Run the simulations
    print(f"Average game length: {avg_length:.2f} rounds")
    print(f"Player 1 wins: {p1_wins}")
    print(f"Player 2 wins: {p2_wins}")
    print(f"Draws: {draws}")
