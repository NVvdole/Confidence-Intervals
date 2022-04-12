# File Name: PairedMeanTInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math
import statistics

print("Paired Mean T-Interval")
print("")
print("n = sample size")
print("x = first sample")
print("y = second sample")
print("")

n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))
    
x = []
for i in range(n):
    temp = float(input("Enter x" + str(i + 1) + ": "))
    while temp <= 0.0:
        temp = float(input("Enter x" + str(i + 1) + ": "))
    x.append(temp)
    
y = []
for i in range(n):
    temp = float(input("Enter y" + str(i + 1) + ": "))
    while temp <= 0.0:
        temp = float(input("Enter y" + str(i + 1) + ": "))
    y.append(temp)
    
CL = float(input("Enter CL: "))
while CL <= 0.0 or CL >= 1.0:
    CL = float(input("Enter CL: "))
print("")

d = []
for i in range(n):
    temp = x[i] - y[i]
    d.append(temp)
meand = statistics.mean(d)
std_devd = math.sqrt(statistics.variance(d))

df = n - 1
std_err = std_devd / math.sqrt(n)

T1 = t.ppf((1.0 + CL) / 2.0, df)
lower1 = meand - (T1 * std_err)
upper1 = meand + (T1 * std_err)

T2 = t.ppf(CL, df)
lower2 = meand - (T2 * std_err)
upper2 = meand + (T2 * std_err)
    
print("d = x - y")
print("d = " + str(d))
print("d- = " + str(meand))
print("sd = " + str(std_devd))
print("")

print("Degrees of Freedom")
print("df = " + str(df))
print("")

print("Two-Sided Interval")
print(str(lower1) + " < \u03BCd < " + str(upper1))
print("")

print("Left-Sided Interval")
print(str(lower2) + " < \u03BCd < inf")
print("")

print("Right-Sided Interval")
print("-inf < \u03BCd < " + str(upper2))
