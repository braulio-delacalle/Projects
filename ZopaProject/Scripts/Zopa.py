def loan_rate(n, refill):

    zopa_data = pd.read_csv("../Data/ZopaData.csv")

    zopa_data = zopa_data.drop(columns = "Unnamed: 0")
    zopa_data = zopa_data.sort_values(by = "Rate", ascending = True)
    zopa_data = zopa_data.reset_index()
    zopa_data = zopa_data.drop("index", axis = 1)

    amount_asked = n
    rate_final = 0
    amount_lent = 0
    amount_left_to_give = amount_asked
    index_ = 0
    amount_remaining = 0


    if n > 15000 or n < 1000:
        return "Please enter a valid amount."
    if n > sum(zopa_data["Available"]):
        return "We are not able to provide that amount."
    if n % 100 != 0:
        return "Please enter a valid amount."

    for rate, available in zip(zopa_data["Rate"], zopa_data["Available"]):

        if amount_left_to_give == 0:

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

        elif amount_left_to_give < int(available):
            rate_final += (float(rate) * (int(amount_left_to_give)/ amount_asked))
            amount_remaining = int(available) - amount_left_to_give
            amount_lent += amount_left_to_give
            amount_left_to_give -= amount_left_to_give
            index_ += 1

        elif amount_left_to_give > int(available):
            rate_final += (float(rate) * (int(available)/ amount_asked))
            amount_lent += int(available)
            amount_left_to_give -= int(available)
            index_ += 1

    index_ = index_ - 1
    zopa_data_new = zopa_data[index_:]
    zopa_data_new["Available"][1] = amount_remaining

    if refill == True:

        data_available = np.random.randint(100,1000,size=100)
        df_available = pd.DataFrame(data_available, columns=['Available'])

        data_rate = np.random.uniform(0.05, 0.2,size=100)
        df_rate = pd.DataFrame(data_rate, columns=['Rate'])
        df_rate = df_rate.round(decimals = 2)

        df = pd.concat([df_rate, df_available], axis=1)

        frames = [df, zopa_data_new]
        zopa_data_new = pd.concat(frames)

    zopa_data_new.to_csv("../Data/ZopaData.csv")

print(loan_rate(5000, True))
