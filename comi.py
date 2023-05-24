def comi(C, n, k):
    N_star = list(range(n))
    return FindSubSet(N_star, C, k)

def FindSubSet(N_star, C, k):
    n = len(C)

    if n != k :
        max_sum_el = max(range(len(C)), key=lambda i: sum(C[i]))
        N_star.pop(max_sum_el)
        C.pop(max_sum_el)
        for row in C:
            del row[max_sum_el]
        return FindSubSet(N_star, C, k)
    else:        
        return N_star