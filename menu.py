from branchandbounds import branch_and_bounds
from bruteforce import brute_force
from greedy import greedy_selection
from custom_input import user_input
from comi import comi
import custom_output as out
import experiments as exper

def menu():
    while True:
        print("--------------------------------------------")
        print("Menu:")
        print("1. Solve problem")
        print("2. Start experiment")
        print("3. Exit")
        print("--------------------------------------------")
        choice = input("Enter your choice (1-3): ")
        print("\n")
        
        if choice == '1':
            solve_problem()
             
        elif choice == '2':
            choose_experiment()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

def solve_problem():
    print("--------------------------------------------")
    print("Choose an algorithm:")
    print("1. Greedy Algorithm")
    print("2. Branch and Bounds Algorithm")
    print("3. Brute Force Algorithm")
    print("4. Cutting Out the Most Incompatible Algorithm")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-4): ")

    data = user_input()
    
    if choice == '1':
        out.write_file(out.print_results(greedy_selection(data[0], data[1], data[2]), data[0]), data[0], "Greedy")
    elif choice == '2':
        out.write_file(out.print_results(branch_and_bounds(data[0], data[1], data[2]), data[0]), data[0], "Branch and Bounds")
    elif choice == '3':
        out.write_file(out.print_results(brute_force(data[0], data[1], data[2]), data[0]), data[0], "Bruteforce")
    elif choice == '4':
        out.write_file(out.print_results(comi(data[0], data[1], data[2]), data[0]), data[0], "COMI")
    else:
        print("Invalid choice!")

def choose_experiment(): 
    print("--------------------------------------------")
    print("Choose an experiment:")
    print("1. The effect of the problem`s dimension on the algorithm's running time")
    print("2. The effect of the number of final values on the algorithm's running time")
    print("3. The effect of the parameters of the problem on the accuracy of algorithms")
    print("4. The effect of the problem`s dimension on the accuracy of algorithms")
    print("5. The effect of the number of final values on the accuracy of algorithms")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        exper.dimention_to_time_experiment()
    elif choice == '2':
        exper.finalvalues_to_time_experiment()
    elif choice == '3':
        print("experiment 3")
    elif choice == '4':
        print("experiment 4")
    elif choice == '5':
        print("experiment 5")
    else:
        print("Invalid choice!")

def main():
    try:
        menu()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
