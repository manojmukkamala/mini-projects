from itertools import count


def count_down(start):
    print(start)

    next = start - 1
    if next > 0:
        count_down(next)

count_down(3)