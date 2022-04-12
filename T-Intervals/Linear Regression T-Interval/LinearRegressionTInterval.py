# File Name: LinearRegressionTInterval.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t
import math
import statistics

print("Linear Regression T-Interval")
print("")
print("n = sample size")
print("x = predictor data")
print("y = response data")
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

meanx = statistics.mean(x)
std_devx = math.sqrt(statistics.variance(x))
meany = statistics.mean(y)
std_devy = math.sqrt(statistics.variance(y))

cov = 0
for i in range(n):
    cov += (x[i] - meanx) * (y[i] - meany)
cov /= (n - 1)
r = cov / (std_devx * std_devy)

b1 = r * (std_devy / std_devx)
b0 = meany - (b1 * meanx)

yhat = []
for i in range(n):
    temp = b0 + (b1 * x[i])
    yhat.append(temp)
    
std_err_top = 0
for i in range(n):
    std_err_top += pow(y[i] - yhat[i], 2)
std_err_top /= (n - 2)
std_err_top = math.sqrt(std_err_top)

std_err_bottom = 0
for i in range(n):
    std_err_bottom += pow(x[i] - meanx, 2)
std_err_bottom = math.sqrt(std_err_bottom)

x_sqd = 0
for i in range(n):
    x_sqd += pow(x[i], 2)

df = n - 2
std_err1 = std_err_top / std_err_bottom
std_err0 = std_err1 * math.sqrt(x_sqd / n)

T1 = t.ppf((1.0 + CL) / 2.0, df)
lower11 = b1 - (T1 * std_err1)
upper11 = b1 + (T1 * std_err1)
lower01 = b0 - (T1 * std_err0)
upper01 = b0 + (T1 * std_err0)

T2 = t.ppf(CL, df)
lower12 = b1 - (T2 * std_err1)
upper12 = b1 + (T2 * std_err1)
lower02 = b0 - (T2 * std_err0)
upper02 = b0 + (T2 * std_err0)
        
print("Linear Regression")
print("y = b0 + b1x")
print("b0 = " + str(b0))
print("b1 = " + str(b1))
print("r = " + str(r))
print("r^2 = " + str(pow(r, 2)))
print("")

print("Degrees of Freedom")
print("df = " + str(df))
print("")

print("Two-Sided Intervals")
print(str(lower11) + " <= \u03B21 <= " + str(upper11))
print(str(lower01) + " <= \u03B20 <= " + str(upper01))
print("")

print("Left-Sided Intervals")
print("\u03B21 >= " + str(lower12))
print("\u03B20 >= " + str(lower02))
print("")

print("Right-Sided Intervals")
print("\u03B21 <= " + str(upper12))
print("\u03B20 <= " + str(upper02))
