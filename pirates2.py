def is_number(a):
    try:
        number = float(a)
        return True
    except ValueError:
        return False

    # user = [list(item) for item in input]
after = 3

print('given after value, how many people come after me :', after)
user = [['ruby', 6000, 5000], ['diamond', 5000, 4000], ['saphire', 50, 10, 15, 75,90,100]]
    # number of people after you
numberPicksAfter = after * 2
    # [[ 'ruby', 6000, 5000], ['diamond', 5000, 4000]]

    # number of gems
count = 0
i = 0
j = 0
for index in user:
    for inside in index:
        if is_number(inside) is True:
            count = count + 1
        j = j + 1
    i = i + 1

print('count of how many numbers: ', count)
    # counts the number of people that will be taking a gem
numberOfPeopleTotal = count / 2
print('number of people total that take a gem', numberOfPeopleTotal)
    # this is your location in the list of people
gemToTakeFirst = numberOfPeopleTotal - after
print('gem to take, which first spot in line you are', gemToTakeFirst)

choicesAfterMe = after * 2


gemToTakeSecond = numberOfPeopleTotal + after + 1
print('which gem in the order to take second', gemToTakeSecond)
    # extra user list just incase
saveList = user

    # final array, will have gem, and price
order = []
i = 0
j = 0
print(user)
    # makes 2d array into 1 array
for index in user:
    for inside in index:

        temp = str(inside)

        if temp[0] != '1' and temp[0] != '2' and temp[0] != '3' and temp[0] != '4' and temp[0] != '5' and temp[0] != '6' and \
                        temp[0] != '7' and temp[0] != '8' and temp[0] != '9' and temp[0] != '0':
            name = temp

        else:
            order.append(name)
            num = int(temp)
            order.append(num)





newList = user


print('order : ',order)


