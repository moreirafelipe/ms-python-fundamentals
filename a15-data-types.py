#To get current date and time
#We need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()

#The now function returns a datetime object
print('Today is: ' + str(current_date))

#Timedelta is used to deine a period of time
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

#Controling date formating
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

birthday = str(input('When is your birthday (dd/mm/yyyy)?\n'))

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ', str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day