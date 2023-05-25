import itertools

def brute_force(C, n, k):
    bestSubset  = []
    maxCompatibility = 1000000

    for subset in itertools.combinations(range(1, n + 1), k):
        compatibility = 0
        for i in range(k):
            for j in range(i + 1, k):
                compatibility += C[subset[i] - 1][subset[j] - 1]
        if compatibility < maxCompatibility:
            maxCompatibility = compatibility
            bestSubset  = subset


    return [x-1 for x in bestSubset] 