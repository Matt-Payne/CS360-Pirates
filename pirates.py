def process(after, input):
    user = [list(item) for item in input]
    # number of people after you
    numberPeopleAfter = after * 2
    # [[ 'ruby', 6000, 5000], ['diamond', 5000, 4000]]

    # number of gems
    count = 0
    for i in user:
        for j in user[i]:
            if is_number(user[i][j]) is True :
                    count++
        j++
    i++
    # counts the number of people that will be taking a gem
    numberOfPeopleTotal = count / 2
    # this is your location in the list of people
    gemToTake = numberOfPeopleTotal - after
    # extra user list just incase
    saveList = user


    # final array, will have gem, and price
    order = []
    # makes 2d array into 1 array
    for i in user:
        for j in user[i]:
            force = user[i][j]
            temp = str(user[i][j])

            if j == 0:
                name = user[i][j]



            if is_number(force) is True :
                order.append(name)
                num = int(temp)
                order.append(num)
        j++
    i++

    for i in order :
        



def is_number(a):
    try :
        number = float(a)
        return True
    except ValueError:
        return False
