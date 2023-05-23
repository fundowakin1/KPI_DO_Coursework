import numpy as np
from datetime import datetime

def print_results(numbers):
    print("--------------------------------------------")
    print("Results:")
    print("--------------------------------------------")
    print("The most compatible objects:")
    for number in numbers:
        print(f"\t{number+1}")
    print("--------------------------------------------")

    return [x+1 for x in numbers] 


def write_file(numbers, matrix):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Results {current_datetime}.txt"
    
    with open(filename, 'w') as file:
        file.write("Matrix C:\n")
        
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        
        file.write('\n')
        
        file.write("The results (S):\n")
        for number in numbers:
            file.write(str(number) + '\n')
