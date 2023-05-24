import copy

def comi(C, n, k):
    N_star = list(range(n))
    C_copy = copy.deepcopy(C)
    return FindSubSet(N_star, C_copy, k)

def FindSubSet(N_star, C_copy, k):
    n = len(C_copy)

    if n != k :
        max_sum_el = max(range(len(C_copy)), key=lambda i: sum(C_copy[i]))
        N_star.pop(max_sum_el)
        C_copy.pop(max_sum_el)
        for row in C_copy:
            del row[max_sum_el]
        return FindSubSet(N_star, C_copy, k)
    else:        
        return N_star