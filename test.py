from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
print(solve(x**2-1, x))