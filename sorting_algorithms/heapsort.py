# Kyra Lothrop, 101145872, A3
# SYSC 2100 Winter 2021 - heapsort

def heapsort(lst: list) -> tuple[int, int]:
    """Sort the elements in lst into ascending order."""

    num_comparisons = 0
    num_swaps = 0

    # Form lst into a max heap.
    comparisons, swaps = heapify(lst)
    num_comparisons += comparisons
    num_swaps += swaps
    last = len(lst) - 1  # index of rightmost node on the lowest level
    # of the heap.

    # After each iteration, the sublist lst[0] .. lst[last] is a heap,
    # and the elements in lst[last + 1] .. lst[len(lst) - 1] are in
    # ascending order.

    while last > 0:
        # Swap lst[0] (the largest value in the heap) and lst[last].
        # This moves the largest value out of the heap and places it at
        # the front of the sequence of sorted values.

        lst[0], lst[last] = lst[last], lst[0]
        num_swaps += 1
        last -= 1

        # lst[0] .. lst[last] is a "damaged" heap.
        # lst[last+1] .. lst[len(lst) - 1] contains values removed from the
        # heap, sorted in ascending order.
        # Restore lst[0] .. lst[last] into a heap.

        comparisons, swaps = _perc_down(lst, 0, last)
        num_comparisons += comparisons
        num_swaps += swaps

    return (num_comparisons, num_swaps)


def _perc_down(lst: list, root: int, last: int) -> tuple[int, int]:
    """Restore lst[root] .. lst[last] to a max heap.

    lst[root] is the root node of the complete binary tree stored in the
    sublist lst[root] .. lst[last]. The left and right subtrees of
    lst[root] (if they exist) satisfy the heap property. Percolate the
    root node down the tree until lst[root] .. lst[last] is a heap.
    """
    # If lst[root] has a left child, it's lst[2 * root + 1],
    # and its index is <= last.

    num_comparisons = 0
    num_swaps = 0

    left_child = 2 * root + 1
    while left_child <= last:

        # lst[root] has at least one child (the left child).
        # If it has a right child, it's lst[left_child + 1],
        # and its index is <= last.

        if left_child + 1 <= last:

            # lst[root] has two children. Determine which one is larger.
            num_comparisons += 1
            if lst[left_child] < lst[left_child + 1]:
                largest_child = left_child + 1
            else:
                largest_child = left_child
        else:
            # lst[root] has one child (the left child)
            largest_child = left_child

        num_comparisons += 1
        if lst[root] > lst[largest_child]:

            #  lst[root] is larger than its largest child, so we're done.
            return (num_comparisons, num_swaps)

        # Swap lst[root] and its largest child.
        num_swaps += 1
        lst[root], lst[largest_child] = lst[largest_child], lst[root]

        # lst[largest_child] is the node we just moved down a level.
        # If necessary, continue to percolate it down the tree.

        root = largest_child
        left_child = 2 * root + 1

    return (num_comparisons, num_swaps)


def heapify(lst: list) -> tuple[int, int]:
    """Turn lst into a max heap."""
    # lst represents a complete binary tree. The last node in the tree is
    # located at index (len(lst) - 1). The parent of the node at position i
    # is (i - 1) // 2.
    #
    # last_node = len(lst) - 1
    # parent = (last_node - 1) // 2

    num_comparisons = 0
    num_swaps = 0

    parent = (len(lst) - 2) // 2

    while parent >= 0:
        # Percolate the node at lst[parent] down the tree, so that all
        # nodes in the sublist lst[parent] .. lst[len(lst) - 1] satisfy
        # the heap property.

        comparisons, swaps = _perc_down(lst, parent, len(lst) - 1)
        num_comparisons += comparisons
        num_swaps += swaps
        # Move backwards through the nodes until we've processed the
        # root node, lst[0].

        parent -= 1

    return (num_comparisons, num_swaps)