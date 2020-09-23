# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:17:48 2018

@author:
"""


def creditBalance(balance, annualInterestRate, monthlyPayment):
    """
    balance is: float
    annualInterestRate is: float
    monthlyPayment is: float
    returns: float, rounded to 2 decimal places

    Returns the credit card balance after one year if a person only pays the
    minimum monthly payment required by the credit card company each month."""

    # this variable will iterate through 12 months of the year
    month = 0

    while month < 12:
        unpaid_balance = balance - monthlyPayment

        # The bank charges interest each month on unpaid balance
        balance = unpaid_balance + (annualInterestRate/12.0) * unpaid_balance
        month += 1

    # Don't forget to round answer to two decimal places
    balance = round(balance, 2)

    return balance


# Bisection search to find the minimum monthly payment that pays off balance
left = 0
right = balance
result = (left + right) / 2
epsilon = 10

while abs(creditBalance(balance, annualInterestRate, result)) >= epsilon:
    attempt = creditBalance(balance, annualInterestRate, result)
    if attempt == 0:
        break
    if attempt > 0:
        left = result
    else:
        right = result
    result = (left + right) / 2

# This line of code rounds the result to a multiple of 10
result = (result + 9) // 10 * 10


print("Lowest payment: " + str(result))
