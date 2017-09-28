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
#A better upper bound is 1/12 of the sum we would have had to pay had we decided to pay all the debt at the end of the year
#The accrued debt at the end of the year would have been balance*(1+annualInterestRate)^12
upper_bound = balance
# A better bound is possible: balance/12
lower_bound = 0
last_guess = guess
tol = 0.1


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