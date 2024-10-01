__author__ = "730573848"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
    return count


if __name__ == "__main__":
    print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))  # Output: 2
    print(num_instances(phrase="HelloHelloHello", search_char="e"))  # Output: 3
    print(num_instances(phrase="Happy Tuesday!", search_char="y"))  # Output: 2
    print(num_instances(phrase="Happy Tuesday!", search_char="z"))  # Output: 0
