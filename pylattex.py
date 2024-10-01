import sympy as sp
import numpy as np

# Get user input as a string
user_input = input("Enter a function of x (e.g., x**2 + sin(x)): ")
user_range = input("Enter a range for x, seperated by commas: ").split(",")
user_point = input("Enter a x-value: ")
# Define symbols for x and y
x = sp.symbols('x')
# Convert user input to a SymPy expression
expr = sp.sympify(user_input)
# Convert the SymPy expression to a numerical function
f_numeric = sp.lambdify((x), expr, 'numpy')
#Differentiate expressions
diffexpr = sp.diff(expr, x, 1)
doubdiffexpr = sp.diff(expr, x, 2)

