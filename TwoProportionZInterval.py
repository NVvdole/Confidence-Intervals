# File Name: TwoProportionZInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("Two Proportion Z-Interval")
print("")
print("x = first sample successes")
print("nx = first sample size")
print("y = second sample successes")
print("ny = second sample size")
print("")

x = int(input("Enter x: "))
while x <= 0:
    x = int(input("Enter x: "))
    
n1 = int(input("Enter nx: "))
while n1 <= x:
    n1 = int(input("Enter nx: "))
    
y = int(input("Enter y: "))
while y <= 0:
    y = int(input("Enter y: "))
    
n2 = int(input("Enter ny: "))
while n2 <= y:
    n2 = int(input("Enter nx: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

p1 = float(x) / n1
p2 = float(y) / n2
std_err = math.sqrt(((p1 * (1.0 - p1)) / n1) + ((p2 * (1.0 - p2)) / n2))

Z1 = norm.ppf((1.0 + CL) / 2.0)
lower1 = (p1 - p2) - (Z1 * std_err)
upper1 = (p1 - p2) + (Z1 * std_err)

Z2 = norm.ppf(CL)
lower2 = (p1 - p2) - (Z2 * std_err)
upper2 = (p1 - p2) + (Z2 * std_err)

print("Proportions")    
print("px^ = " + str(p1))
print("py^ = " + str(p2))
print("")

print("Two-Sided Interval")
print(str(lower1) + " <= px - py <= " + str(upper1))
print("")

print("Left-Sided Interval")
print("px - py >= " + str(lower2))
print("")

print("Right-Sided Interval")
print("px - py <= " + str(upper2))
