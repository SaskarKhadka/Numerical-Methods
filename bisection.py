from numpy import sin, cos, tan, exp, cosh, sinh, tanh
from prettytable import PrettyTable

function = input("Enter your function: ")

def func_value(x) -> float:
    return eval(function);
    
while True:
    initial_approx_1 = float(input("Enter 1st initial approximation: "))
    initial_approx_2 = float(input("Enter 2nd initial approximation: "))
    if(func_value(initial_approx_1) * func_value(initial_approx_2) < 1):
        break

tolerance = int(input("Enter tolerance: "))
ule = 1/2 * 10**(-tolerance)

midpoint = round((initial_approx_1 + initial_approx_2) / 2, tolerance + 1)

midpoint_func_value = round(func_value(midpoint), tolerance + 1)

table = PrettyTable()

table.field_names = ["a", "b", "x", "f(x)"]
table.add_row([initial_approx_1, initial_approx_2, midpoint, midpoint_func_value])


while abs(midpoint_func_value) >= ule:
    if(midpoint_func_value * func_value(initial_approx_1) < 0): initial_approx_2 = midpoint
    else: initial_approx_1 = midpoint
    midpoint = round((initial_approx_1 + initial_approx_2) / 2, tolerance + 1)
    midpoint_func_value = round(func_value(midpoint), 5)
    table.add_row([initial_approx_1, initial_approx_2, midpoint, midpoint_func_value])
    
print(table)
print(f"The solution of given function is: {midpoint:.4f}")



