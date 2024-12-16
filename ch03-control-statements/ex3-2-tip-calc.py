print('Welcome to the Tip Calculator')
meal_price = float(input('Enter cost of meal: '))
for i in range(15, 26, 5):
    tip_pct = i/100
    tip_amt = meal_price*tip_pct
    total_amt = meal_price + tip_amt
    print()
    print(f'{i}%')
    print(f'Tip amount:\t{round(tip_amt, 2):.2f}')
    # print(f'Total amount:\t{round(total_amt, 2):.2f}')
    print('Total amount:\t'+'{:.2f}'.format(round(total_amt, 2)))
print('Bye')