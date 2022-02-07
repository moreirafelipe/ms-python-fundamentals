#import module
#import datetime

#import attribute from module
from datetime import datetime

#print timestamps to see how long sections
#take to run

first_name = 'Susan'
print('Task completed')

#First datetime is the module, the second is the attribute
print(datetime.now())
print()

for x in range(0,10):
    print(x)

print('Task completed')
print(datetime.now())
print()

#Using functions
def print_time():
    print('Task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()

#Print timestapms to see how long sections of code take run
first_name = 'Susan'
print('First name assigned')
print(datetime.now())
print()

for x in range(0,10):
    print(x)

print('Loop completed')
print(datetime.now())
print()

#Print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('First name assigned')

for x in range(0,10):
    print(x)
print_time('loop_completed')

#Same logic over
first_name = input('enter your first name: ')
first_name_initial = first_name[0:1]

last_name = input('enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + ' ' + last_name_initial)

#Optimizing code
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + get_initial(first_name) + get_initial(last_name))