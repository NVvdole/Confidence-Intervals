# File Name: CorrelationZInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import norm
import math

print("Correlation Z-Interval")
print("")
print("n = sample size")
print("r = sample correlation coefficient")
print("")

n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))
    
r = float(input("Enter r: "))
while r <= -1.0 or r >= 1.0:
    r = float(input("Enter r: "))
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

meanv = 0.5 * math.log((1.0 + r) / (1.0 - r))
std_errv = math.sqrt(1.0 / (n - 3))

Z1 = norm.ppf((1.0 + CL) / 2.0)
pow_lower1 = meanv - (Z1 * std_errv)
pow_upper1 = meanv + (Z1 * std_errv)
lower_top1 = math.exp(2.0 * pow_lower1) - 1.0
lower_bottom1 = math.exp(2.0 * pow_lower1) + 1.0
lower1 = lower_top1 / lower_bottom1
upper_top1 = math.exp(2.0 * pow_upper1) - 1.0
upper_bottom1 = math.exp(2.0 * pow_upper1) + 1.0
upper1 = upper_top1 / upper_bottom1

Z2 = norm.ppf(CL)
pow_lower2 = meanv - (Z2 * std_errv)
lower_top2 = math.exp(2.0 * pow_lower2) - 1.0
lower_bottom2 = math.exp(2.0 * pow_lower2) + 1.0
lower2 = lower_top2 / lower_bottom2

pow_upper2 = meanv + (Z2 * std_errv)
upper_top2 = math.exp(2.0 * pow_upper2) - 1.0
upper_bottom2 = math.exp(2.0 * pow_upper2) + 1.0
upper2 = upper_top2 / upper_bottom2

print("Two-Sided Interval")
print(str(lower1) + " < \u03C1 < " + str(upper1))
print("")

print("Left-Sided Interval")
print(str(lower2) + " < \u03C1 < 1.0")
print("")

print("Right-Sided Interval")
print("-1.0 < \u03C1 < " + str(upper2))
