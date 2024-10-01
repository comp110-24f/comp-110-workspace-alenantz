__author__: str = "730573848"


def get_coords(xs: str, ys: str) -> None:
    """Prints all character pairs from two strings."""
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print(f"({xs[i]},{ys[j]})")
            j += 1
        i += 1
