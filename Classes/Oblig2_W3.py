import sympy as sp
from math import sqrt, pow, cos, sin
from sympy.vector import Vector


# calculating sine of angle pi/10
a = sp.sin(sp.pi / 10)
print(a)
# calculating cos of pi/8
b = sp.cos(sp.pi / 8)
print(b)

# Quadratic formula
a = sp.S(1)  # ensures 1 is treated as a sympy symbol
b = sp.S(-2)  # sympy is for symbolic mathematics
c = sp.S(-3)

answer1 = (-b - sp.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
answer2 = (-b + sp.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(answer1, answer2)

# using sympy to solve the equation
x = sp.symbols("x")  # will print 'x' in console
print(sp.solve(x ** 2 - 2 * x - 3, x))


# functions for calculating vectors

# scalar product of u and v
def dot(u, v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    return x + y


def dot3(u, v, z):
    x = u[0] * v[0] * z[0]
    y = u[1] * v[1] * z[1]
    z = u[2] * v[2] * z[2]
    return x + y + z


# length of u
def absv(u):
    x = sp.S(sp.sqrt(u[0]**2 + u[1]**2))
    return x


# unit vector in the direction of u, normalized = unit vector
def normalise(u, length):
    x = u[0]/length
    y = u[1]/length
    return [x, y]


vector_u = [sp.sqrt(2)/2, 2]
vector_v = [3, sp.sqrt(5)]
v_u = [sp.S(vector_u)]  # sp.S - force numbers to be symbols
v_v = [sp.S(vector_v)]
print(dot(vector_u, vector_v))


# Length of vector
a = absv(vector_u)
print(a)

b = absv(vector_v)
print(b)


#  unit vector IN direction of U
print(normalise(vector_u, absv(vector_u)))










