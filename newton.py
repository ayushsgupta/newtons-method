import time
start_time = time.time()

from sympy import *
print "SYMPY IMPORT TIME: %s SEC" % (round(time.time() - start_time, 5))

# CONSTANTS
ACCURACY = 20

# GET INPUTS
str_f = raw_input("---------------\nf(x) = ")
x1 = input("x1 = ")

start_calc_time = time.time()

# DECLARE 'X' AS A VARIABLE
x = symbols("x")

# CONVERT F(X) INTO SYMBOLIC FUNCTION
f = sympify(str_f)
x1 = float(x1)

# CALCULATE DERIVATIVE OF F(X)
f_prime = diff(f, x)

# DISPLAY F(X) AND F'(X)
print "---------------\nf(x) =", f
print "f'(x) =", f_prime, "\n---------------"

def approximateZeros(xn, n):
    n -= 1
    if n > 1:
        new_xn = approximateZeros(xn, n)
        numerator = f.subs(x, new_xn).evalf()
        denominator = f_prime.subs(x, new_xn).evalf()
        xn1 = new_xn - (numerator / denominator)
        return xn1
    elif n is 1:
        return xn

print "ZERO:", approximateZeros(x1, ACCURACY)
print "CALCULATION TIME: %s SEC" % (round(time.time() - start_calc_time, 5))
