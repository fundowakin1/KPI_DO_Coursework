import itertools

def MaxCompatibleSubset(k, c, n):
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


c = [[99, 0.1, 1, 0.6],
     [99, 99, 0.3, 0.5],
     [99, 99, 99, 0.9],
     [99, 99, 99, 99]]

k = 3
print(MaxCompatibleSubset(k, c, len(c)))