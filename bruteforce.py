import itertools

def brute_force(k, c, n):
    bestSubset  = []
    maxCompatibility = 100

    for subset in itertools.combinations(range(1, n + 1), k):
        compatibility = 0
        for i in range(k):
            for j in range(i + 1, k):
                compatibility += c[subset[i] - 1][subset[j] - 1]
        if compatibility < maxCompatibility:
            maxCompatibility = compatibility
            bestSubset  = subset

    return bestSubset 