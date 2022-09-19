from numpy import Infinity, sin, cos, tan, exp, cosh, sinh, tanh
from prettytable import PrettyTable
from sympy import diff, symbols

x = symbols('x', real=True)

function = input("Enter your function: ")
initial_approx = float(input("Enter initial approximation: "))

tolerance = int(input("Enter tolerance: "))
ule = 1/2 * 10**(-tolerance)

def func_value(x, func) -> float:
    return eval(func)

def derv_func(func):
    return diff(eval(func), x)

table = PrettyTable()
table.field_names = ["a", "x", "f(x)"]

x_func_value = Infinity

while abs(x_func_value) >= ule:
    x_n = round(initial_approx - (func_value(initial_approx, function) / func_value(initial_approx, str(derv_func(function)))), tolerance + 1)
    x_func_value = round(func_value(x_n, function), tolerance + 1) 
    table.add_row([initial_approx, x_n, x_func_value])
    initial_approx = x_n
    
print(table)
print(f"The solution of given function is: {x_n:.4f}")



