# tanult_module_ss.py

def input_handler_ss(input_type):
    """
    Data input handler function. Asks for a number or an operator depending on the type.
    """
    if input_type == 'num':
        text = input("\nEnter a number: ")
        while not text.isnumeric():
            print("Invalid number!")
            text = input("\nEnter a number: ")
        user_input = int(text)
    elif input_type == 'op':
        text = input("Enter an operation (+, -, *, /): ")
        while text not in ['+', '-', '*', '/']:
            print("Invalid operation!")
            text = input("Enter an operation (+, -, *, /): ")
        user_input = text
    else:
        user_input = None
    return user_input