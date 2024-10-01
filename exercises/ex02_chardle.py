__author__: str = "730573848"


def input_word() -> str:
    """
    Prompts the user to enter a 5-character word.
    If the word length is not 5, prints an error message and exits the program.
    Returns the input word."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Exit the program if the word length is not 5
    return word


def input_letter() -> str:
    """
    Prompts the user to enter a single character.
    If the input length is not 1, prints an error message and exits the program.
    Returns the input character.
    """
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # Exit the program if the input length is not 1
    return letter


def contains_char(word: str, letter: str) -> None:
    """
    Searches for the input character in the input word.
    Prints the indices where the character is found.
    Counts and prints the number of instances of the character in the word.
    """
    print(f"Searching for {letter} in {word}")
    count = 0  # Initialize a counter for the number of matches
    for i in range(len(word)):
        if word[i] == letter:
            print(f"{letter} found at index {i}")
            count += 1  # Increment the counter for each match
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    """
    Main function to coordinate the flow of the Chardle game.
    Calls input_word, input_letter, and contains_char functions.
    """
    contains_char(word=input_word(), letter=input_letter())


# This ensures that the main function is called when the script is run directly
if __name__ == "__main__":
    main()
