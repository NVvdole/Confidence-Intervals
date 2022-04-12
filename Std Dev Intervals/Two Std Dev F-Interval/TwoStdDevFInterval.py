# File Name: TwoStdDevFInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import f
import math

print("Two Standard Deviation F-Interval")
print("")
print("sx = first sample std dev")
print("nx = first sample size")
print("sy = second sample std dev")
print("ny = second sample size")
print("")

std_dev1 = float(input("Enter sx: "))
while std_dev1 <= 0.0:
    std_dev1 = float(input("Enter sx: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
std_dev2 = float(input("Enter sy: "))
while std_dev2 <= 0.0:
    std_dev2 = float(input("Enter sy: "))
    
n2 = int(input("Enter ny: "))
while n2 <= 0:
    n2 = int(input("Enter ny: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

df1 = n1 - 1
df2 = n2 - 1

F_lower1 = f.ppf((1.0 + CL) / 2.0, df1, df2)
F_upper1 = f.ppf(1.0 - ((1.0 + CL) / 2.0), df1, df2)
lower1 = math.sqrt((pow(std_dev1, 2) / pow(std_dev2, 2)) / F_lower1)
upper1 = math.sqrt((pow(std_dev1, 2) / pow(std_dev2, 2)) / F_upper1)

F_lower2 = f.ppf(CL, df1, df2)
lower2 = math.sqrt((pow(std_dev1, 2) / pow(std_dev2, 2)) / F_lower2)

F_upper2 = f.ppf(1.0 - CL, df1, df2)
upper2 = math.sqrt((pow(std_dev1, 2) / pow(std_dev2, 2)) / F_upper2)

print("Degrees of Freedom")
print("df1 = " + str(df1))
print("df2 = " + str(df2))
print("")

print("Two-Sided Intervals")
print(str(lower1) + " < \u03C3x / \u03C3y < " + str(upper1))
print(str(pow(lower1, 2)) + " < \u03C3x^2 / \u03C3y^2 < " + str(pow(upper1, 2)))
print("")

print("Left-Sided Intervals")
print(str(lower2) + " < \u03C3x / \u03C3y < inf")
print(str(pow(lower2, 2)) + " < \u03C3x^2 / \u03C3y^2 < inf")
print("")

print("Right-Sided Intervals")
print("0.0 < \u03C3x / \u03C3y < " + str(upper2))
print("0.0 < \u03C3x^2 / \u03C3y^2 < " + str(pow(upper2, 2)))

