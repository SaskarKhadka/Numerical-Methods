from numpy import sin, cos, tan, sinh, cosh, exp, log, tanh
from prettytable import PrettyTable

function = input("Enter y derivative: ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
y_a = float(input(f"Enter y({a}): "))
total_intervals = int(input("Total intervals: "))
common_difference = (b - a) / total_intervals

def func_value(x, y):
    return round(eval(function), 4)

table = PrettyTable()
table.field_names = ["x_n", "y_n", "y_n+1_*", "y_n+1"]

while a < b:
    functional_value = func_value(a, y_a)
    y_next_0 = round(y_a + common_difference *  functional_value, 4)
    y_next = round(y_a + common_difference / 2 * (functional_value + func_value(a + common_difference, y_next_0)), 4)
    table.add_row([a, y_a, y_next_0, y_next])
    a = a + common_difference
    y_a = y_next
    
print(table)
print(f"y({b}) = {y_next}")
# print("y(" + b + ") = " + y_next)
     