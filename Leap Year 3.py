year = int(input('Enter year number: '))
if (year%4 == 0 and year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0) :
    print('Leap Year')
elif year%4 != 0 or (year%4 == 0 and year%100 == 0) :
    print('not Leap Year')

     
