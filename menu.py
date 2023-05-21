from branchandbounds import branch_and_bounds
from custom_input import user_input

def menu():
    while True:
        print("\nMenu:")
        print("1. Solve problem")
        print("2. Start experiment")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            solve_problem()
        elif choice == '2':
            start_experiment()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

def solve_problem():
    print("Choose an algorithm:")
    print("1. Greedy Algorithm")
    print("2. Branch and Bounds Algorithm")
    print("3. Brute Force Algorithm")
    print("4. Dynamic Programming (Cutting ut the most incompatible)")
    choice = input("Enter your choice (1-4): ")

    data = user_input()
    
    if choice == '1':
        algorithm_a(data)
    elif choice == '2':
        branch_and_bounds(C=data[2], n=data[1], k=data[0])
    elif choice == '3':
        algorithm_c(data)
    elif choice == '4':
        algorithm_d(data)
    else:
        print("Invalid choice!")

def algorithm_a(data):
    
    # Algorithm A implementation here
    print("Running Algorithm A with data:", data)



def algorithm_c(data):
    data = user_input()
    # Algorithm C implementation here
    print("Running Algorithm C with data:", data)

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
