def process(after, input):
    # user = [list(item) for item in input]
    user = [['ruby', 6000, 5000], ['diamond', 5000, 4000]]
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

    print(count)
    # counts the number of people that will be taking a gem
    numberOfPeopleTotal = count / 2
    # this is your location in the list of people
    gemToTake = numberOfPeopleTotal - after
    # extra user list just incase
    saveList = user


    # final array, will have gem, and price
    order = []
    i = 0
    j = 0
    # makes 2d array into 1 array
    for out in user:
        for inner in user[i]:
            force = user[i][j]
            temp = str(user[i][j])

            if j == 0:
                name = user[i][j]



            if is_number(force) is True:
                order.append(name)
                num = int(temp)
                order.append(num)
        j = j + 1
    i = i + 1

    newList = user


    #print(order)

        



def is_number(a):
    try:
        number = float(a)
        return True
    except ValueError:
        return False
