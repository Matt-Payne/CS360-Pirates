from operator import itemgetter, attrgetter

def is_number(a):
    try:
        number = float(a)
        return True
    except ValueError:
        return False









# user = {('diamond', 100), ('diamond', 5000), ('ruby', 200), ('diamond', 1050), ('saphire', 30), ('saphire', 100), ('iron', 30), ('bitcoin',5000)}

#user = (sorted(user, key=itemgetter(0)))
#print(user)

#print(sorted(user, key=itemgetter(1), reverse=True))


user = [['ruby', 6000, 5000], ['diamond', 5000, 4000]]



count = 0
i = 0
j = 0
for index in user:
    for inside in index:
        if is_number(inside) is True :
                count = count + 1
        j = j + 1
    i = i + 1

print(count)
"""""
nameCount = len(user)
print("number of lists in the list :",nameCount)
counter = len(user[1])
"""""
temp = 'true'

if temp[0] != '1' or temp[0] != '2' or temp[0] != '3' or temp[0] != '4' or temp[0] != '5' or temp[0] != '6' or temp[0] != '7' or temp[0] != '8' or temp[0] != '9' or temp[0] != '0':
    name = temp
    print(name)

size = len(user)
print(size)


i = 0
j - 0

while (i < size):
    while (j < len(user[i])):
        print(user[i][j])
        j= j + 1
    i = i + 1