import sys
sys.path.append('..')
import pandas as pd
import numpy as np

zopa_data = pd.read_csv("../Data/ZopaData.csv")
#zopa_data = zopa_data.drop(columns = "Unnamed: 0")
zopa_data = zopa_data.sort_values(by = "Rate", ascending = True)
zopa_data = zopa_data.reset_index()
zopa_data = zopa_data.drop("index", axis = 1)

def loan_rate(n, refill): # n = amount asked to be lent. refill = "True" if you want to refill the data the end of the function
   

    amount_asked = n
    rate_final = 0
    amount_lent = 0  # This variable will be growing with the money of each lender
    amount_left_to_lend = amount_asked # This variable wil be reducing after going through each lender
    index_ = 0  # This variable to know the last lender. 
    amount_remaining = 0  # This variable to know the money left of the last lender
    

    if n > 15000 or n < 1000:
        print ("Please enter an amount between 1000 and 15000.")
        return
    if n > sum(zopa_data["Available"]):
        print ("We are not able to provide that amount.")
        return
    if n % 100 != 0:
        print ("Please enter a valid amount.")
        return
     
   

    # In the following loop, rate_lender is the rate of each lender.
    # In the following loop, available_lender is the amount available of each lender.
    for rate_lender, available_lender in zip(zopa_data["Rate"], zopa_data["Available"]):
        if amount_left_to_lend == 0:
            print("""
                Requested amount: {reqamount}
                Rate: {rate_}%
                Monthly repayment: {monthly}
                Total repayment: {totalrep}""".format(
                    reqamount = amount_asked,
                    rate_ = round(rate_final * 100, ndigits = 1),
                    monthly =  round(amount_asked * ((1+rate_final)/36), ndigits = 2),
                    totalrep = round(amount_asked * (1+rate_final), ndigits = 2))
                    )
            break
                 

        elif amount_left_to_lend < int(available_lender):
            rate_final += (float(rate_lender) * (int(amount_left_to_lend)/ amount_asked))
            amount_remaining = int(available_lender) - amount_left_to_lend
            amount_lent += amount_left_to_lend
            amount_left_to_lend -= amount_left_to_lend
            index_ += 1

        elif amount_left_to_lend > int(available_lender):
            rate_final += (float(rate_lender) * (int(available_lender)/ amount_asked))
            amount_lent += int(available_lender)
            amount_left_to_lend -= int(available_lender)
            index_ += 1

    index_ = index_ - 1
    zopa_data_new = zopa_data[index_:].copy()
    zopa_data_new.loc[1,"Available"] = amount_remaining

    # if refill == "True", the data will be refilled with 100 random rows.
    if refill == 'True':

        data_available = np.random.randint(100,1000,size=100)
        df_available = pd.DataFrame(data_available, columns=['Available'])

        data_rate = np.random.uniform(0.05, 0.2,size=100)
        df_rate = pd.DataFrame(data_rate, columns=['Rate'])
        df_rate = df_rate.round(decimals = 2)

        df = pd.concat([df_rate, df_available], axis=1)

        frames = [df, zopa_data_new]
        zopa_data_new = pd.concat(frames)
        print('Bucket filled')

    zopa_data_new.to_csv("../Data/ZopaData.csv", index=False)
