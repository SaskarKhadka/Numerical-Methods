from numpy import sin, cos, tan, exp, cosh, sinh, tanh
from prettytable import PrettyTable

x_function = input("Enter x: ")
y_function = input("Enter y: ")
z_function = input("Enter z: ")
initial_approx = [0, 0, 0]

def func_value(x, y, z, func) -> float:
    return round(eval(func), 5);

tolerance = int(input("Enter tolerance: "))
ule = 1/2 * 10**(-tolerance)

def calc_vars(vars: list):
    x_value = func_value(vars[0], vars[1], vars[2], x_function)
    y_value = func_value(vars[0], vars[1], vars[2], y_function)
    z_value = func_value(vars[0], vars[1], vars[2], z_function)
    table.add_row([x_value, y_value, z_value])
    return [x_value, y_value, z_value]

table = PrettyTable()

table.field_names = ["x", "y", "z"]
table.add_row([initial_approx[0], initial_approx[1], initial_approx[2]])
vars = calc_vars([initial_approx[0], initial_approx[1], initial_approx[2]])

while initial_approx != vars:
    initial_approx = vars
    vars = calc_vars(initial_approx)
    
print(table)
print(f"The solution of given set of equations is: x = {vars[0]:.4f}, y = {vars[1]:.4f}, z = {vars[2]:.4f}")



