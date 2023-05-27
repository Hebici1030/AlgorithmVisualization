# import sympy
# import sympy as sp
#
# # #定义函数f(x)
# x = sp.Symbol('x')
# f = sp.sqrt(x)
# #
# # #计算Ω
# # omega = sp.integrate(sp.sqrt(1+f.diff(x)**2), (x, 0, 1))
# # print("Ω = ", omega)
#
# print(sympy.O(f,(x,sympy.oo)))
# from sympy.functions.special.theta_functions import theta
# from sympy.functions.special.theta_functions import theta
# from sympy import exp, pi, I
#
# z = 1/2
# q = exp(I*pi/4)
#
# theta(z, q)
# python
# from sympy import Symbol, O
#
# # Define the variable and the function
# n = Symbol('n')
# f = 3*n**2 + 5*n + 7
#
# # Calculate the Theta of the function
# theta = f + O(n**2)
# print(f)
# # Print the result
# print(theta)
import sympy
from sympy import Symbol, Limit

# # Define the variable and the function
# n = Symbol('n')
# f = 3*n**2 + 5*n + 7
#
# # Calculate the lower bound of the function
# lower_bound = Limit(f/n**2, n, sympy.oo).doit()

# Print the result
# print(lower_bound)
# from sympy import Symbol
#
# x = Symbol('x')
# f = 1 + x + x**2
# g = 1 - x
# h = f / g
#
# num_order = f.asymptotic_order(x)
# denom_order = g.asymptotic_order(x)
# h_order = min(num_order, denom_order)
#
# print(h_order)
# from sympy import *
# x = symbols('x')
# expr = x**3 + x**2*log(x)
# # order = expr.asymptotic_order(x)
# expr.as_ordered_factors()

# import sympy
#
# x = sympy.Symbol('x')
# f = sympy.log(x,2) + 4
#
# # Divide f by x raised to the power of its degree
# g = f / x**sympy.degree(f)
#
# # Take the limit as x approaches infinity
# asymptotic_order = sympy.limit(g, x, sympy.oo)
#
# print(asymptotic_order)
import sympy

x = sympy.Symbol('x')
f = sympy.log(x,2) + 4
# g = x**2

asymptotic_order = sympy.O(f, x)
print(asymptotic_order)
