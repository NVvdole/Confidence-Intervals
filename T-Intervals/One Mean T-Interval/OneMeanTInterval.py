# File Name: OneMeanTInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math

print("One Mean T-Interval")
print("")
print("x- = sample mean")
print("sx = sample std dev")
print("nx = sample size")
print("")

mean = float(input("Enter x-: "))

std_dev = float(input("Enter sx: "))
while std_dev <= 0.0:
    std_dev = float(input("Enter sx: "))
    
n = int(input("Enter nx: "))
while n <= 0:
    n = int(input("Enter nx: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

df = n - 1
std_err = std_dev / math.sqrt(n)

T1 = t.ppf((1.0 + CL) / 2.0, df)
lower1 = mean - (T1 * std_err)
upper1 = mean + (T1 * std_err)

T2 = t.ppf(CL, df)
lower2 = mean - (T2 * std_err)
upper2 = mean + (T2 * std_err)
    
print("Degrees of Freedom")
print("df = " + str(df))
print("")

print("Two-Sided Interval")
print(str(lower1) + " < \u03BCx < " + str(upper1))
print("")

print("Left-Sided Interval")
print(str(lower2) + " < \u03BCx < inf")
print("")

print("Right-Sided Interval")
print("-inf < \u03BCx < " + str(upper2))
