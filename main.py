# main.py

def greet(name):
    """Function to greet a user."""
    return f"Hello, {name}!"


def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b


def main():
    """Main function to run the demo."""
    # Greet the user
    user_name = input("Enter your name: ")
    print(greet(user_name))

    # Add two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
