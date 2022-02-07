province = input('What province do you live in? ')
tax = 0

#And/ Or conditional
if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

#In
if province in('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

#Nested conditions
country = input('What country do you live in? ')

if country == 'Canada':
    province = input('What province/ state do you live in? ')

    if province in('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0