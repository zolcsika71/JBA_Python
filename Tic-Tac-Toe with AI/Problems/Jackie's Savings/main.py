def final_deposit_amount(*interest, amount=1000):
    for month in interest:
        print(month)
        amount += amount / 100 * month

    return round(amount, 2)


print(final_deposit_amount(5, 7, 4))
