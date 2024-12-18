import locale as lc

lc.setlocale(lc.LC_ALL, "en_US")
price = 12345.14567
print(f'price: {price}')
print(f'price as currency format: {lc.currency(price, grouping=True)}')