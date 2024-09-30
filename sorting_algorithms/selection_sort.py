# Kyra Lothrop, 101145872, Lab 12
# SYSC 2100 Winter 2021

def selection_sort(lst: list) -> tuple[int, int]:
    """Sort lst into ascending order using the selection sort, and return the
    number of element comparisons and swaps performed while sorting.
    """
    num_comparisons = 0
    num_swaps = 0

    for i, item in enumerate(lst):
        min_idx = len(lst) - 1
        for j in range(i, len(lst)):
            num_comparisons += 1
            if lst[j] < lst[min_idx]:
                min_idx = j

        if min_idx != i:
            num_swaps += 1
            lst[min_idx], lst[i] = lst[i], lst[min_idx]

    return (num_comparisons, num_swaps)