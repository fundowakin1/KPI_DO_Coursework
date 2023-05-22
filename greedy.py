def greedy_selection(C, n, k):
    # Створюємо список пар об’єктів, відсортований за зростанням сумісності
    pairs = [(i, j, C[i][j]) for i in range(n) for j in range(i + 1, n)]
    pairs.sort(key=lambda x: x[2])

    # Створюємо порожній список S
    S = []

    # Додаємо об’єкти до S згідно з жадібним алгоритмом
    for i, j, c in pairs:
        if len(S) == k:
            break
        if i not in S and j not in S and len(S) == 0:
            S.append(i)
            S.append(j)
        elif i not in S and j in S:
            S.append(i)
        elif i in S and j not in S:
            S.append(j)

    # Повертаємо список S
    return S