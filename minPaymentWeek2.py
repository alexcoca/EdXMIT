# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:25:14 2017

@author: alexc
"""

def minPayment():
    pass

month=1
def balanceCalc(balance,annualInterestRate,monthlyPaymentRate,month):
    if month == 12:
        return round(balance - monthlyPaymentRate*balance + (annualInterestRate/12)*(balance-monthlyPaymentRate*balance),2)
    else:
        month +=1
        return balanceCalc(round(balance-monthlyPaymentRate*balance+(annualInterestRate/12)*(balance-monthlyPaymentRate*balance),2),annualInterestRate,monthlyPaymentRate,month)

print("Remaining balance:"+" "+str(balanceCalc(balance,annualInterestRate,monthlyPaymentRate,month)))