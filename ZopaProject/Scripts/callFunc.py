import argparse

import os
import sys

sys.path.append('..')

import pandas as pd
from ToolsLoanCalculator import LoanCalculator
import numpy as np

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('money_asked',
                       type=int)
my_parser.add_argument('refill')
# Execute the parse_args() method
args = my_parser.parse_args()

input_money = args.money_asked
input_refill = args.refill
LoanCalculator.loan_rate(input_money, input_refill)
