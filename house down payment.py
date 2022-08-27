good_credit = False
price = 1000000

if good_credit:
    down_payment = 0.1 * price
    print(f"you need to put {down_payment} as down payment ")
else:
    down_payment= 0.2 * price
    print(f"you need to put {down_payment} as down payment")
