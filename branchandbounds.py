import numpy as np

def branch_and_bounds(C, n, k):
    N = list(range(1, n+1))
    max_compat = 100000000000
    best_subset = []

    def backtrack(subset, curr_index, curr_compat):
        nonlocal max_compat, best_subset

        if len(subset) == k:  # Subset size reached k
            if curr_compat < max_compat:
                max_compat = curr_compat
                best_subset = subset[:]
            return

        if curr_index >= n:  # Reached the end of the object list
            return

        if len(subset) + n - curr_index < k:  # Not enough objects remaining
            return

        # Branching: Include current object
        subset.append(N[curr_index])
        backtrack(subset, curr_index + 1, calc_total_compat(subset))
        subset.pop()

        # Bound: Exclude current object
        backtrack(subset, curr_index + 1, curr_compat)

    def calc_total_compat(subset):
        total = 0.0
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                total += C[subset[i] - 1][subset[j] - 1]
        return total

    backtrack([], 0, 0.0)
    return [x-1 for x in best_subset]