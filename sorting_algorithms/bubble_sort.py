# Kyra Lothrop, 101145872, Lab 12
# SYSC 2100 Winter 2021

def bubble_sort(lst: list) -> tuple[int, int]:
    """Bubble sort lst into ascending order and return the number of
    element comparisons and swaps performed while sorting.

    Best case: list is already sorted in ascending order.
    >>> a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> bubble_sort(a_list)
    (45, 0)
    >>> a_list
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Worst case: list is sorted in descending order.
    >>> a_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>>  bubble_sort(a_list)
    (45, 45)
    >>> a_list
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    num_comparisons = 0
    num_swaps = 0

    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):

            num_comparisons += 1
            if lst[j] > lst[j + 1]:
                num_swaps += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return (num_comparisons, num_swaps)


def bubble_sort_short(lst: list) -> tuple[int, int]:
    """Bubble sort lst into ascending order and return the number of
    element comparisons and swaps performed while sorting.
    """
    num_comparisons = 0
    num_swaps = 0

    for i in range(len(lst) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            num_comparisons += 1
            if lst[j] > lst[j + 1]:
                exchanges = True
                num_swaps += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not exchanges:
            break

    return (num_comparisons, num_swaps)