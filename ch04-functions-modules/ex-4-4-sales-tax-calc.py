from ex_4_4_sales_calc_module import calc_sales_tax, calc_sales_total_after_tax

def main():
    print('Sales Tax Calculator\n')
    choice = 'y'
    while choice == 'y':
        total_cost = 0.0
        print('ENTER ITEMS (ENTER 0 TO END)')
        item_cost = 1.0
        while (item_cost != 0):
            item_cost = float(input('Cost of item: '))
            total_cost += item_cost
        print(f'Total:           {total_cost:.2f}')
        print(f'Sales Tax:       {calc_sales_tax(total_cost):.2f}')
        print(f'Total After Tax: {calc_sales_total_after_tax(total_cost):.2f}')
        print()
        choice = input('Again? (y/n): ')
        print()
    print('Thanks, bye!')

if __name__ == '__main__':
    main()