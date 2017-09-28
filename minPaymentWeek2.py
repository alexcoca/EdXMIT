# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:25:14 2017

@author: alexc
"""

import pdb


month = 1
def balanceCalc(balance,annualInterestRate,monthlyPayment,month):
    if month == 12:
        return round(balance - monthlyPayment + (annualInterestRate/12)*(balance-monthlyPayment),2)
    else:
        month +=1
        return balanceCalc(round(balance-monthlyPayment+(annualInterestRate/12)*(balance-monthlyPayment),2),annualInterestRate,monthlyPayment,month)


guess = balance/2
upper_bound = balance
lower_bound = 0
last_guess = guess
tol = 1e-7

while (abs(balanceCalc(balance,annualInterestRate,guess,month))>tol):
    month = 1;
    if balanceCalc(balance,annualInterestRate,guess,month) > 0:
        lower_bound = last_guess
        guess = lower_bound + (upper_bound - lower_bound)/2
        last_guess = guess
    else:
        upper_bound = last_guess
        guess =upper_bound - (upper_bound - lower_bound)/2
        last_guess = guess
        
guess = int(round(guess,0))

while (guess%10 != 0):
    guess += 1

print("Lowest Payment:"+" "+str(guess))