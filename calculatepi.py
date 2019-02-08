"""
calculatepi.py
Author: Sean Healey
Credit: Tutorials
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""

import math

# Prompt user for number of terms to use and number of decimals to display
num_terms = int(input('I will estimate pi. How many terms should I use? '))
decimals = int(input('How many decimal places should I use in the result? '))

# Create list with desired number of terms to calculate pi
terms_list = [((-1)**(x))/(2*x+1) for x in range(0,num_terms)]

# Calculate pi to desired number of decimal places
approx_pi = round(4*sum(terms_list),decimals)

# Print output
print('The approximate value of pi is ' + str(approx_pi))