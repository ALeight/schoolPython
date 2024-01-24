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


mylist = [1, 3, 5, 2, 2, 6, 7, 8, 5, 5, 5, 8]


# Computing a function which returns number of elements larger than both its predecessor and its successor
# Finish the implementation of the function
def counter(someList):
    count = 0
    if len(someList) < 3:
        return 0
    # for x in SomeList[2:] --> [2:], the colon implies it copies the list
    for x in range(len(someList[2:])):  # numbers before and after colon implies where list is sliced
        if (someList[x - 1] < someList[x]) and (someList[x] > someList[x + 1]):
            count += 1
        if someList[x] == -1:
            break
    return count


counter(mylist)