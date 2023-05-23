from branchandbounds import branch_and_bounds
from bruteforce import brute_force
from greedy import greedy_selection
from custom_input import user_input
import custom_output as out

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
            start_experiment()
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
    print("4. Dynamic Programming (Cutting out the most incompatible)")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-4): ")

    data = user_input()
    
    if choice == '1':
        out.write_file(out.print_results(greedy_selection(data[0], data[1], data[2])), data[0])
    elif choice == '2':
        out.write_file(out.print_results(branch_and_bounds(data[0], data[1], data[2])), data[0])
    elif choice == '3':
        out.write_file(out.print_results(brute_force(data[0], data[1], data[2]))1, data[0])
    elif choice == '4':
        algorithm_d(data)
    else:
        print("Invalid choice!")

def algorithm_d(data):
    data = user_input()
    # Algorithm D implementation here
    print("Running Algorithm D with data:", data)

def start_experiment():
    # Implement experiment functionality
    print("Starting experiment...")
    # Add your experiment code here

def main():
    try:
        menu()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
