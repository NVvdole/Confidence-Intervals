# File Name: OneMeanZInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("One Mean Z-Interval")
print("")
print("\u03C3x = population std dev")
print("x- = sample mean")
print("nx = sample size")
print("")

sig = float(input("Enter \u03C3x: "))
while sig <= 0.0:
    sig = float(input("Enter \u03C3x: "))
    
mean = float(input("Enter x-: "))
    
n = int(input("Enter nx: "))
while n <= 0:
    n = int(input("Enter nx: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

std_err = sig / math.sqrt(n)

Z1 = norm.ppf((1.0 + CL) / 2.0)
lower1 = mean - (Z1 * std_err)
upper1 = mean + (Z1 * std_err)

Z2 = norm.ppf(CL)
lower2 = mean - (Z2 * std_err)
upper2 = mean + (Z2 * std_err)

print("Two-Sided Interval")
print(str(lower1) + " < \u03BCx < " + str(upper1))
print("")

print("Left-Sided Interval")
print(str(lower2) + " < \u03BCx < inf")
print("")

print("Right-Sided Interval")
print("-inf < \u03BCx < " + str(upper2))
