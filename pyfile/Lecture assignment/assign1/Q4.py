year = int(input())
if year<1:
    print('Invalid year entered.')
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Leap year.')
else:
    print('Not a leap year.')