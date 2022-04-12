# File Name: OneStdDevChiSquareInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi2
import math

print("One Standard Deviation Chi-Square Interval")
print("")
print("sx = sample std dev")
print("nx = sample size")
print("")

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

X2_lower1 = chi2.ppf((1.0 + CL) / 2.0, df)
X2_upper1 = chi2.ppf(1.0 - ((1.0 + CL) / 2.0), df)
lower1 = math.sqrt(((n - 1) * pow(std_dev, 2)) / X2_lower1)
upper1 = math.sqrt(((n - 1) * pow(std_dev, 2)) / X2_upper1)

X2_lower2 = chi2.ppf(CL, df)
lower2 = math.sqrt(((n - 1) * pow(std_dev, 2)) / X2_lower2)

X2_upper2 = chi2.ppf(1.0 - CL, df)
upper2 = math.sqrt(((n - 1) * pow(std_dev, 2)) / X2_upper2)

print("Degrees of Freedom")
print("df = " + str(df))
print("")

print("Two-Sided Intervals")
print(str(lower1) + " < \u03C3x < " + str(upper1))
print(str(pow(lower1, 2)) + " < \u03C3x^2 < " + str(pow(upper1, 2)))
print("")

print("Left-Sided Intervals")
print(str(lower2) + " < \u03C3x < inf")
print(str(pow(lower2, 2)) + " < \u03C3x^2 < inf")
print("")

print("Right-Sided Intervals")
print("0.0 < \u03C3x < " + str(upper2))
print("0.0 < \u03C3x^2 < " + str(pow(upper2, 2)))
