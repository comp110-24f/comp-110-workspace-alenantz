__author__: str = "730573848"


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings."""
    return str1 + str2
    # Global variables


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    # Print the result of calling concat with word1 and word2
    print(concat(word1, word2))
