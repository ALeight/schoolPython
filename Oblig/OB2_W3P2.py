import sympy as sp
# from math import sqrt, pow, cos, sin
from sympy.vector import Vector


# scalar product of u and v
def dot(u, v):
    x = u[0] * v[0]
    y = u[1] * v[1]
    return x + y


# three coordinate scalar product
def dot3(u, v):
    x = u[0] * v[0] + u[1] * v[1]
    y = u[2] * v[2]
    return x + y


# calculates length of vector
def length(u):
    x = sp.S(sp.sqrt(u[0]**2 + u[1]**2 + u[2]**2))
    return x


def crossprod(u, v):
    x = u[1] * v[2] - u[2] * v[1]
    y = u[2] * v[0] - u[0] * v[2]
    z = u[0] * v[1] - u[1] * v[0]
    return [x, y, z]


# area of parallelogram
def areavec(u, v):
    x = u[1] * v[2] - v[1] * u[2]
    y = u[2] * v[0] - v[2] * u[0]
    z = u[0] * v[1] - v[0] * u[1]
    return sp.sqrt((x**2 + y**2 + z**2))


vec_u = (3, 1, -1)
vec_v = (3, -5, 5)


print(length(vec_v))
print(dot3(vec_u, vec_v))
print(crossprod(vec_u, vec_v))
print(crossprod(vec_v, vec_u))
print(areavec(vec_u, vec_v))

