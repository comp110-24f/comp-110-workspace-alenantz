"""My first challenge question"""

_author_ = "730573848"


def mimic(message: str) -> str:
    """Returning Hello!"""
    return message


def main() -> None:
    """Using main."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
