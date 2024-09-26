import math

# Constants
constants = {
    'pi': math.pi,
    'e': math.e,
    'golden_ratio': (1 + math.sqrt(5)) / 2
}

# Custom functions
def root(x, n):
    return x ** (1/n)

# Custom eval function
def custom_eval(expression):
    # Replace ^ with ** for exponentiation
    expression = expression.replace('^', '**')
    # Replace constants with their values
    for const, value in constants.items():
        expression = expression.replace(const, str(value))
    # Add the functions you want to allow from the math module and custom ones
    allowed_names = {
        **{k: v for k, v in math.__dict__.items() if not k.startswith("__")},
        'root': root
    }
    # Safely evaluate the expression
    try:
        return eval(expression, {"__builtins__": None}, allowed_names)
    except Exception as e:
        return f"Error in expression: {str(e)}"

if 1 == 1:
    # Example usage 
    inputt = input("Expression: ")
    result = custom_eval(inputt)
    print(f"The result of the expression '{inputt}' is: {result}")
