from numpy import sin, cos, tan, exp, cosh, sinh, tanh
from prettytable import PrettyTable
import decimal
decimal.getcontext().prec = 10

function = input("Enter your function: ")

def func_value(x) -> float:
    return float(eval(function));
    
while True:
    initial_approx_1 = float(input("Enter 1st initial approximation: "))
    initial_approx_2 = float(input("Enter 2nd initial approximation: "))
    if(func_value(initial_approx_1) * func_value(initial_approx_2) < 1):
        break

tolerance = int(input("Enter tolerance: "))
ule = 1/2 * 10**(-tolerance)

x = round((initial_approx_1 * func_value(initial_approx_2) - initial_approx_2 * func_value(initial_approx_1)) / (func_value(initial_approx_2) - func_value(initial_approx_1)), tolerance + 1)

x_func_value = round(func_value(x), tolerance + 1)

table = PrettyTable()

table.field_names = ["a", "b", "x", "f(x)"]
table.add_row([initial_approx_1, initial_approx_2, x, x_func_value])


while abs(x_func_value) >= ule:
    if(x_func_value * func_value(initial_approx_1) < 0): initial_approx_2 = x
    else: initial_approx_1 = x
    x = round((initial_approx_1 * func_value(initial_approx_2) - initial_approx_2 * func_value(initial_approx_1)) / (func_value(initial_approx_2) - func_value(initial_approx_1)), tolerance + 1)
    x_func_value = round(func_value(x), tolerance + 1) 
    table.add_row([initial_approx_1, initial_approx_2, x, x_func_value])
    
print(table)
print(f"The solution of given function is: {x:.4f}")



