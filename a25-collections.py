from array import array

names = ['Christopher', 'Susan']
scores = []

#Add new item in the last position
scores.append(98) 
scores.append(99)
print(names)
print(scores)

#Collections are zero-indexed
print(scores[1])

scores = array('d')

scores.append(97)
scores.append(98)

print(scores)
print(scores[1])

#Get len of an array
print(len(names))

#Insert before index
names.insert(0, 'Bill')
names.insert(0, 'Justin')
print(names)

names.sort()
print(names)

#Start and end index
presenters = names[1:3]

print(names)
print(presenters)

#Dictionaries - key value structures
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])
print(person['last'])