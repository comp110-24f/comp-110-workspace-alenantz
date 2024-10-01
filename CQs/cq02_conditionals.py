__author__: str = "730573848"

secret = 7


def guess_a_number() -> None:
    try:
        guess = int(input("Guess a number: "))

        print(f"Your guess was {guess}")

        if guess == secret:
            print("You got it!")
        elif guess < secret:
            print(f"Your guess was too low! The secret number is {secret}.")
        else:
            print(f"Your guess was too high! The secret number is {secret}.")

    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    guess_a_number()
