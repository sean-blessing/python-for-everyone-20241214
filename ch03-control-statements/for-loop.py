print('Welcome to for loops')

# print the numbers 0 to 10
print(f'range(11) = {range(11)}')
for i in range(11):
    print(i)

print(f'range(1, 21) = {range(1,21)}')
for i in range(1,21):
    print(i)

print(f'range(0,101,5) = {range(0,101,5)}')
for i in range(0,101,5):
    print(i)
    
print(f'range(200,-1,-25) = {range(200,-1,-25)}')
for i in range(200,-1,-25):
    print(i)

import numpy as np

print(f'arange(0.0, 5.0, .25) = {np.arange(0.0, 5.0, .25)}')
for i in np.arange(0.0, 5.0, .25):
    print(i)
    
# print(f'range(0.0, 5.0, 0.25) = {[i for i in range(0, 20)]}')
# for i in [x * 0.25 for x in range(0, 20)]:
#     print(i)

print('Bye')