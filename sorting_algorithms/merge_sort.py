# Kyra Lothrop, 101145872, Lab 12
# SYSC 2100 Winter 2021

def merge_sort(lst: list) -> tuple[int, int]:
    """Sort lst into ascending order using the merge sort, and return the
    number of element comparisons and swaps performed while sorting.
    """

    num_comparisons = 0
    num_swaps = 0

    if len(lst) > 1:
        # Divide into a left and right half
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Recursive function
        comparison_left, swap_left = merge_sort(left_half)
        comparison_right, swap_right = merge_sort(right_half)

        num_comparisons += comparison_left + comparison_right
        num_swaps += swap_left + swap_right

        i, j, k = 0, 0, 0

        # Compare an element in the left_half to the right_half, the half that
        # has the smaller element gets placed in the lst and goes to the next
        # element in that half
        while i < len(left_half) and j < len(right_half):
            num_comparisons += 1
            num_swaps += 1
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                i = i + 1
            else:
                lst[k] = right_half[j]
                j = j + 1
            k = k + 1

        # Put whats left from the left_half into the list
        while i < len(left_half):
            num_swaps += 1
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        # Put whats left from the right_half into the list
        while j < len(right_half):
            num_swaps += 1
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1

    return (num_comparisons, num_swaps)