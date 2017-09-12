"""
Example 1-3

"""
#Python Number
age=26
pi=3.14159

#Python String
string = 'Adan Umer'
tokens = string.split()

#Python List indexing
firstName = tokens[0]
lastName = tokens[1]

print('\n----- List test -----')
print('First Name: '+ firstName)
print('Last Name : '+ lastName)

#String Concatination
my_name = firstName+' '+lastName

print('\n----- String test -----')
print('My Name: '+ my_name)

#Python 'if' statement
print('\n----- If test -----')
if(string == my_name):
	print('Yes! Both strings are same')
	print('String: ' + string)
else:
	print('No! Both strings are not same')
	print('String1 :'+string + '  String2: '+my_name)

#Python List (Mutable)
print('\n----- List and For statement test -----')
students = ['Adnan','Zain', 'Aown']
students.append('Ali')

for student in students:
	print 'Hello!',student

#Python Tuple [Immutable Sequence]
ages = (19,22,18)

print('\n----- Tuple test -----')
for age in ages:
	print 'Age:', age

#Python Set [No order, No duplicates]
uniqueAges = set(ages)
uniqueAges.add(18) #already in set, no effect
uniqueAges.remove(22)
uniqueAges.add(25)

print('\n----- Set test -----')
for thisAge in uniqueAges:
	print thisAge

if 18 in uniqueAges:
	print 'There is an 18-year-old present!'
else:
	print 'There is no 18-year-old present!'

# sorting
students.sort()
orderedUniqueAges = sorted(uniqueAges)

print('\n----- Sorted students test -----')
for student in students:
	print 'Hello!', student


print('\n----- Sorted uniqueAges test -----')
for thisAge in orderedUniqueAges:
	print thisAge

#Python Dictionary - Mapping unique keys to values
netWorth = {}
netWorth['Donald Trump'] = 300000000
netWorth['Bill Gate'] = 500000000
netWorth['Tom Cruise'] = 4000000
netWorth['Joe Postdoc'] = 2000


print('\n----- Dictionary test -----')
for (person, worth) in netWorth.items():
	if worth < 100000:
		print 'Hmm!', person, 'is not a millionair'

if 'Tom Cruise' in netWorth:
	print 'show me the money'


print('\n----- End of the basic Python -----')



