# File Name: TwoMeanZInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("Two Mean Z-Interval")
print("")
print("\u03C3x = first population std dev")
print("\u03C3y = second population std dev")
print("x- = first sample mean")
print("nx = first sample size")
print("y- = second sample mean")
print("ny = second sample size")
print("")
    
sig1 = float(input("Enter \u03C3x: "))
while sig1 <= 0.0:
    sig1 = float(input("Enter \u03C3x: "))

sig2 = float(input("Enter \u03C3y: "))
while sig2 <= 0.0:
    sig2 = float(input("Enter \u03C3y: "))
    
mean1 = float(input("Enter x-: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
mean2 = float(input("Enter y-: "))
    
n2 = int(input("Enter ny: "))
while n2 <= 0:
    n2 = int(input("Enter ny: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

std_err = math.sqrt((pow(sig1, 2) / n1) + (pow(sig2, 2) / n2))

Z1 = norm.ppf((1.0 + CL) / 2.0)
lower1 = (mean1 - mean2) - (Z1 * std_err)
upper1 = (mean1 - mean2) + (Z1 * std_err)

Z2 = norm.ppf(CL)
lower2 = (mean1 - mean2) - (Z2 * std_err)
upper2 = (mean1 - mean2) + (Z2 * std_err)

print("Two-Sided Interval")
print(str(lower1) + " < \u03BCx - \u03BCy < " + str(upper1))
print("")

print("Left-Sided Interval")
print(str(lower2) + " < \u03BCx - \u03BCy < inf")
print("")

print("Right-Sided Interval")
print("-inf < \u03BCx - \u03BCy < " + str(upper2))
