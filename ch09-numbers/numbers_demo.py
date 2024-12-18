print('Welcome to fun with numbers')
balance = 100.10
print(f'Balance: {balance}')
balance += 100.10
print(f'Balance: {balance}')
balance += 100.10
print(f'Balance: {balance}')

balance = round(balance, 2)
print(f'Balance: {balance:.2f}')

print(f'Pow 2^3: {pow(2,3)}')
import math as m
print(f'm.pow(2,3): {m.pow(2,3)}')
print(f'm.sqrt(16): {m.sqrt(16)}')
print(f'm.pi: {m.pi}')
print(f'm.floor(12.545): {m.floor(12.545)}')
print(f'm.ceil(12.545): {m.ceil(12.545)}')

print('f strings w/ format specification...')
fp_number = 12345.6789
print(f'{fp_number:.2f}')
print(f'{fp_number:,.2f}')
print(f'{fp_number:15,.2f}')
print(f'{fp_number:.2e}')

fp_number = .12345
print(f'{fp_number:.0%}')
print(f'{fp_number:.1%}')

int_number = 12345
print(f'{int_number:d}')
print(f'{int_number:,d}')

print('---- string literal formatting ----')
spec = 15
print(f"{'Description':{spec}}.")

print(f"{'Description':15} {'Price':>10} {'Qty':>5}")
print(f"{'Hammer':15} {9.99:10.2f} {3:5d}")

print('Currency and Locale')
import locale as lc

lc.setlocale(lc.LC_ALL, "en_US")
print(lc.currency(12345.15, grouping=True))

print('Rounding...')

from decimal import Decimal

discount = Decimal("10.005")
print(f'discount: {discount}')
discount = discount.quantize(Decimal("1.00"))
print(f'discount.quantize("1.00"): {discount}')

print('Bye')