from numpy import sin, cos, tan, sinh, cosh, exp, log
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
table.field_names = ["x_n", "y_n", "k1", "k2", "y_n+1"]

while a < b:
    k1 = round(common_difference * func_value(a, y_a), 4)
    k2 = round(common_difference * func_value(a + common_difference, y_a + k1), 4)
    y_next = round(y_a + 0.5 * (k1 + k2), 4)
    table.add_row([a, y_a, k1, k2, y_next])
    a = a + common_difference
    y_a = y_next
    
print(table)
print(f"y({b}) = {y_next}")
     