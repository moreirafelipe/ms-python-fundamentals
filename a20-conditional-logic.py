price = input('How much did you pay? ')

#Simple conditional
price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))

#Composed conditional
price = input('How much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = 0.7
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))


#Lowercase input example
country = input('Enter the name of your home country: ')

if country.lower() == 'Canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')

