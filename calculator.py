# Made By Ethan Kharoufeh
#Latest Version: 9/5/2024
import time
def cls():
    print('\n' * 50)
print('Please Enter Username Below')

if input() == 'ethan.kharoufeh':
    print('User Found - Please enter Password Below')
else:
    print('Access Denied')
if input() == 'CSLOG':
    print('Access Granted')
else:
    print('Access Denied')
print('Taking You To Calculator')

time.sleep(1)

cls()
print('\nWhich Function Would You Like To Use? - Type "Directory" To See Possible Funtions')
stuff = input()

if stuff == ('sum'):
    cls()
    def sum(a, b, c):
        return (a + b + c)
    a = int(input('Enter 1st Number:'))
    b = int(input('Enter 2nd Number:'))
    c = int(input('Enter 3rd Number:'))
    print(f'Sum of {a}, {b} and {c} is {sum(a, b, c)}')

elif stuff == ('difference'):
    cls()
    def difference(a, b, c):
        return (a - b - c)
    a = int(input('Enter 1st Number:'))
    b = int(input('Enter 2nd Number:'))
    c = int(input('Enter 3rd Number:'))
    print(f'Difference of {a}, {b} and {c} is {difference(a, b, c)}')

elif stuff == ('product'):
    cls()
    def product(a, b, c):
        return (a * b * c)
    a = int(input('Enter 1st Number:'))
    b = int(input('Enter 2nd Number:'))
    c = int(input('Enter 3rd Number:'))
    print(f'Product of {a}, {b} and {c} is {product(a, b, c)}')

elif stuff == ('quotient'):
    cls()
    def quotient(a, b, c):
        return (a / b / c)
    a = int(input('Enter 1st Number:'))
    b = int(input('Enter 2nd Number:'))
    c = int(input('Enter 3rd Number:'))
    print(f'Quotient of {a}, {b} and {c} is {quotient(a, b, c)}')

elif stuff == ('exponent'):
    cls()
    def exponent(a, b):
        return (a ** b)
    a = int(input('Enter 1st Number:'))
    b = int(input('Enter 2nd Number:'))
    print(f'{a} to the {b} power is {exponent(a, b)}')

elif stuff == ('directory'):
    cls()
    print('Available Functions:\nsum\ndifference\nproduct\nquotient\nexponent')
    print('\nTo Use A Function, Type it Below')
while True:
    stuff = input()
    if stuff == ('sum'):
        cls()
        def sum(a, b, c):
            return (a + b + c)
        a = int(input('Enter 1st Number:'))
        b = int(input('Enter 2nd Number:'))
        c = int(input('Enter 3rd Number:'))
        print(f'Sum of {a}, {b} and {c} is {sum(a, b, c)}')
    
    elif stuff == ('difference'):
        cls()
        def difference(a, b, c):
            return (a - b - c)
        a = int(input('Enter 1st Number:'))
        b = int(input('Enter 2nd Number:'))
        c = int(input('Enter 3rd Number:'))
        print(f'Difference of {a}, {b} and {c} is {difference(a, b, c)}')
    
    elif stuff == ('product'):
        cls()
        def product(a, b, c):
            return (a * b * c)
        a = int(input('Enter 1st Number:'))
        b = int(input('Enter 2nd Number:'))
        c = int(input('Enter 3rd Number:'))
        print(f'Product of {a}, {b} and {c} is {product(a, b, c)}')
    
    elif stuff == ('quotient'):
        cls()
        def quotient(a, b, c):
            return (a / b / c)
        a = int(input('Enter 1st Number:'))
        b = int(input('Enter 2nd Number:'))
        c = int(input('Enter 3rd Number:'))
        print(f'Quotient of {a}, {b} and {c} is {quotient(a, b, c)}')
    
    elif stuff == ('exponent'):
        cls()
        def exponent(a, b):
            return (a ** b)
        a = int(input('Enter 1st Number:'))
        b = int(input('Enter 2nd Number:'))
        print(f'{a} to the {b} power is {exponent(a, b)}')
        break