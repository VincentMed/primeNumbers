# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:28:43 2022

@author: Vincent Medrano

Prime numbers between 1 and 1000 with total amount.
"""

start = 2
end = 1001
counter = 0

for x in range(start, end):
    isPrime = True
    for div in range(2, x):
        if x % div == 0:
            isPrime = False
            break
    if isPrime:
        counter += 1
        print(x, end = " ")

print(f"That is a total of {counter} prime numbers")
        
