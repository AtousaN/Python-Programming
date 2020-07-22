year = int(input('Enter year number: '))
if year%4 != 0 :
    print('not Leap Year')
elif year%4 == 0 :
    if year%100 == 0 :
        if year%400 == 0 :
            print('Leap Year')
        else:
            print('not Leap Year')
    else:
        print('Leap Year')

