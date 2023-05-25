import random
from branchandbounds import branch_and_bounds
from bruteforce import brute_force
from greedy import greedy_selection
from comi import comi
import time
import matplotlib.pyplot as plt


def dimention_to_time_experiment():
    n = 10
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")
    
    R = float(input("Enter R (number of dimentions): "))
    print("--------------------------------------------")

    
    k = int(0.5*n)
    
    J = int(input("Enter the number of experiments for each n: "))
    print("--------------------------------------------")
    
    mu = 0.5
    sigma = mu*0.9

    dimensions = []
    average_time_greedy_list = []
    average_time_branch_list = []
    average_time_brute_list = []
    average_time_comi_list = []

    r = 0

    while r <= R:
        counter = 0
        current_size = r+n

        dimensions.append(current_size)
        
        average_time_greedy = 0
        average_time_branch = 0
        average_time_brute = 0
        average_time_comi = 0

        while counter < J:

            matrix = [[100] * current_size for _ in range(current_size)]

            for i in range(current_size):
                for j in range(i + 1, current_size):
                    value = random.normalvariate(mu, sigma)
                    
                    value = max(0, min(1, value))
                    matrix[i][j] = round(value, 2)
                    matrix[j][i] = round(value, 2)

            results_list = solving_problem(matrix, current_size, int(current_size*0.5))
            average_time_greedy += results_list[0]
            average_time_branch += results_list[1]
            average_time_brute += results_list[2]
            average_time_comi += results_list[3]
            
            counter += 1
        
        average_time_greedy_list.append(average_time_greedy / J)
        average_time_branch_list.append(average_time_branch / J)
        average_time_brute_list.append(average_time_brute / J)
        average_time_comi_list.append(average_time_comi / J)

        print(f"Processed for n: {current_size}, k: {int(current_size*0.5)}")

        r+=1

    plt.plot(dimensions, average_time_greedy_list, marker='o', label='Greedy')
    plt.plot(dimensions, average_time_branch_list, marker='o', label='Branch and Bounds')
    plt.plot(dimensions, average_time_brute_list, marker='o', label='Bruteforce')
    plt.plot(dimensions, average_time_comi_list, marker='o', label='COMI')
    plt.xlabel('Dimension of the Problem')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Execution Time vs. Problem Dimension')
    plt.legend()
    plt.grid(True)
    plt.show()

        
    return []

def finalvalues_to_time_experiment():
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")
    n = int(input("Enter size of matrix n: "))
    print("--------------------------------------------")
    
    k = float(input("Enter number of changes of k: "))
    print("--------------------------------------------")

    if k>n:
        raise ValueError("k cannot be > then n!") 
    
    J = int(input("Enter the number of experiments for each n: "))
    print("--------------------------------------------")
    
    mu = 0.5
    sigma = mu*0.9

    dimensions = []
    average_time_greedy_list = []
    average_time_branch_list = []
    average_time_brute_list = []
    average_time_comi_list = []

    r = 0
    delta_k = int(n/k)
    current_k = 0

    while r < k:
        counter = 0
        current_k += delta_k

        dimensions.append(current_k)
        
        average_time_greedy = 0
        average_time_branch = 0
        average_time_brute = 0
        average_time_comi = 0

        while counter < J:

            matrix = [[100] * n for _ in range(n)]

            for i in range(n):
                for j in range(i + 1, n):
                    value = random.normalvariate(mu, sigma)
                    
                    value = max(0, min(1, value))
                    matrix[i][j] = round(value, 2)
                    matrix[j][i] = round(value, 2)

            results_list = solving_problem(matrix, n, current_k)
            average_time_greedy += results_list[0]
            average_time_branch += results_list[1]
            average_time_brute += results_list[2]
            average_time_comi += results_list[3]
            
            counter += 1
        
        average_time_greedy_list.append(average_time_greedy / J)
        average_time_branch_list.append(average_time_branch / J)
        average_time_brute_list.append(average_time_brute / J)
        average_time_comi_list.append(average_time_comi / J)

        print(f"Processed for n: {n}, k: {current_k}")

        r+=1

    plt.plot(dimensions, average_time_greedy_list, marker='o', label='Greedy')
    plt.plot(dimensions, average_time_branch_list, marker='o', label='Branch and Bounds')
    plt.plot(dimensions, average_time_brute_list, marker='o', label='Bruteforce')
    plt.plot(dimensions, average_time_comi_list, marker='o', label='COMI')
    plt.xlabel('Dimension of the Problem')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Execution Time vs. Problem Final Objects Number')
    plt.legend()
    plt.grid(True)
    plt.show()

        
    return []

def dimention_to_efficiency_experiment():
    print("Input data for your experiment: ")
    return []

def dimention_to_efficiency_experiment():
    print("Input data for your experiment: ")
    return []

def dimention_to_efficiency_experiment():
    print("Input data for your experiment: ")
    return []


def solving_problem(C, n, k):
    #Greedy -------------------------------------------
    start_time_greedy = time.time()

    greedy_selection(C, n, k)

    end_time_greedy = time.time()
    elapsed_time_greedy = end_time_greedy - start_time_greedy

    #Branch and Bounds -------------------------------------------
    start_time_branch = time.time()

    branch_and_bounds(C, n, k)

    end_time_branch = time.time()
    elapsed_time_branch = end_time_branch - start_time_branch

    #Bruteforce -------------------------------------------
    start_time_brute = time.time()

    brute_force(C, n, k)

    end_time_brute = time.time()
    elapsed_time_brute = end_time_brute - start_time_brute

    #COMI -------------------------------------------
    start_time_comi = time.time()

    comi(C, n, k)

    end_time_comi = time.time()
    elapsed_time_comi = end_time_comi - start_time_comi

    return [elapsed_time_greedy, elapsed_time_branch, elapsed_time_brute, elapsed_time_comi]