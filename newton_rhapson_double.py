from numpy import Infinity, sin, cos, tan, exp, cosh, sinh, tanh
from prettytable import PrettyTable
from sympy import symbols, diff

x, y = symbols('x y', real=True)

function_1 = input("Enter 1st function: ")
function_2 = input("Enter 2nd function: ")
initial_approx = input("Enter initial approximation: ").split(",")

tolerance = int(input("Enter tolerance: "))
ule = 1/2 * 10**(-tolerance)

def func_value(x, y, func) -> float:
    return round(eval(func), tolerance + 1)

def derv_func_x(func):
    return diff(eval(func), x)

def derv_func_y(func):
    return diff(eval(func), y)

table = PrettyTable()
table.field_names = ["x", "y", "f", "g", "a = f'x", "b = f'y", "c = g'x", "d = g'y", "D = ad - bc", "D1 = -fd + gb", "D2 = -ga + fc", "h = D1/D", "k = D2/D"]

x_n = float(initial_approx[0])
y_n = float(initial_approx[1])

f = Infinity
g = Infinity
    
while abs(f) >= ule and abs(g) >= ule:
    f = round(func_value(x_n, y_n, function_1), tolerance + 1)
    g = round(func_value(x_n, y_n, function_2), tolerance + 1)
    f_derv_x = round(func_value(x_n, y_n, str(derv_func_x(function_1))), tolerance + 1)
    f_derv_y = round(func_value(x_n, y_n, str(derv_func_y(function_1))), tolerance + 1)
    g_derv_x = round(func_value(x_n, y_n, str(derv_func_x(function_2))), tolerance + 1)
    g_derv_y = round(func_value(x_n, y_n, str(derv_func_y(function_2))), tolerance + 1)
    d = round((f_derv_x * g_derv_y) - (f_derv_y * g_derv_x), tolerance + 1)
    d1= round((g * f_derv_y) - (f * g_derv_y), tolerance + 1)
    d2 = round((f * g_derv_x) - (g * f_derv_x), tolerance + 1)
    h = round(d1 / d, tolerance + 1)
    k = round(d2 / d, tolerance + 1)
    table.add_row([x_n, y_n, f, g, f_derv_x, f_derv_y, g_derv_x, g_derv_y, d, d1, d2, h, k])
    x_n = round(x_n + h, tolerance + 1)
    y_n = round(y_n + k, tolerance + 1)
    
print(table)
print(f"The solution of given set of equation is: x = {x_n:.4f}, y = {y_n:.4f}")



