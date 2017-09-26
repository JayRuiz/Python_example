
input = 'Jay, Kim, 1971, 10, 17, male'

tokens = input.split(',')

firstName = tokens[0]
lastName = tokens[1]

birthDate = (int(tokens[2]), int(tokens[3]), int(tokens[4]))
isMale = (tokens[5] == 'male')

print 'Howday!', firstName, lastName
print 'Birthday', birthDate


