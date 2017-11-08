from operator import itemgetter, attrgetter
def is_number(a):
    try:
        number = float(a)
        return True
    except ValueError:
        return False



def process(after, input):
    user = [list(item) for item in input]

    temp = after
    after = temp


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


    # counts the number of people that will be taking a gem
    numberOfPeopleTotal = count / 2

    # this is your location in the list of people
    gemToTakeFirst = numberOfPeopleTotal - after


    choicesAfterMe = after * 2

    gemToTakeSecond = numberOfPeopleTotal + after + 1

    # extra user list just incase
    saveList = user

    # final array, will have gem, and price
    order = []
    i = 0
    j = 0

    # makes 2d array into 1 array
    for index in user:
        for inside in index:

            temp = str(inside)

            if temp[0] != '1' and temp[0] != '2' and temp[0] != '3' and temp[0] != '4' and temp[0] != '5' and temp[
                0] != '6' and \
                            temp[0] != '7' and temp[0] != '8' and temp[0] != '9' and temp[0] != '0':
                name = temp

            else:
                order.append(name)
                num = int(temp)
                order.append(num)

    newList = user


    length = len(order)
    tempList = []
    finalList = []
    i = 0
    while (i < length):
        temp = order[i]
        temp2 = order[i + 1]
        tempList.append(temp)
        tempList.append(temp2)
        __tuple = tuple(tempList)
        finalList.append(__tuple)
        tempList = []
        i = i + 2


    user = (sorted(finalList, key=itemgetter(0)))


    tupleListInOrder = (sorted(user, key=itemgetter(1), reverse=True))



    backToList = [list(item) for item in tupleListInOrder]


    if gemToTakeFirst - 1 >= 0:
        firstPick = int(gemToTakeFirst - 1)

    else:
        firstPick = 0

    if gemToTakeSecond - 1 >= 0:
        secondPick = int(gemToTakeSecond - 1)

    else:
        secondPick = 0

    # element 3 not 4, already accounted for starting at 0 and not 1 etc user[3] instead of user[4]


    # list like ['bitcoin',5000]
    myPick1 = backToList[firstPick]


    myPick2 = backToList[secondPick]


    firstString = ""
    firstString = str(myPick1[0])
    firstString = firstString + ':'
    firstString = firstString + str(myPick1[1])



    secondString = ""
    secondString = str(myPick2[0])
    secondString = secondString + ':'
    secondString = secondString + str(myPick2[1])



    finalString = firstString + ' ' + secondString

    return finalString

