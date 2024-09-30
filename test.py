from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(solve([x + y - 2*z, y + 4*z], [x, y], dict=True))