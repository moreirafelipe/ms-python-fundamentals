x = 42
y = 0

print('Practicing Errors Handling')

try:
    print(x / y)
    pass
except ZeroDivisionError as e:
    print('Not allowed to divide by zero!')
else:
    print('Something else went wrong!')
finally:
    print('This is our cleanup code!')