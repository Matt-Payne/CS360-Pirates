def process(after, input):
    user = [list(item) for item in input]
    # number of people after you
    numberPeopleAfter = after * 2
    # [[ 'ruby', 6000, 5000], ['diamond', 5000, 4000]]

    # number of gems
    count = 0
    i = 0
    j = 0
    for index in user:
        for inside in user[i]:
            if is_number(user[i][j]) is True :
                    count = count + 1
        j = j + 1
    i = i + 1
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
    # Left Of

        



def is_number(a):
    try:
        number = float(a)
        return True
    except ValueError:
        return False
