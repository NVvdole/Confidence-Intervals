# File Name: TwoMeanTInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math

print("Two Mean T-Interval (Unpooled Variance)")
print("")
print("x- = first sample mean")
print("sx = first sample std dev")
print("nx = first sample size")
print("y- = second sample mean")
print("sy = second sample std dev")
print("ny = second sample size")
print("")

mean1 = float(input("Enter x-: "))

std_dev1 = float(input("Enter sx: "))
while std_dev1 <= 0.0:
    std_dev1 = float(input("Enter sx: "))
    
n1 = int(input("Enter nx: "))
while n1 <= 0:
    n1 = int(input("Enter nx: "))
    
mean2 = float(input("Enter y-: "))

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

df_top = pow((pow(std_dev1, 2) / n1) + (pow(std_dev2, 2) / n2), 2)
df_bottom = (pow(pow(std_dev1, 2)/ n1, 2) / (n1 - 1)) + (pow(pow(std_dev2, 2)/ n2, 2) / (n2 - 1))
df = df_top / df_bottom
std_err = math.sqrt((pow(std_dev1, 2) / n1) + (pow(std_dev2, 2) / n2))

T1 = t.ppf((1.0 + CL) / 2.0, df)
lower1 = (mean1 - mean2) - (T1 * std_err)
upper1 = (mean1 - mean2) + (T1 * std_err)

T2 = t.ppf(CL, df)
lower2 = (mean1 - mean2) - (T2 * std_err)
upper2 = (mean1 - mean2) + (T2 * std_err)

print("Degrees of Freedom")
print("df = " + str(df))
print("")

print("Two-Sided Interval")
print(str(lower1) + " <= \u03BCx - \u03BCy <= " + str(upper1))
print("")

print("Left-Sided Interval")
print("\u03BCx - \u03BCy >= " + str(lower2))
print("")

print("Right-Sided Interval")
print("\u03BCx - \u03BCy <= " + str(upper2))
