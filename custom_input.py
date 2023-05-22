import random


def user_input():
    print("\n--------------------------------------------")
    print("Choose data source:")
    print("1. Generate random data")
    print("2. Import data from file")
    print("3. Enter data manually")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        return generate_random_matrix()
    elif choice == '2':
        return input_file()
    elif choice == '3':
        return input_matrix()
    else:
        print("Invalid choice!")
        return None

def generate_random_matrix():
    print("--------------------------------------------")
    n = int(input("Enter the size of the matrix (n): "))
    print("--------------------------------------------")
    k = int(input("Enter the number of objects to find (k): "))
    print("--------------------------------------------")
    if k > n:
            raise ValueError("k must be less than or equal to n.")
    mu = float(input("Enter mu (average value for generation): "))
    print("--------------------------------------------")
    sigma = float(input("Enter sigma (dispersion for values): "))
    print("--------------------------------------------")
    matrix = [[100] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            value = random.normalvariate(mu, sigma)
            
            value = max(0, min(1, value))
            matrix[i][j] = round(value, 2)
            matrix[j][i] = round(value, 2)

    return [matrix, n, k]

def input_matrix():
    print("--------------------------------------------")
    n = int(input("Enter the size of the matrix (n): "))
    print("--------------------------------------------")
    k = int(input("Enter the number of objects to find (k): "))
    print("--------------------------------------------")
    if k > n:
            raise ValueError("k must be less than or equal to n.")
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                matrix[i][j] = 100
            else:
                while True:
                    try:
                        value = float(input(f"Enter the value for element ({i+1},{j+1}) (same as ({j+1},{i+1})): "))
                        if 0.0 <= value <= 1.0:
                            matrix[i][j] = value
                            matrix[j][i] = value
                            break
                        else:
                            print("Invalid input. Please enter a float value between 0 and 1.")
                    except ValueError:
                        print("Invalid input. Please enter a float value.")
    print("--------------------------------------------")

    return [matrix, n, k]

def input_file():
    print("--------------------------------------------")
    filename = input("Enter the filename with your data: ")
    print("--------------------------------------------")
    matrix = []
    with open(filename, 'r') as file:
        n = int(file.readline().strip())  # Read the value of n
        k = int(file.readline().strip())  # Read the value of k
        if k > n:
            raise ValueError("k must be less than or equal to n.")
        for _ in range(n):
            row = list(map(float, file.readline().strip().split()))  # Read a row of the matrix
            if len(row) != n:
                raise ValueError("Matrix dimensions do not match the specified value of n.")
            matrix.append(row)
    
    # Validate matrix properties
    if len(matrix) != n:
        raise ValueError("Matrix dimensions do not match the specified value of n.")
    for i in range(n):
        if len(matrix[i]) != n:
            raise ValueError("Matrix dimensions do not match the specified value of n.")
        if matrix[i][i] != 100:
            raise ValueError("Matrix diagonal values are not equal to 100.")
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                raise ValueError("Matrix is not symmetric.")
    
    return [matrix, n, k]