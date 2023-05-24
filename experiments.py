import random
from branchandbounds import branch_and_bounds
from bruteforce import brute_force
from greedy import greedy_selection
from comi import comi
import time
import matplotlib.pyplot as plt


def dimention_to_time_experiment():
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")
    n = int(input("Enter the start n: "))
    print("--------------------------------------------")

    N = int(input("Enter the final n: "))
    print("--------------------------------------------")

    if n > N:
            raise ValueError("Final n be more than to n.")

    deltan = int(input("Enter the delta_n: "))
    print("--------------------------------------------")

    if deltan >= (N-n):
            raise ValueError("Incorrect delta n")

    k = int(input("Enter the number of objects to find for the start n: "))
    print("--------------------------------------------")

    if k > n:
            raise ValueError("k must be less than or equal to n.")
    
    J = int(input("Enter the number of experiments for each n: "))
    print("--------------------------------------------")
    
    mu = float(input("Enter mu (average value for generation): "))
    print("--------------------------------------------")
    sigma = float(input("Enter sigma (dispersion for values): "))
    print("--------------------------------------------")

    dimensions = []
    average_time_greedy_list = []
    average_time_branch_list = []
    average_time_brute_list = []
    average_time_comi_list = []

    counter1 = 0
    counter2 = 0

    while n+(deltan*counter1) < N:
        r = n+deltan*counter1

        dimensions.append(r)
        
        average_time_greedy = 0
        average_time_branch = 0
        average_time_brute = 0
        average_time_comi = 0

        while counter2 < J:

            matrix = [[100] * r for _ in range(r)]

            for i in range(r):
                for j in range(i + 1, r):
                    value = random.normalvariate(mu, sigma)
                    
                    value = max(0, min(1, value))
                    matrix[i][j] = round(value, 2)
                    matrix[j][i] = round(value, 2)

            results_list = solving_problem(matrix, r, (k*(counter1+1)))
            average_time_greedy += results_list[0]
            average_time_branch += results_list[1]
            average_time_brute += results_list[2]
            average_time_comi += results_list[3]

            
            
            counter2 += 1
        
        average_time_greedy_list.append(average_time_greedy / J)
        average_time_branch_list.append(average_time_branch / J)
        average_time_brute_list.append(average_time_brute / J)
        average_time_comi_list.appemd(average_time_comi / J)

        print(f"Processed for n: {r}, k: {k*(counter1+1)}")

        counter1 += 1

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

def variation_to_efficiency_experiment():
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