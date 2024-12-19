print('Welcome to dictionaries')

states = {
    "OH": "Ohio",
    "KY": "Kentucky",
    "IN": "Indiana"
}

products = {
    1: "Hammer",
    2: "Nails",
    3: "Drill",
    4: "Screw"
}

# print the dictionaries:
print(f"states: {states}")
print(f"products: {products}")

# state_code = input('Enter State Abbreviation: ').upper()
# # check to see if state_code exists before retrieval
# if state_code in states:
#     #state_name = states[state_code]
#     state_name = states.get(state_code)
#     print(f'{state_code} is {state_name}')
# else:
#     print(f"No state entry for code: {state_code}")

product_id = 5

product = products.get(product_id, "NA")
print(f"product for code 5: {product}")

#del states["KY"]
del_state = states.pop("KY")
print(f"State deleted: {del_state}")
print(f"states: {states}")
print('Bye')

# p. 335
states['KY'] = 'Kentucky'
states['CO'] = 'Colorado'
states['FL'] = 'Florida'
states['MI'] = 'Muchigan'

print(f'States Dict: {states}')
states['MI'] = 'Michigan'
print(f'States Dict: {states}')
states['mi'] = 'test'
print(f'States Dict: {states}')
del states['mi']
print(f'States Dict: {states}')

print(f"\nkeys, values, items")
print("="*10)
print(f'Keys: {states.keys()}')
print(f'Values: {states.values()}')
print(f'Items: {states.items()}')

for key in sorted(states.keys()):
    print(f"StateCode: {key}")

for state_code, state_name in states.items():
    print(f"code: {state_code}, name: {state_name}")

countries = dict([("GB", "United Kingdom"),
                  ("US", "United States"),
                  ("NL", "Netherlands"),
                  ("DE", "Germany")])
print(f"countries: {countries}")