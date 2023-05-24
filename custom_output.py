from datetime import datetime
import itertools

def print_results(numbers, matrix):
    print("--------------------------------------------")
    print("Results:")
    print("--------------------------------------------")
    print("The most compatible objects:")
    for number in numbers:
        print(f"\t{number+1}")
    print("--------------------------------------------")
    print("The sum compatibility:")
    print(calculate_sum_of_combinations(numbers, matrix))
    print("--------------------------------------------")

    return [x+1 for x in numbers] 


def calculate_sum_of_combinations(list_of_indexes, matrix):
    pairs = itertools.combinations(list_of_indexes, 2)
    sum_of_combinations = 0

    for pair in pairs:
        i, j = pair
        sum_of_combinations += matrix[i][j]

    return sum_of_combinations


def write_file(numbers, matrix, alg_name):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Results {current_datetime} {alg_name}.txt"
    
    with open(filename, 'w') as file:
        file.write("Matrix C:\n")
        
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        
        file.write('\n')
        
        file.write("The results (S):\n")
        for number in numbers:
            file.write(str(number) + '\n')

        file.write('\n')

        file.write("The sum compitability:\n")
        file.write(str(calculate_sum_of_combinations([x-1 for x in numbers] , matrix)))
