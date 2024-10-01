__author__: str = "730573848"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user for a guess of a specific length and return the valid guess."""
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the character `char_guess` is present in the `secret_word`."""
    assert len(char_guess) == 1, "char_guess must be a single character!"

    for char in secret_word:
        if char == char_guess:
            return True
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis indicating the accuracy of the guess."""
    assert len(guess) == len(secret), "Guess and secret must be the same length."

    result = ""

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    return result


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    turns = 1
    max_turns = 6

    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")

        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            return

        turns += 1

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
