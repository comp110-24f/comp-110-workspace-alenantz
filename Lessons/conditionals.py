"""Practice with conditionals."""


def less_than_10(num: int) -> bool:
    """Tell me if num is < 10"""
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
        print("Have a Nice Day!")


less_than_10(num=11)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
