#A student makes honour roll if their average is >= 85
#And their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll')

if gpa >= .85 and lowest_grade >= .70:
    print('Well done')

#Using conditionals
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('Well done')