import random


def single_trial(num_people):
    # Create a list to track which birthdays have been taken
    birthdays = [False] * 365  # 365 days in a year

    for i in range(num_people):
        # Generate a random birthday for each person (0 to 364)
        birthday = random.randint(0, 364)

        # Check if this birthday is already taken
        if birthdays[birthday]:  # If True, then it is already taken
            return True  # There is a shared birthday
        # Mark this birthday as shared
        birthdays[birthday] = True

    return False  # No shared birthdays


def run_trials(num_people, num_trials):
    successes = 0  # of successful trials

    for _ in range(num_trials):
        if single_trial(num_people):  # Run a single trial
            successes += 1  # Increment success count

    return successes  # Return the number of successful trials


# Welcome message
print("Welcome to the Shared Birthday Simulator")
num_trials = 100000  # Setting the number of trials to conduct

# Get threshold from the user
valid_input = False
while not valid_input:
    threshold = input("What threshold would you like? (enter as a percent) ")

    # Validate input
    try:
        threshold = int(threshold)
        if 0 <= threshold <= 100:
            valid_input = True  # Valid input, exit loop
        else:
            print("Error: Please enter a number between 0 and 100.")
    except ValueError:
        print("Error: Not a valid percent. Please enter a number.")

num_people = 2 # Start with 2 people and keep increasing until threshold is met

while True:
    # Run the trials for the current number of people
    success_count = run_trials(num_people, num_trials)
    probability = (success_count / num_trials) * 100  # Calculate probability

    # Print out the results for this number of people
    print(
        f"For {num_people} people, the probability of a shared birthday was {success_count} / {num_trials} or {probability:.2f}%")

    # Check if the threshold is met
    if probability >= threshold:
        print(f"To achieve at least {threshold}% probability of a collision, need {num_people} people in the room.")
        break  # Exit loop

    num_people += 1  # Increment the number of people for the next trial

print("Thank you for using the Shared Birthday Simulator!")