#Combining Strings
first_name = 'Christopher' #Single and double quotes are acceptable
last_name = 'Harrison'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)

#You can use functions to modify strings
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

#The functions help us format strings we save to files and databases, or display users
first_name = input("What is your first name?")
last_name = input("What is your last name?")
print('Hello ' + first_name.capitalize() + ' ' \
    + last_name.capitalize())