#!/usr/bin/env python3

#given 2 data sets, x and y, of n number of space-separated real numbers, calculate the value of the Pearson correlation coefficient.

n = int(input())

x = list(map(float, input().split()))
y = list(map(float, input().split()))

mean_x = sum(x)/n
mean_y = sum(y)/n

stdev_x = (sum([(i - mean_x)**2 for i in x])/n)**0.5
stdev_y = (sum([(i - mean_y)**2 for i in y])/n)**0.5

covariance = sum([(x[i]-mean_x)*(y[i]-mean_y) for i in range(n)])

corr_coefficient = covariance / (n * stdev_x * stdev_y)

print(round(corr_coefficient,3))
