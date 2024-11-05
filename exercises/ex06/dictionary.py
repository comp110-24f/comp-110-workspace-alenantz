__author__: str = "730573848"


from typing import Dict, List


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """
    Inverts the keys and values of the input dictionary.

    Parameters:
    input_dict (dict[str, str]): The dictionary to invert.

    Returns:
    dict[str, str]: The inverted dictionary.

    Raises:
    KeyError: If duplicate values are found in the input dictionary.
    """
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """
    Returns the most frequent favorite color from the dictionary.

    Parameters:
    color_dict (dict[str, str]): A dictionary of names and their favorite colors.

    Returns:
    str: The most popular color. If there's a tie, the first color in the dictionary wins.
    """
    color_count: Dict[str, int] = {}
    for name, color in color_dict.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_count = 0
    favorite = ""
    for color, count in color_count.items():
        if count > max_count:
            max_count = count
            favorite = color
        elif count == max_count:
            if list(color_dict.values()).index(color) < list(color_dict.values()).index(
                favorite
            ):
                favorite = color

    return favorite


def count(input_list: list[str]) -> dict[str, int]:
    """
    Counts the occurrences of each item in the input list.

    Parameters:
    input_list (list[str]): The list of items to count.

    Returns:
    dict[str, int]: A dictionary where keys are items from the list and values are their counts.
    """
    count_dict: Dict[str, int] = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """
    Categorizes words into lists based on their starting letter.

    Parameters:
    word_list (list[str]): The list of words to categorize.

    Returns:
    dict[str, list[str]]: A dictionary where each key is a letter and each value is a list of words starting with that letter.
    """
    alphabet_dict: Dict[str, List[str]] = {}
    for word in word_list:
        initial = word[0].lower()
        if initial in alphabet_dict:
            alphabet_dict[initial].append(word)
        else:
            alphabet_dict[initial] = [word]
    return alphabet_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    """
    Updates the attendance record for a given day and student.

    Parameters:
    attendance_dict (dict[str, list[str]]): The existing attendance dictionary.
    day (str): The day of the week.
    student (str): The student who attended.

    Returns:
    None
    """
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
