"""
#E069
T1 = ('Iran', 'Germany', 'Japan', 'America', 'Canada')
print (T1)
country = input ('Enter one of the countries that have been shown: ')
print (T1.index(country))
"""
"""
#E070
T1 = ('Iran', 'Germany', 'Japan', 'America', 'Canada')
print (T1)
country = input ('Enter one of the countries that have been shown: ')
print (T1.index(country))
number = int( input('Enter a numbe between 0 and 4: '))
print (T1[number])
"""
"""
#E071
L1 = ['Tennis', 'Swimming']
sport = input ('What is your favourite sport? ')
sport = sport.capitalize()
L1.append(sport)
L1.sort()
print (L1)
"""
"""
#E072
L1 = ['Math', 'Science', 'Art', 'History', 'Music', 'Geography']
print ('Which of these subjects do not you like? ')
print (L1)
dislike = input ()
L1.remove(dislike)
print (L1)
"""
"""
#E073
a = input('Your First Favourite Food: ')
b = input('Your Second Favourite Food: ')
c = input('Your Third Favourite Food: ')
d = input('Your Fourth Favourite Food: ')
Dic = {1: a , 2: b , 3: c , 4: d}
print(Dic)
discard = int( input('Which one do you want to get rid of? '))
Dic.pop(discard,'Enter a number between 1 and 4')
List = list(Dic.values())
L = []
for i in range(len(List)) :
    str = List[i-1]
    L.append(str.capitalize())
L.sort()
print(L)
"""
"""
#E074
L1 = ['Red', 'Blue', 'Yellow', 'Orange', 'Pink', 'Purple', 'Green', 'Brown', 'Black', 'White' ]
start = int( input('Enter a number between 0 and 4: ') )
end = int( input('Enter a number between 5 and 9: ') )
print (L1[(start+1):end])
"""
"""
#E075
L1 = [100, 200, 300]
for elem in L1 :
    print (elem)
num = int( input('Enter a three-digit number: ') )
if num in L1 :
    print (L1.index(num))
else :
    print ('That is not in the list')
"""
"""
#E076
Guest1 = input('Enter the names of first people you want to invite to a party: ')
Guest2 = input('Enter the names of second people you want to invite to a party: ')
Guest3 = input('Enter the names of third people you want to invite to a party: ')
List = [Guest1, Guest2, Guest3]
count = 3
y_n = input ('Do you want to invite any other person? (Answer with yes or no) ')
y_n = y_n.lower()
while y_n == 'yes' :
    new = input('Enter the name: ')
    List.append(new)
    count += 1
    y_n = input ('Do you want to invite any other person? ')
    y_n = y_n.lower()
print ('The number of guests are: ', count)
"""
"""
#E077
Guest1 = input('Enter the names of first people you want to invite to a party: ')
Guest2 = input('Enter the names of second people you want to invite to a party: ')
Guest3 = input('Enter the names of third people you want to invite to a party: ')
List = [Guest1, Guest2, Guest3]
count = 3
y_n = input ('Do you want to invite any other person? (Answer with yes or no) ')
y_n = y_n.lower()
while y_n == 'yes' :
    new = input('Enter the name: ')
    List.append(new)
    count += 1
    y_n = input ('Do you want to invite any other person? ')
    y_n = y_n.lower()
print ('The number of guests are: ', count)
print (List)
entry = input('Enter one of the names in the list: ')
print('This person is number ', List.index(entry)+1, 'in the list')
doubt = input('Do you still want this person to come to the party? ')
doubt = doubt.lower()
if doubt == 'no' :
    List.pop(List.index(entry))
    print (List)
else :
    print (List)
"""
"""
#E078
TV = ['Friends', '24', 'Downton Abbey', 'Sherlock']
for elem in TV :
    print (elem)
show = input('Enter another show: ')
position = int( input('Enter the position you want it inserted into the list: ') )
TV.insert(position-1,show)
print (TV)
"""
"""
#E079
nums = []
for i in range(3) :
    n = input('Enter a number: ')
    nums.append(n)
    print (nums)
que = input('Do you still want the last number you entered saved? (Answer with yes or no) ')
que = que.lower()
if que == 'no' :
    nums.pop(2)
    print (nums)
else :
    print (nums)
"""








