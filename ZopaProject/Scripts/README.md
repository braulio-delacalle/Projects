### Scripts foulder ###
This foulder contains 2 files: 
    
1. callFunc.py: file to call the function in the terminal. Below we will explain the way to use it.
2. Zopa.py: file created for testing purposes.
    
To be able to run the LoanCalculator function in the terminal we will call the callFunc.py file. 
The function takes 2 arguments:

1. money_asked: the amount requested by the borrower, which has to be between 1000 and 15000 in increments of 100.
2. refill: this argument is used to refill the dataset with 100 new random values. This argument will take the strings "True"      if you want to refill or "False" if you do not want to refill.
    
To call the function in the terminal you wil have to be in the file where this script is. Next, enter: Python Zopa.py (money_asked) ('True'/ 'False'). Press enter to run.

Input example: 
                
                Python Zopa.py 1000 'True'

Output example: 
                
                Requested amount: 1000
                Rate: 5.0%
                Monthly repayment: 29.17
                Total repayment: 1050.0
                Bucket filled