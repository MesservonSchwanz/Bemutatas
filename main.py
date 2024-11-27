# main.py
from bemutatando_module_ss import create_gui
from tanult_module_ss import input_handler_ss
from sajat_module_ss import log_event_ss
import sys  # Needed to exit the program

def main():
    print("Welcome to the application!")

    # Loop for input validation
    while True:
        print("\nEnter a number between 1 and 5 to start the program.")
        print("Enter 6 to exit.")
        user_input = input_handler_ss('num')

        if user_input == 6:
            log_event_ss("Program exited by user.")
            print("Exiting the program...")
            sys.exit()  # Exit the program
        elif 1 <= user_input <= 5:
            log_event_ss(f"Program started with option {user_input}.")
            print(f"Starting the program with option {user_input}...")
            create_gui()  # Start the graphical interface
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()