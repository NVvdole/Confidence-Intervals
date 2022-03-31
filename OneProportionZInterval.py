# File Name: OneProportionZInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("One Proportion Z-Interval")
print("")
print("x = sample successes")
print("nx = sample size")
print("")

x = int(input("Enter x: "))
while x <= 0:
    x = int(input("Enter x: "))
    
n = int(input("Enter nx: "))
while n <= x:
    n = int(input("Enter nx: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

p = float(x) / n
std_err = math.sqrt((p * (1.0 - p)) / n)

Z1 = norm.ppf((1.0 + CL) / 2.0)
lower1 = p - (Z1 * std_err)
upper1 = p + (Z1 * std_err)
    
Z2 = norm.ppf(CL)
lower2 = p - (Z2 * std_err)
upper2 = p + (Z2 * std_err)

print("Proportion")
print("px^ = " + str(p))
print("")

print("Two-Sided Interval")
print(str(lower1) + " <= px <= " + str(upper1))
print("")

print("Left-Sided Interval")
print("px >= " + str(lower2))
print("")

print("Right-Sided Interval")
print("px <= " + str(upper2))
