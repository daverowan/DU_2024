def print_help():
    # Print the list of commands
    print("Acceptable commands: help, quit, square, box, diagonaldown, diagonalup, checkerboard")


def get_valid_size(min_size, max_size):
    while True:
        size_input = input(f"Enter size ({min_size}-{max_size}): ")
        if size_input.isdigit():
            size = int(size_input)
            if min_size <= size <= max_size:
                return size
            else:
                print("Size is out of range.")
        else:
            print("Invalid input, please enter an integer.")


def draw_square(size):
    # Draw a filled square of a given size
    for i in range(size):
        print("*" * size)


def draw_box(size):
    # Draw an empty box of a given size
    print("*" * size)  # Print top edge
    for i in range(size - 2):
        print("*" + " " * (size - 2) + "*")  # Print sides
    if size > 1:
        print("*" * size)  # Print bottom edge


def draw_diagonal_down(size):
    # Draw a diagonal line downwards (top left to bottom right)
    for i in range(size):
        print(" " * i + "*")


def draw_diagonal_up(size):
    # Draw a diagonal line upwards (bottom left to top right)
    for i in range(size):
        print(" " * (size - i - 1) + "*")


def draw_checkerboard(size):
    # Draw a checkerboard pattern
    for i in range(size):
        row = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                row += "*"  # Add a star
            else:
                row += " "  # Add a space
        print(row)


active = True
# List of commands
valid_commands = ["help", "quit", "square", "box", "diagonaldown", "diagonalup", "checkerboard"]

while active:
    command = input("Enter a command: ").strip().lower()

    if command == "help":
        print_help()
    elif command == "quit":
        print("Goodbye!")
        active = False
    elif command == "square":
        size = get_valid_size(1, 15)
        draw_square(size)
    elif command == "box":
        size = get_valid_size(3, 15)
        draw_box(size)
    elif command == "diagonaldown":
        size = get_valid_size(3, 15)
        draw_diagonal_down(size)
    elif command == "diagonalup":
        size = get_valid_size(3, 15)
        draw_diagonal_up(size)
    elif command == "checkerboard":
        size = get_valid_size(5, 15)
        draw_checkerboard(size)

    else:
        print("Invalid command. Use: help, quit, square, box, diagonaldown, diagonalup, checkerboard")