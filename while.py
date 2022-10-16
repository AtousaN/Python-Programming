"""
#E045 : dar surati k total akharin meghdar balaye 50 bashad
total = 0
while total <= 50 :
    num = int( input('Enter a number: ') )
    total += num
    print ('The total is ', total)
"""
"""
#E045 : dar surati k total akharin meghdar zire 50 bashad
total = 0
while total <= 50 :
    num = int( input('Enter a number: ') )
    total += num
    if total > 50 :
        print ('The total is higher than 50!')
        break
    print ('The total is ', total)
"""
"""
#E046
num = int( input('Enter a number: ') )
while num <= 5 :
    num = int( input('Enter a number: ') )
print('The last number you entered was a', num)
"""
"""
#E047
first = int( input('Enter a number: ') )
second = int( input('Enter another number: ') )
Sum = first + second
que = input('Do you want to add another number? (Answer with y or n) ')
que = que.lower()
while que == 'y' :
    num = int( input('Enter the number: '))
    Sum += num
    que = input('Do you want to add another number? (Answer with y or n) ')
    que = que.lower()
print ('The total is: ', Sum)
"""
"""
#E048
List = []
count = 0
name = input('Enter the name of whom you want to invite to the party: ')
print(name,'has now been invited')
List.append(name)
count += 1
que = input('Do you want to invite somebody else? (Answer with yes or no) ')
que = que.lower()
while que == 'yes' :
    name = input('Enter the name of whom you want to invite to the party: ')
    print(name,'has now been invited')
    List.append(name)
    count += 1
    que = input('Do you want to invite somebody else? (Answer with yes or no) ')
    que = que.lower()
print('You have', count, 'people coming to the party')
print(List)
"""
"""
#E049
compnum = 50
count = 0
num = int( input('Enter a number: ') )
while num != compnum :
    if num < compnum :
        print('Too low')
    elif num > compnum :
        print('Too high')
    count += 1
    num = int( input('Have another guess!: ') )
print('Well done, you took', count, 'attempts')
"""
"""
#E050
num = int( input('Enter a number between 10 and 20: ') )
while num < 10 or num > 20 :
    if num < 10 :
        print('Too low')
    elif num > 20 :
        print('Too high')
    num = int( input('Please try again: ') )
print('Thank you')
"""
"""
#E051
num = 10
print('There are',num,'green bottles hanging on the wall,',
      num,'green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
num = num - 1
answer = int( input('How many green bottles will be hanging on the wall? ') )
while num > 1 :
    if answer == num :
        print('There will be',num,'green bottles hanging on the wall.')
    else :
        print('No, try again')
    print('There are',num,'green bottles hanging on the wall,',
      num,'green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
    num = num - 1
    answer = int( input('How many green bottles will be hanging on the wall? ') )
if answer == num :
    print('There will be',num,'green bottle hanging on the wall.')
else :
    print('No, try again')
print('There is',num,'green bottle hanging on the wall,',
      num,'green bottle hanging on the wall, and if 1 green bottle should accidentally fall')
num = num - 1
answer = int( input('How many green bottles will be hanging on the wall? ') )
print('There are no more green bottles hanging on the wall!')
"""
