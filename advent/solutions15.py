#Day 1
def day1_2015(part1_input):
    #Part 1
    counter = 0
    for a in part1_input:
        if a == "(":
            counter += 1
        elif a == ")":
            counter -= 1
        else:
            break
            print("Error")
    solution1 = counter

    #Part 2
    counter = 0
    position = 0
    for a in part1_input:
        if a == "(":
            counter += 1
        elif a == ")":
            counter -= 1
        else:
            break
            print("Error")
        position += 1
        if counter <= -1:
            break
    solution2 = position

    return solution1, solution2

#Day 2
def day2_2015(part1_input):

    #Part 1
    input_list = part1_input.split()
    areas_list = []
    order_list = []
    shopping_list = []

    for present in input_list:
        a, b, c = present.split('x')
        areas_list.append([int(a), int(b), int(c)])

    for a in areas_list:
        x = 2 * a[0] * a[1]
        y = 2 * a[1] * a[2]
        z = 2 * a[2] * a[0]
        b = [x, y, z]
        b.sort()
        xtra = b[:1]
        b.append(xtra[0] / 2)
        order_list.append(b)

    for present in order_list:
        shopping_list.append(sum(present))

    solution1 = sum(shopping_list)

    print(input_list)

    #Part 2
    ribbon_list = []
    for a in areas_list:
        a.sort()
        ribbon = 2 * a[0] + 2 * a[1] + (a[0] * a[1] * a[2])
        ribbon_list.append(ribbon)
    solution2 = sum(ribbon_list)

    return solution1, solution2

#Day 3
def day3_2015(part1_input):
    #Part 1
    Visits = [[0, 0]]
    Coord = [0, 0]
    print(part1_input)
    for char in part1_input:
        x = char
        if x == "^":
            Coord[0] = Coord[0] + 1
            Visits.append(Coord.copy())
        elif x == "v":
            Coord[0] = Coord[0] - 1
            Visits.append(Coord.copy())
        elif x == "<":
            Coord[1] = Coord[1] - 1
            Visits.append(Coord.copy())
        elif x == ">":
            Coord[1] = Coord[1] + 1
            Visits.append(Coord.copy())

    Unique_Houses = []
    for item in Visits:
        if item not in Unique_Houses:
            Unique_Houses.append(item)

    solution1 = len(Unique_Houses)
    #solution1 = part1_input

    #Part 2
    Coord1 = [0, 0]
    Coord2 = [0, 0]
    Counter = 1
    Stops = [[0, 0]]

    for char in part1_input:
        x = char
        if x == "^":
            if Counter == 1:
                Coord1[0] = Coord1[0] + 1
                Stops.append(Coord1.copy())
                Counter = 2
            else:
                Coord2[0] = Coord2[0] + 1
                Stops.append(Coord2.copy())
                Counter = 1
        elif x == "v":
            if Counter == 1:
                Coord1[0] = Coord1[0] - 1
                Stops.append(Coord1.copy())
                Counter = 2
            else:
                Coord2[0] = Coord2[0] - 1
                Stops.append(Coord2.copy())
                Counter = 1
        elif x == "<":
            if Counter == 1:
                Coord1[1] = Coord1[1] - 1
                Stops.append(Coord1.copy())
                Counter = 2
            else:
                Coord2[1] = Coord2[1] - 1
                Stops.append(Coord2.copy())
                Counter = 1
        elif x == ">":
            if Counter == 1:
                Coord1[1] = Coord1[1] + 1
                Stops.append(Coord1.copy())
                Counter = 2
            else:
                Coord2[1] = Coord2[1] + 1
                Stops.append(Coord2.copy())
                Counter = 1

    Unique_Stops = []
    for item in Stops:
        if item not in Unique_Stops:
            Unique_Stops.append(item)

    solution2 = len(Unique_Stops)

    return solution1, solution2

#Day 4
def day4_2015(part1_input):
    import hashlib

    #Part 1
    key = part1_input
    counter = 1
    concat = key + str(counter)
    code = hashlib.md5(concat.encode('utf-8'))

    while str(code.hexdigest())[0:5] != '00000':
        counter = counter + 1
        concat = key + str(counter)
        code = hashlib.md5(concat.encode('utf-8'))

    solution1 = counter

    #Part 2
    key = part1_input
    counter = 1
    concat = key + str(counter)
    code = hashlib.md5(concat.encode('utf-8'))

    while str(code.hexdigest())[0:6] != '000000':
        counter = counter + 1
        concat = key + str(counter)
        code = hashlib.md5(concat.encode('utf-8'))

    solution2 = counter

    return solution1, solution2

#Day 5
def day5_2015(part1_input):
    input_list = part1_input.split()

    def countvowels(word):
        vowels = False
        a = word.count('a')
        e = word.count('e')
        i = word.count('i')
        o = word.count('o')
        u = word.count('u')
        if (a + e + i + o + u) >= 3:
            vowels = True
        else:
            vowels = False
        return vowels


    def countdups(word):
        counter = 0
        dups = False
        a = ''
        for char in word:
            if char == a:
                dups = True
            a = char
        return dups


    def checksubs(word):
        subs = False
        if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
            subs = True
        return subs

    counter = 0

    for entry in input_list:
        vowels = countvowels(entry)
        dups = countdups(entry)
        subs = checksubs(entry)

        # If all tests are good, increase the counter
        if vowels == True and dups == True and subs == False:
            counter = counter + 1

    solution1 = counter

    #Part 2
    def doublepair(word):
        n = len(word)
        c = len(word)
        dubs = False
        for a in word:
            pair = a + word[(1 + n - c)]
            b = word.count(pair)
            trip = a + a + a
            d = word.count(trip)
            quad = a + a + a + a
            p = word.count(quad)
            if p >= 1 or b - d >= 2:
                dubs = True
                break
            c = c - 1
            if c <= 1:
                break
        return dubs

    def bridge(word):
        n = 2
        l = len(word)
        xyx = False
        for a in word:
            if a == word[n]:
                xyx = True
                break
            n = n + 1
            if n == l:
                break
        return xyx

    counter = 0
    for entry in input_list:
        dubs = doublepair(entry)
        xyx = bridge(entry)
        if dubs == True and xyx == True:
            counter = counter + 1

    solution2 = counter

    return solution1, solution2

#Day 6
def day6_2015(part1_input):
    import numpy as np

    #Part 1
    grid = np.zeros((1000, 1000))
    split_input = part1_input.split()
    input_list = []
    counter = 1
    for word in split_input[1:]:
        if word == 'turn' or word == 'toggle':
            input_list += [' '.join(split_input[:counter])]
            split_input = split_input[counter:]
            counter = 0
        counter += 1
    input_list += [' '.join(split_input)]

    def turnoff(command, grid):
        start = command.split(' ')[2]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[4]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                grid[counterx, countery] = 0
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid


    def turnon(command, grid):
        start = command.split(' ')[2]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[4]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                grid[counterx, countery] = 1
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid


    def toggle(command, grid):
        start = command.split(' ')[1]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[3]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                if y == 1:
                    grid[counterx, countery] -= 1
                else:
                    grid[counterx, countery] += 1
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid

    for command in input_list:
        if command.split(' ')[0] == 'toggle':
            grid = toggle(command, grid)
        elif command.split(' ')[1] == 'off':
            grid = turnoff(command, grid)
        elif command.split(' ')[1] == 'on':
            grid = turnon(command, grid)
        else:
            print('Command Error')

    solution1 = np.sum(grid)

    #Part 2
    grid = np.zeros((1000, 1000))

    def turnoff2(command, grid):
        start = command.split(' ')[2]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[4]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                if y >= 1:
                    grid[counterx, countery] -= 1
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid

    def turnon2(command, grid):
        start = command.split(' ')[2]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[4]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                grid[counterx, countery] += 1
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid

    def toggle2(command, grid):
        start = command.split(' ')[1]
        startx = int(start.split(',')[0])
        starty = int(start.split(',')[1])
        end = command.split(' ')[3]
        endx = int(end.split(',')[0]) + 1
        endy = int(end.split(',')[1]) + 1

        counterx = startx
        countery = starty
        changed = 0

        for x in grid[startx:endx]:
            for y in x[starty:endy]:
                grid[counterx, countery] += 2
                countery += 1
                changed += 1
            countery = starty
            counterx += 1
        return grid

    for command in input_list:
        if command.split(' ')[0] == 'toggle':
            toggle2(command, grid)
        elif command.split(' ')[1] == 'off':
            turnoff2(command, grid)
        elif command.split(' ')[1] == 'on':
            turnon2(command, grid)
        else:
            print('Command Error')

    solution2 = np.sum(grid)

    return solution1, solution2

#Day 7
def day7_2015(part1_input):
    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter] == '->':
            input_list += [' '.join(split_input[:(counter + 2)])]
            split_input = split_input[(counter + 2):]
            counter = 0
        else:
            counter += 1

    # Part 1
    def run(input_list, signals, count):
        count = 0
        for step in input_list:
            split = str.split(step)
            if 'NOT' in split:
                signals, count = NOTGate(step, signals, count)
            elif 'OR' in split:
                signals, count = ORGate(step, signals, count)
            elif 'AND' in split:
                signals, count = ANDGate(step, signals, count)
            elif 'RSHIFT' in split:
                signals, count = RSGate(step, signals, count)
            elif 'LSHIFT' in split:
                signals, count = LSGate(step, signals, count)
            elif '->' in split:
                signals, count = noGate(step, signals, count)
            else:
                raise Exception('Unrecognised input.')

        return signals, count


    def noGate(step, dic, exc):
        list = str.split(step)
        try:
            list[0] = int(list[0])
        except:
            pass

        if list[2] not in dic:
            if isinstance(list[0], int) == True:
                dic[list[2]] = list[0]
            elif list[0] in dic:
                dic[list[2]] = dic[list[0]]
            else:
                exc = exc + 1
        return dic, exc

    def NOTGate(step, dic, exc):
        list = str.split(step)  # splits into a list containing [NOT, ll, ->, ll]
        try:
            list[1] = int(list[1])
        except:
            pass

        if list[3] not in dic:
            if isinstance(list[1], int) == True:
                newSignal = ~(list[1])
                dic[list[3]] = newSignal
            elif list[1] in dic:
                newSignal = ~(dic[list[1]])
                dic[list[3]] = newSignal
            else:
                exc = exc + 1
        return dic, exc

    def ORGate(step, dic, exc):
        list = str.split(step)  # splits into a list containing [ll, OR, ll, ->, ll]
        try:
            list[0] = int(list[0])
        except:
            pass
        try:
            list[2] = int(list[2])
        except:
            pass

        if list[4] not in dic:
            if isinstance(list[0], int) and isinstance(list[2], int) == True:
                newSignal = (list[0] | list[2])
                dic[list[4]] = newSignal
            elif isinstance(list[0], int) == True and list[2] in dic:
                newSignal = (list[0] | dic[list[2]])
                dic[list[4]] = newSignal
            elif isinstance(list[2], int) == True and list[0] in dic:
                newSignal = (dic[list[0]] | list[2])
                dic[list[4]] = newSignal
            elif list[0] in dic:
                if isinstance(list[2], int) == True:
                    newSignal = (dic[list[0]] | list[2])
                    dic[list[4]] = newSignal
                elif list[2] in dic:
                    print(list[0], list[2])
                    newSignal = (dic[list[0]] | dic[list[2]])
                    dic[list[4]] = newSignal
            else:
                exc = exc + 1
        return dic, exc

    def ANDGate(step, dic, exc):
        list = str.split(step)
        try:
            list[0] = int(list[0])
        except:
            pass
        try:
            list[2] = int(list[2])
        except:
            pass

        if list[4] not in dic:
            if isinstance(list[0], int) and isinstance(list[2], int) == True:
                newSignal = (list[0] & list[2])
                dic[list[4]] = newSignal
            elif isinstance(list[0], int) == True and list[2] in dic:
                newSignal = (list[0] & dic[list[2]])
                dic[list[4]] = newSignal
            elif list[0] in dic:
                if isinstance(list[2], int) == True:
                    newSignal = (dic[list[0]] & list[2])
                    dic[list[4]] = newSignal
                elif list[2] in dic:
                    print(list[0], list[2])
                    newSignal = (dic[list[0]] & dic[list[2]])
                    dic[list[4]] = newSignal
            else:
                exc = exc + 1
        return dic, exc

    def RSGate(step, dic, exc):
        list = str.split(step)

        if list[4] not in dic:
            if list[0] in dic:
                newSignal = (dic[list[0]] >> int(list[2]))
                dic[list[4]] = newSignal
            else:
                exc = exc + 1
        return dic, exc

    def LSGate(step, dic, exc):
        list = str.split(step)

        if list[4] not in dic:
            if list[0] in dic:
                newSignal = (dic[list[0]] << int(list[2]))
                dic[list[4]] = newSignal
            else:
                exc = exc + 1
        return dic, exc

    signals = {}
    counter = 1
    while counter != 0:
        signals, counter = run(input_list, signals, counter)
    solution1 = signals['a']

    #Part 2

    counter = 0
    while counter < len(input_list):
        if input_list[counter][-2:] == ' b':
            input_list[counter] = str(signals['a']) + ' -> b'
        counter += 1

    signals = {}
    counter = 1
    while counter != 0:
        signals, counter = run(input_list, signals, counter)
    solution2 = signals['a']

    return solution1, solution2

#Day 8
def day8_2015(part1_input):

    input_list = list(part1_input)
    # This is a really lazy bit of refactoring to just force the import to match what Jupyter notebooks would read :p
    for char in range(0,len(input_list)):
        if input_list[char] == ' ':
            input_list[char] = '\n'

    #Part 1
    codeCount = 0
    strCount = 0
    holdTag = 0

    for char in input_list:

        if holdTag == 3:  # ignores the second hex character
            holdTag = 0

        elif holdTag == 2:  # ignores the first hex character
            holdTag = 3

        elif holdTag == 1:
            if char == '"':  # ignores the extra \
                holdTag = 0
            elif char == '\\':  # ignores the extra \
                holdTag = 0
            elif char == 'x':  # ignores the extra \
                holdTag = 2

        elif char == '\\':  # counts one for any escape sequence, then enters loop to ignore the rest
            holdTag = 1
            strCount = strCount + 1

        elif char == '\n':  #
            codeCount -= 1

        elif char == '"':
            pass

        else:
            strCount = strCount + 1

        codeCount += 1
    solution1 = codeCount - strCount

    #Part 2

    codeCount = 0
    encodeCount = 2  # start at two to cover the additional " you'll need at either end

    for char in input_list:

        if char == '"':
            encodeCount += 2

        elif char == '\\':
            encodeCount += 2

        elif char == '\n':  #
            codeCount -= 1
            encodeCount += 2  # to add the " to the end of the current expression and the start of the new one

        else:
            encodeCount += 1

        codeCount += 1

        solution2 = encodeCount - codeCount

    return solution1, solution2

#Day 9
def day9_2015(part1_input):
    import itertools

    split_input = part1_input.split()
    input_list = []
    counter = 0
    while len(split_input) > 0:
        try:
            a = int(split_input[counter])
            input_list += [' '.join(split_input[:(counter + 1)])]
            split_input = split_input[(counter + 1):]
            counter = 0
        except:
            counter += 1

    #Part 1
    places = []
    for route in input_list:
        step = str.split(route)
        if step[0] in places:
            pass
        else:
            places += [step[0]]
        if step[2] in places:
            pass
        else:
            places += [step[2]]

    register = {}

    for place in places:
        otherPlaces = places.copy()
        otherPlaces.remove(place)
        register[place] = {}
        for otherPlace in otherPlaces:
            for route in input_list:
                step = str.split(route)
                if place in step and otherPlace in step:
                    register[place][otherPlace] = int(step[4])

    answer = 1000000
    for combo in list(itertools.permutations(places)):
        length = len(combo)
        step = 0
        total = 0
        for leg in combo:
            if step == length - 1:
                pass
            else:
                total += register[combo[step]][combo[step + 1]]
            step += 1

        if total <= answer:
            answer = total
    solution1 = answer

    #Part 2
    answer = 0
    for combo in list(itertools.permutations(places)):
        length = len(combo)
        step = 0
        total = 0
        for leg in combo:
            if step == length - 1:
                pass
            else:
                total += register[combo[step]][combo[step + 1]]
            step += 1

        if total >= answer:
            answer = total
    solution2 = answer

    return solution1, solution2

#Day 10
def day10_2015(part1_input):

    #Part 1
    LaS = part1_input
    for n in range(40):
        new = ""
        counter = 1
        run = 1
        for x in LaS:
            if counter == len(LaS):
                new = new + str(run) + str(x)
                LaS = new

            elif x == LaS[counter]:
                run += 1

            else:
                new = new + str(run) + str(x)
                run = 1

            counter += 1
        solution1 = str(len(LaS))

    #Part 2

    solution2 = "Due to server constraints, Part 2 must be run on a local machine. Code can be accessed through the 'solution' link:"

    return solution1, solution2

#Day 11
def day11_2015(part1_input):

    def solution(inpt):
        numInpt = []
        oupt = ''

        for char in inpt:
            number = ord(char) - 96
            numInpt.append(number)

        run = False
        trick = False
        pair1 = False
        pair2 = False
        counter3 = 0

        for x in range(1000000):

            run = False
            trick = True
            pair1 = False
            pair2 = False
            skip = False

            counter1 = 0

            for x in numInpt[:6]:
                if numInpt[counter1 + 1] == x + 1:
                    if numInpt[counter1 + 2] == x + 2:
                        run = True
                else:
                    counter1 += 1

            for x in numInpt:
                if x == ord('i') - 96 or x == ord('o') - 96 or x == ord('l') - 96:
                    trick = True
                else:
                    trick = False

            counter2 = 0

            for x in numInpt[:7]:
                if x == numInpt[counter2 + 1]:
                    if skip == True:
                        skip = False
                    elif pair1 == False:
                        pair1 = True
                        skip = True
                    else:
                        pair2 = True
                else:
                    skip = False

                counter2 += 1

            if run == True and trick == False and pair2 == True:
                oupt = ''
                for x in numInpt:
                    oupt += chr(x + 96)

                return oupt

                break

            else:
                for x in range(7, 0, -1):
                    if numInpt[x] != 26:
                        numInpt[x] += 1
                        break
                    else:
                        numInpt[x] = 1

    #Part 1
    solution1 = solution(part1_input)

    #Part 2
    sol2_interate = []
    for char in solution1:
        number = ord(char) - 96
        sol2_interate.append(number)
    for x in range(7, 0, -1):
        if sol2_interate[x] != 26:
            sol2_interate[x] += 1
            break
        else:
            sol2_interate[x] = 1
    sol2_input = ''
    for x in sol2_interate:
        sol2_input += chr(x + 96)

    solution2 = solution(sol2_input)

    return solution1, solution2

#Day 12
def day12_2015(part1_input):
    import ast

    txt = part1_input.decode("utf-8") #the file reads in as a bytes (b') type - need to convert it to string type

    #Part 1
    lst = list(txt)
    counter = 0
    total = 0
    string = ''

    for x in lst:
        if ord(x) >= 48 and ord(x) <= 57:
            string = string + x
            if ord(lst[counter + 1]) >= 48 and ord(lst[counter + 1]) <= 57:
                pass
            else:
                num = int(string)
                total = total + num
                string = ''

        elif x == '-' and ord(lst[counter + 1]) >= 48 and ord(lst[counter + 1]) <= 57:
            string = string + x
        counter += 1

    solution1 = total

    #Part 2
    def loop(x, count, typ):
        valueX = 0
        level = count
        for a in x:
            if type(a) is dict:
                output = loop(a.values(), level + 1, 'd')
                valueX += output

            elif type(a) is list or type(a) is tuple:
                output = loop(a, level + 1, 'l')
                valueX += output

            else:
                if a == 'red' and typ == 'd':
                    valueX = 0
                    break
                elif a == 'red' and typ == 'l':
                    pass
                elif type(a) is int:
                    valueX += a

        return valueX

    solution2 = loop(ast.literal_eval(txt), 0, 'l') #ast.literal_eval reads the string representation of a list as an actual list

    return solution1, solution2

#Day 13
def day13_2015(part1_input):
    import itertools

    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter][-1] == '.':
            input_list += [' '.join(split_input[:(counter + 1)])]
            split_input = split_input[(counter + 1):]
            counter = 0
        else:
            counter += 1

    input_list_of_lists = []
    for line in input_list:
        input_list_of_lists += [line.split(' ')]

    guests = []
    for line in input_list_of_lists:
        # print(line)
        name = line[0]
        if name not in guests:
            guests += [name]

    register = {}
    for guest in guests:
        otherGuests = guests.copy()
        otherGuests.remove(guest)
        register[guest] = {}
        for otherGuest in otherGuests:
            for instruction in input_list_of_lists:
                if instruction[0] == guest and instruction[-1] == (otherGuest + '.'):
                    if instruction[2] == 'lose':
                        register[guest][otherGuest] = int('-' + instruction[3])
                    elif instruction[2] == 'gain':
                        register[guest][otherGuest] = int(instruction[3])
                    else:
                        print('Recognition error in ' + str(instruction))

    options = []
    fullOptions = []
    options = list(itertools.permutations(guests, len(guests)))
    for option in options:
        fullOptions += [option + (option[0],)]
    best_arrangement = []
    topScore = 0
    for option in fullOptions:
        counter = 0
        score = 0
        while counter <= len(guests) - 1:
            score += register[option[counter]][option[counter + 1]]
            score += register[option[counter + 1]][option[counter]]
            counter += 1
        if score >= topScore:
            topScore = score
            best_arrangement = option

    solution1 = topScore

    #Part 2
    for dic in register:
        register[dic]['Jono'] = 0
    register['Jono'] = {}
    for guest in guests:
        register['Jono'][guest] = 0
    guests.append('Jono')

    options = []
    fullOptions = []
    options = list(itertools.permutations(guests, len(guests)))
    for option in options:
        fullOptions += [option + (option[0],)]
    best_arrangement = []
    topScore = 0
    for option in fullOptions:
        counter = 0
        score = 0
        while counter <= len(guests) - 1:
            score += register[option[counter]][option[counter + 1]]
            score += register[option[counter + 1]][option[counter]]
            counter += 1
        if score >= topScore:
            topScore = score
            best_arrangement = option

    solution2 = topScore

    return solution1, solution2

#Day 14
def day14_2015(part1_input):
    import pandas as pd

    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter][-1] == '.':
            input_list += [' '.join(split_input[:(counter + 1)])]
            split_input = split_input[(counter + 1):]
            counter = 0
        else:
            counter += 1

    input_list_of_lists = []
    for line in input_list:
        input_list_of_lists += [line.split(' ')]

    data = pd.DataFrame()  # {'Name':[], 'Speed':[], 'Endurance':[], 'Rest':[]})

    for line in input_list_of_lists:
        data = data.append(
            {'Name': line[0], 'Speed': int(line[3]), 'Endurance': int(line[6]), 'Rest': int(line[-2])},
            ignore_index=True)

    timeStep = 2503

    for id, row in data.iterrows():

        cycles = timeStep // (data['Endurance'][id] + data['Rest'][id])
        finalDash = timeStep % (data['Endurance'][id] + data['Rest'][id])
        if finalDash <= data['Endurance'][id]:
            distance = (cycles * data['Endurance'][id] + finalDash) * data['Speed'][id]
        else:
            distance = (cycles + 1) * data['Endurance'][id] * data['Speed'][id]

        data.loc[id, "Distance"] = distance

    solution1 = str(int(max(data["Distance"])))

    #Part 2
    data2 = pd.DataFrame()  # {'Name':[], 'Speed':[], 'Endurance':[], 'Rest':[]})

    for line in input_list_of_lists:
        data2 = data.append(
            {'Name': line[0], 'Speed': int(line[3]), 'Endurance': int(line[6]), 'Rest': int(line[-2])},
            ignore_index=True)

    data['Points'] = pd.Series([0 for x in range(len(data.index))], index=data.index)

    for timeStep in range(1, 2504):

        for id, row in data.iterrows():
            cycles = timeStep // (data['Endurance'][id] + data['Rest'][id])
            finalDash = timeStep % (data['Endurance'][id] + data['Rest'][id])
            if finalDash <= data['Endurance'][id]:
                distance = (cycles * data['Endurance'][id] + finalDash) * data['Speed'][id]
            else:
                distance = (cycles + 1) * data['Endurance'][id] * data['Speed'][id]

            data.loc[id, "Distance"] = distance

        for id, row in data.iterrows():
            if data['Distance'][id] == max(data["Distance"]):
                data.loc[id, "Points"] += 1

        if timeStep % 500 == 0:
            print('Completed ' + str(timeStep) + ' seconds.')

    solution2 = max(data["Points"])

    return solution1, solution2

#Day 15
def day15_2015(part1_input):
    import pandas as pd
    import re

    split_input = part1_input.split()
    input_list = []
    counter = 1
    while counter < len(split_input):
        if split_input[counter][-1] == ':':
            input_list += [' '.join(split_input[:(counter)])]
            split_input = split_input[(counter):]
            counter = 0
        else:
            counter += 1

    input_list_of_lists = []
    for line in input_list:
        input_list_of_lists += [line.split(' ')]

    data = pd.DataFrame()
    for line in input_list_of_lists:
        data = data.append({'Name': line[0], 'Capacity': int(re.sub("[^\d\-]", "", line[2])),
                            'Durability': int(re.sub("[^\d\-]", "", line[4])),
                            'Flavor': int(re.sub("[^\d\-]", "", line[6])),
                            'Texture': int(re.sub("[^\d\-]", "", line[8])),
                            'Calories': int(re.sub("[^\d\-]", "", line[10]))}, ignore_index=True)

    ingredients = data['Name'].tolist()
    print(ingredients)

    recipe = {}
    for row in data['Name']:
        recipe[row] = 0
    print(recipe)

    data.set_index('Name', inplace=True, drop=True)
    print(data)

    def ingred(totalTeaspoons, index, recipe, topScore):
        spaceLeft = totalTeaspoons
        for x in range(0, index):
            spaceLeft -= recipe.get(ingredients[x])
        if index <= len(recipe) - 2:
            for n in range(0, spaceLeft + 1):
                recipe[ingredients[index]] = n
                index += 1
                index, recipe, topScore = ingred(index, recipe, topScore)
        else:
            recipe[ingredients[index]] = spaceLeft
            capacity = 0
            for x in range(len(ingredients)):
                capacity += data.at[ingredients[x], 'Capacity'] * recipe[ingredients[x]]
            durability = 0
            for x in range(len(ingredients)):
                durability += data.at[ingredients[x], 'Durability'] * recipe[ingredients[x]]
            flavor = 0
            for x in range(len(ingredients)):
                flavor += data.at[ingredients[x], 'Flavor'] * recipe[ingredients[x]]
            texture = 0
            for x in range(len(ingredients)):
                texture += data.at[ingredients[x], 'Texture'] * recipe[ingredients[x]]

            if capacity <= -1 or durability <= -1 or flavor <= -1 or texture <= -1:
                score = 0
            else:
                score = capacity * durability * flavor * texture

            if score >= topScore + 1:
                topScore = score

        index -= 1
        return index, recipe, topScore
    totalTeaspoons = 100
    solution1 = ingred(totalTeaspoons, 0, recipe, 0)[2]

    #Part 2
    def calor(totalTeaspoons, index, recipe, topScore):
        spaceLeft = totalTeaspoons
        for x in range(0, index):
            spaceLeft -= recipe.get(ingredients[x])
        if index <= len(recipe) - 2:
            for n in range(0, spaceLeft + 1):
                recipe[ingredients[index]] = n
                index += 1
                index, recipe, topScore = calor(index, recipe, topScore)

        else:
            recipe[ingredients[index]] = spaceLeft

            capacity = 0
            for x in range(len(ingredients)):
                capacity += data.at[ingredients[x], 'Capacity'] * recipe[ingredients[x]]
            durability = 0
            for x in range(len(ingredients)):
                durability += data.at[ingredients[x], 'Durability'] * recipe[ingredients[x]]
            flavor = 0
            for x in range(len(ingredients)):
                flavor += data.at[ingredients[x], 'Flavor'] * recipe[ingredients[x]]
            texture = 0
            for x in range(len(ingredients)):
                texture += data.at[ingredients[x], 'Texture'] * recipe[ingredients[x]]
            calories = 0
            for x in range(len(ingredients)):
                calories += data.at[ingredients[x], 'Calories'] * recipe[ingredients[x]]

            if capacity <= -1 or durability <= -1 or flavor <= -1 or texture <= -1:
                score = 0
            elif calories != 500:
                score = 0
            else:
                score = capacity * durability * flavor * texture
            if score >= topScore + 1:
                topScore = score

        index -= 1
        return index, recipe, topScore

        totalTeaspoons = 100
        solution2 = calor(totalTeaspoons, 0, recipe, 0)[2]

    return solution1, solution2

#Day 16
def day16_2015(part1_input):
    import pandas as pd

    split_input = part1_input.split()
    input_list = []
    counter = 1
    while counter < len(split_input):
        if split_input[counter] == 'Sue':
            input_list += [' '.join(split_input[:(counter)])]
            split_input = split_input[(counter):]
            counter = 1
        else:
            counter += 1

    input_list_of_dicts = []
    for row in input_list:
        input_list_of_dicts += [{row.split(' ')[i]: row.split(' ')[i + 1] for i in range(0, len(row.split(' ')), 2)}]

    criteria = ['Sue', 'children:', 'cats:', 'samoyeds:', 'pomeranians:', 'akitas:', 'vizslas:', 'goldfish:',
                'trees:', 'cars:', 'perfumes:']
    data = pd.DataFrame(columns=criteria)

    new_reg = dict.fromkeys(criteria)

    for entry in input_list_of_dicts:
        for item in entry:
            new_reg[item] = (entry.get(item)).strip(',')
        data = data.append(new_reg, ignore_index=True)
        new_reg = dict.fromkeys(criteria)

    data.set_index('Sue', inplace=True, drop=True)

    answer = {'Sue': 0, 'children:': 3, 'cats:': 7, 'samoyeds:': 2, 'pomeranians:': 3, 'akitas:': 0, 'vizslas:': 0,
              'goldfish:': 5, 'trees:': 3, 'cars:': 2, 'perfumes:': 1}

    for catagory in criteria[1:len(criteria)]:
        for entry in range(1, len(data) + 1):
            if data[catagory][str(entry) + ':'] != None and data[catagory][str(entry) + ':'] != str(
                    answer[catagory]):
                data.at[str(entry) + ':', catagory] = 'Wrong'

    for n in range(0, len(data)):
        if data.iloc[n].str.contains("Wrong").any() == False:
            solution1 = data.index[n:n+1].to_list()[0][:-1]

    #Part 2
    split_input = part1_input.split()
    input_list = []
    counter = 1
    while counter < len(split_input):
        if split_input[counter] == 'Sue':
            input_list += [' '.join(split_input[:(counter)])]
            split_input = split_input[(counter):]
            counter = 1
        else:
            counter += 1

    input_list_of_dicts = []
    for row in input_list:
        input_list_of_dicts += [{row.split(' ')[i]: row.split(' ')[i + 1] for i in range(0, len(row.split(' ')), 2)}]

    criteria = ['Sue', 'children:', 'cats:', 'samoyeds:', 'pomeranians:', 'akitas:', 'vizslas:', 'goldfish:',
                'trees:', 'cars:', 'perfumes:']
    data = pd.DataFrame(columns=criteria)

    new_reg = dict.fromkeys(criteria)

    for entry in input_list_of_dicts:
        for item in entry:
            new_reg[item] = (entry.get(item)).strip(',')
        data = data.append(new_reg, ignore_index=True)
        new_reg = dict.fromkeys(criteria)

    data.set_index('Sue', inplace=True, drop=True)

    answer = {'Sue': 0, 'children:': 3, 'cats:': 7, 'samoyeds:': 2, 'pomeranians:': 3, 'akitas:': 0, 'vizslas:': 0,
              'goldfish:': 5, 'trees:': 3, 'cars:': 2, 'perfumes:': 1}

    for catagory in criteria[1:len(criteria)]:
        if catagory == 'cats:' or catagory == 'trees:':
            for entry in range(1, len(data) + 1):
                if data[catagory][str(entry) + ':'] != None and data[catagory][str(entry) + ':'] <= str(
                        answer[catagory]):
                    data.at[str(entry) + ':', catagory] = 'Wrong'
        elif catagory == 'pomeranians:' or catagory == 'goldfish:':
            for entry in range(1, len(data) + 1):
                if data[catagory][str(entry) + ':'] != None and data[catagory][str(entry) + ':'] >= str(
                        answer[catagory]):
                    data.at[str(entry) + ':', catagory] = 'Wrong'
        else:
            for entry in range(1, len(data) + 1):
                if data[catagory][str(entry) + ':'] != None and data[catagory][str(entry) + ':'] != str(
                        answer[catagory]):
                    data.at[str(entry) + ':', catagory] = 'Wrong'

    for n in range(0, len(data)):
        if data.iloc[n].str.contains("Wrong").any() == False:
            solution2 = data.index[n:n+1].to_list()[0][:-1]

    return solution1, solution2

#Day 17
def day17_2015(part1_input):
    input_list = list(map(int, part1_input.split(' ')))
    containers = {}
    for n in range(len(input_list)):
        containers[chr(97 + n)] = sorted(input_list, reverse=True)[n]

    def jugFiller(containerDict, remainingDict, comboList, winningCombos):
        for n in range(len(remainingDict)):
            comboList.append(list(remainingDict.keys())[n])
            localTotal = 0
            for jug in comboList:
                localTotal += containerDict.get(jug, None)
            if localTotal == 150:
                winningCombos.append(comboList.copy())
            if localTotal >= 150:
                comboList.pop()
            else:
                remainingDict = containerDict.copy()
                for x in range(97, ord(comboList[-1]) + 1):
                    del remainingDict[chr(x)]
                winningCombos = jugFiller(containerDict, remainingDict, comboList, winningCombos)
                comboList.pop()
                remainingDict = containerDict.copy()
                if len(comboList) != 0:
                    for x in range(97, ord(comboList[-1]) + 1):
                        del remainingDict[chr(x)]
        return winningCombos

    remaining = containers.copy()
    combo = []
    winners = []
    totalWinners = jugFiller(containers, remaining, combo, winners)

    solution1 = len(totalWinners)

    #Part 2
    lengths = {}
    minLength = len(containers)
    for combo in totalWinners:
        if len(combo) <= minLength:
            minLength = len(combo)
    totalMin = 0
    for combo in totalWinners:
        if len(combo) <= minLength:
            totalMin += 1

    solution2 = totalMin

    return solution1, solution2

#Day 18
def day18_2015(part1_input):
    #Part 1
    grid_list = part1_input.split(' ')
    input_dict = {}
    for i in range(0, 100):
        input_dict[i] = {}

    for light_row in range(0,100):
        for light in range(0,100):
            if grid_list[light_row][light] == '#':
                input_dict[light_row][light] = 1
            elif grid_list[light_row][light] == '.':
                input_dict[light_row][light] = 0
            else:
                print('Unknown value in input!')

    def step(inpt, outpt):
        for row in range(0, 100):
            for column in range(0, 100):
                localTotal = 0
                for neighbourX in range(row - 1, row + 2):
                    for neighbourY in range(column - 1, column + 2):
                        if neighbourX != row or neighbourY != column:
                            try:
                                localTotal += inpt[neighbourX][neighbourY]
                            except:
                                pass
                if inpt[row][column] == 1:
                    if localTotal == 2 or localTotal == 3:
                        outpt[row][column] = 1
                    else:
                        outpt[row][column] = 0
                elif inpt[row][column] == 0:
                    if localTotal == 3:
                        outpt[row][column] = 1
                    else:
                        outpt[row][column] = 0
        return outpt

    outpt = {}
    for i in range(0, 100):
        outpt[i] = {}

    for turn in range(0, 100):
        outpt = step(input_dict, outpt)
        input_dict = outpt
        input_dict = outpt.copy()
        if turn == 99:
            total = 0
            for row in range(0, 100):
                total += sum(outpt[row].values())
            solution1 = total
        outpt = {}
        for i in range(0, 100):
            outpt[i] = {}

    #Part 2
    grid_list = part1_input.split(' ')
    input_dict = {}
    for i in range(0, 100):
        input_dict[i] = {}

    for light_row in range(0,100):
        for light in range(0,100):
            if grid_list[light_row][light] == '#':
                input_dict[light_row][light] = 1
            elif grid_list[light_row][light] == '.':
                input_dict[light_row][light] = 0
            else:
                print('Unknown value in input!')

    def step2(inpt, outpt):
        for row in range(0, 100):
            for column in range(0, 100):
                localTotal = 0
                for neighbour in range(row - 1, row + 2):
                    for cell in range(column - 1, column + 2):

                        if neighbour != row or cell != column:
                            try:
                                localTotal += inpt[neighbour][cell]
                            except:
                                pass
                if (row == 0 or row == 99) and (column == 0 or column == 99):
                    outpt[row][column] = 1
                elif inpt[row][column] == 1:
                    if localTotal == 2 or localTotal == 3:
                        outpt[row][column] = 1
                    else:
                        outpt[row][column] = 0
                elif inpt[row][column] == 0:
                    if localTotal == 3:
                        outpt[row][column] = 1
                    else:
                        outpt[row][column] = 0

        return outpt

    outpt = {}
    for i in range(0, 100):
        outpt[i] = {}
    for turn in range(0, 100):
        outpt = step2(input_dict, outpt)
        input_dict = outpt
        input_dict = outpt.copy()
        if turn == 99:
            total = 0
            for row in range(0, 100):
                total += sum(outpt[row].values())
            solution2 = total
        outpt = {}
        for i in range(0, 100):
            outpt[i] = {}

    return solution1, solution2

#Day 19
def day19_2015(part1_input, part2_input):

    medicine = part2_input
    medicineComponents = []
    for component in range(len(medicine)):
        if component != len(medicine) - 1:
            if medicine[component].isupper() == True and medicine[component + 1].isupper() == False:
                medicineComponents += [medicine[component:component + 2]]
            elif medicine[component].isupper() == True and medicine[component + 1].isupper() == True:
                medicineComponents += medicine[component]
            elif medicine[component] == 'e':
                medicineComponents += medicine[component]
        else:
            if medicine[component].isupper() == True:
                medicineComponents += medicine[component]
            elif medicine[component] == 'e':
                medicineComponents += medicine[component]

    #Part 1
    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter] == '=>':
            input_list += [' '.join(split_input[:(counter + 2)])]
            split_input = split_input[(counter + 2):]
            counter = 0
        else:
            counter += 1

    molecules = []
    for replacement in input_list:
        if replacement[1] == ' ':
            molecules += replacement[0]
        else:
            molecules += [replacement[0:2]]
    molecules = sorted(set(molecules))

    instructions = {}
    for molecule in molecules:
        instructions[molecule] = []

    for replacement in input_list:
        instructions[replacement.split()[0]] += [replacement.split()[2]]

    previousCombos = []
    uniqueCombos = 0
    for component in range(len(medicineComponents)):
        if medicineComponents[component] in molecules:
            newCombos = []
            newCombo = medicineComponents.copy()
            for replacement in instructions[medicineComponents[component]]:
                newCombo[component] = replacement
                comboString = ''.join(str(i) for i in newCombo)
                if comboString not in previousCombos:
                    uniqueCombos += 1
                newCombos += [comboString]
            previousCombos = newCombos
    solution1 = uniqueCombos

    #Part 2
    resultants = {}
    for replacement in input_list:
        resultants[replacement.split(' ')[2]] = replacement.split(' ')[0]

    def check(medicine, swaps):
        skip = 0
        for step in range(len(medicine)):
            if skip >= 1:
                skip -= 1
            # Checks if it can be created from another molecule (is it a resultant) and if so switch it
            for resultant in resultants:
                if len(medicine) - step >= len(resultant):
                    if medicine[step:step + len(resultant)] == resultant:
                        medicine = medicine[0:step] + resultants[resultant] + medicine[step + len(resultant):]
                        # If the length of the new molecule is shorter than the original, skip the difference in steps
                        skip += len(resultants[resultant]) - len(medicine[step:step + len(resultant)])
                        swaps += 1
        return medicine, swaps

    medicine = part2_input
    swaps = 0
    allE = False

    while allE == False:  # for n in range(1):
        medicine, swaps = check(medicine, swaps)
        nonE = 0
        for letter in medicine:
            if letter != 'e':
                nonE += 1
        if nonE == 0:
            allE = True

    solution2 = swaps

    return solution1, solution2

#Day 20
def day20_2015(part1_input):
#Part 1
    from math import sqrt
    answer = 36000000
    house = 1
    presents = 0
    elves = []

    while presents <= answer:
        for elf in range(1, int(sqrt(house)) + 1):
            if house % elf == 0:
                elves += elf, int(house / elf)
        elves = list(set(elves))
        presents = sum(elves) * 10
        if presents >= answer:
            solution1 = house
        else:
            if house % 100000 == 0:
                print('House', house, 'gets', presents, 'presents.')
            house += 1
            presents = 0
            elves = []

#Part 2
    from math import sqrt
    answer = 36000000
    house = 1
    presents = 0
    elves = []
    visits = {}

    while presents <= answer:
        for elf in range(1, int(sqrt(house)) + 1):
            if house % elf == 0:
                if elf not in visits or visits[elf] <= 49:
                    elves.append(elf)
                    if elf not in visits:
                        visits[elf] = 1
                    else:
                        visits[elf] += 1
                if int(house / elf) not in visits or visits[int(house / elf)] <= 49 and house != elf:
                    elves.append(int(house / elf))
                    if int(house / elf) not in visits:
                        visits[int(house / elf)] = 1
                    else:
                        visits[int(house / elf)] += 1
        elves = list(set(elves))
        presents = sum(elves) * 11
        if presents >= answer:
            solution2 = house
        else:
            if house % 100000 == 0:
                print('House', house, 'gets', presents, 'presents.')
            house += 1
            presents = 0
            elves = []

    return solution1, solution2;

#Day 21
def day21_2015(part1_input):
    import pandas as pd
    import itertools

    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter][-1] == ':':
            input_list += [' '.join(split_input[(counter + 1):(counter + 2)])]
            split_input = split_input[(counter + 2):]
            counter = 0
        else:
            counter += 1

    weaponsIn = {'Name': ['Dagger', 'Shortsword', 'Warhammer', 'Longsword', 'Greataxe'],
                 'Cost': [8, 10, 25, 40, 74], 'Damage': [4, 5, 6, 7, 8], 'Defense': [0, 0, 0, 0, 0]}
    weapons = pd.DataFrame(data=weaponsIn)

    armorsIn = {'Name': ['Empty', 'Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail'],
                'Cost': [0, 13, 31, 53, 75, 102], 'Damage': [0, 0, 0, 0, 0, 0], 'Defense': [0, 1, 2, 3, 4, 5]}
    armors = pd.DataFrame(data=armorsIn)

    ringsIn = {
        'Name': ['Empty', 'Empty', 'Damage+1', 'Damage+2', 'Damage+3', 'Defense+1', 'Defense+2', 'Defense+3'],
        'Cost': [0, 0, 25, 50, 100, 20, 40, 80], 'Damage': [0, 0, 1, 2, 3, 0, 0, 0],
        'Defense': [0, 0, 0, 0, 0, 1, 2, 3]}
    rings = pd.DataFrame(data=ringsIn)

    Boss = {'HP': int(input_list[0]), 'Damage': int(input_list[1]), 'Defense': int(input_list[2])}
    Jono = {'HP': 100, 'Damage': 0, 'Defense': 0}

    pairsIn = {}
    counter = 0
    for pair in itertools.combinations(rings.index, 2):
        pairsIn[counter] = [pair[0], pair[1], rings.at[pair[0], 'Cost'] + rings.at[pair[1], 'Cost'],
                            rings.at[pair[0], 'Damage'] + rings.at[pair[1], 'Damage'],
                            rings.at[pair[0], 'Defense'] + rings.at[pair[1], 'Defense']]
        counter += 1
    pairs = pd.DataFrame(data=pairsIn, index=['Ring 1', 'Ring 2', 'Cost', 'Damage', 'Defense']).T.sort_values(
        by=['Cost']).reset_index()
    del pairs['index']

    shop = []
    shop += list(weapons.index), list(armors.index), list(pairs.index)
    inventories = []
    for x in list(itertools.product(*shop)):
        totalCost = 0
        totalCost = weapons['Cost'][x[0]] + armors['Cost'][x[1]] + pairs['Cost'][x[2]]
        inventories += [[totalCost, x[0], x[1], x[2]]]
    inventories.sort(key=lambda x: x[0])

    win = False
    loss = False
    for inventory in inventories:
        if win == True:
            break
        else:
            Jono['HP'] = 100
            Boss['HP'] = int(input_list[0])
            loss = False
        Jono['Damage'] = weapons['Damage'][inventory[1]] + pairs['Damage'][inventory[3]]
        Jono['Defense'] = armors['Defense'][inventory[2]] + pairs['Defense'][inventory[3]]
        while win == False and loss == False:
            if Jono['Damage'] - Boss['Defense'] >= 1:
                Boss['HP'] -= Jono['Damage'] - Boss['Defense']
            else:
                Boss['HP'] -= 1
            if Boss['HP'] <= 0:
                win = True
                winningSet = [weapons['Name'][inventory[1]], armors['Name'][inventory[2]],
                              rings['Name'][pairs['Ring 1'][inventory[3]]],
                              rings['Name'][pairs['Ring 2'][inventory[3]]]]
                solution1 = inventory[0]
                break
            elif Boss['Damage'] - Jono['Defense'] >= 1:
                Jono['HP'] -= Boss['Damage'] - Jono['Defense']
            else:
                Jono['HP'] -= 1
            if Jono['HP'] <= 0:
                loss = True

    #Part 2

    inventories = []
    for x in list(itertools.product(*shop)):
        totalCost = 0
        totalCost = weapons['Cost'][x[0]] + armors['Cost'][x[1]] + pairs['Cost'][x[2]]
        inventories += [[totalCost, x[0], x[1], x[2]]]
    inventories.sort(key=lambda x: x[0], reverse=True)

    win = False
    loss = False
    for inventory in inventories:
        if loss == True:
            break
        else:
            Jono['HP'] = 100
            Boss['HP'] = int(input_list[0])
            win = False
        Jono['Damage'] = weapons['Damage'][inventory[1]] + pairs['Damage'][inventory[3]]
        Jono['Defense'] = armors['Defense'][inventory[2]] + pairs['Defense'][inventory[3]]
        while win == False and loss == False:
            if Jono['Damage'] - Boss['Defense'] >= 1:
                Boss['HP'] -= Jono['Damage'] - Boss['Defense']
            else:
                Boss['HP'] -= 1
            if Boss['HP'] <= 0:
                win = True
                winningSet = [weapons['Name'][inventory[1]], armors['Name'][inventory[2]],
                              rings['Name'][pairs['Ring 1'][inventory[3]]],
                              rings['Name'][pairs['Ring 2'][inventory[3]]]]
            elif Boss['Damage'] - Jono['Defense'] >= 1:
                Jono['HP'] -= Boss['Damage'] - Jono['Defense']
            else:
                Jono['HP'] -= 1
            if Jono['HP'] <= 0:
                loss = True
                losingSet = [weapons['Name'][inventory[1]], armors['Name'][inventory[2]],
                             rings['Name'][pairs['Ring 1'][inventory[3]]],
                             rings['Name'][pairs['Ring 2'][inventory[3]]]]
                solution2 = inventory[0]

    return solution1, solution2

#Day 22
def day22_2015(part1_input):
    split_input = part1_input.split()
    input_list = []
    counter = 0
    while counter < len(split_input):
        if split_input[counter][-1] == ':':
            input_list += [' '.join(split_input[(counter + 1):(counter + 2)])]
            split_input = split_input[(counter + 2):]
            counter = 0
        else:
            counter += 1

    bossStats = {'HP': int(input_list[0]), 'Damage': int(input_list[1])}
    jonoStats = {'HP': 50, 'Mana': 500}

    def newRound(oldSequences, topScore):
        newSequences = {}
        for sequence in oldSequences:
            newSequence = ''
            if manaLeft(sequence, bossStats, jonoStats) >= 53:
                newSequences, topScore = newSpell(sequence, bossStats, jonoStats, 'm', topScore, newSequences)
            if manaLeft(sequence, bossStats, jonoStats) >= 73:
                newSequences, topScore = newSpell(sequence, bossStats, jonoStats, 'd', topScore, newSequences)
            if manaLeft(sequence, bossStats, jonoStats) >= 113 and 's' not in sequence[-2:]:
                newSequences, topScore = newSpell(sequence, bossStats, jonoStats, 's', topScore, newSequences)
            if manaLeft(sequence, bossStats, jonoStats) >= 173 and 'p' not in sequence[-2:]:
                newSequences, topScore = newSpell(sequence, bossStats, jonoStats, 'p', topScore, newSequences)
            if manaLeft(sequence, bossStats, jonoStats) >= 229 and 'r' not in sequence[-2:]:
                newSequences, topScore = newSpell(sequence, bossStats, jonoStats, 'r', topScore, newSequences)
        return newSequences, topScore

    def manaLeft(sequence, bossStats, jonoStats):
        mana = jonoStats['Mana']
        for attack in sequence:
            if attack == 'm':
                mana -= 53
            elif attack == 'd':
                mana -= 73
            elif attack == 's':
                mana -= 113
            elif attack == 'p':
                mana -= 173
            elif attack == 'r':
                mana -= 229
        if sequence[-1] == 'r':
            mana += ((sequence[:-1].count('r')) * 505 + 101)
        elif len(sequence) >= 2 and sequence[-2] == 'r':
            mana += ((sequence[:-2].count('r')) * 505 + 303)
        else:
            mana += ((sequence.count('r')) * 505)
        return mana

    def newSpell(sequence, bossStats, jonoStats, spell, topScore, newSequences):
        newSequence = sequence + spell
        if winCheck(newSequence, bossStats, jonoStats) == True and manaUsed(newSequence, bossStats,
                                                                            jonoStats) <= topScore:
            topScore = manaUsed(newSequence, bossStats, jonoStats)
        elif deadCheck(newSequence, bossStats, jonoStats) == True:
            pass
        elif manaUsed(newSequence, bossStats, jonoStats) <= topScore:
            newSequences[newSequence] = manaUsed(newSequence, bossStats, jonoStats)
        return newSequences, topScore

    def winCheck(sequence, bossStats, jonoStats):
        win = False
        if sequence[-1] == 'p':
            if sequence.count('m') * 4 + sequence.count('d') * 2 + sequence.count('p') * 18 - 15 >= bossStats['HP']:
                win = True
        elif len(sequence) >= 2 and sequence[-2] == 'p':
            if sequence.count('m') * 4 + sequence.count('d') * 2 + sequence.count('p') * 18 - 9 >= bossStats['HP']:
                win = True
        elif len(sequence) >= 3 and sequence[-3] == 'p':
            if sequence.count('m') * 4 + sequence.count('d') * 2 + sequence.count('p') * 18 - 3 >= bossStats['HP']:
                win = True
        else:
            if sequence.count('m') * 4 + sequence.count('d') * 2 + sequence.count('p') * 18 >= bossStats['HP']:
                win = True
        return win

    def deadCheck(sequence, bossStats, jonoStats):
        dead = False
        if sequence[-1] == 's':
            if ((sequence[:-1].count('s')) * 3 + 1) * (bossStats['Damage'] - 7) + (
                    len(sequence) - ((sequence[:-1].count('s')) * 3 + 1)) * bossStats['Damage'] - sequence.count(
                    'd') * 2 >= jonoStats['HP']:
                dead = True
        elif len(sequence) >= 2 and sequence[-2] == 's':
            if ((sequence[:-2].count('s')) * 3 + 2) * (bossStats['Damage'] - 7) + (
                    len(sequence) - ((sequence[:-2].count('s')) * 3 + 2)) * bossStats['Damage'] - sequence.count(
                    'd') * 2 >= jonoStats['HP']:
                dead = True
        else:
            if ((sequence.count('s')) * 3) * (bossStats['Damage'] - 7) + (
                    len(sequence) - (sequence.count('s')) * 3) * bossStats['Damage'] - sequence.count('d') * 2 >= \
                    jonoStats['HP']:
                dead = True
        return dead

    def manaUsed(sequence, bossStats, jonoStats):
        mana = 0
        for attack in sequence:
            if attack == 'm':
                mana += 53
            elif attack == 'd':
                mana += 73
            elif attack == 's':
                mana += 113
            elif attack == 'p':
                mana += 173
            elif attack == 'r':
                mana += 229
        return mana

    attackSequences = {'m': 53, 'd': 73, 's': 113, 'p': 173, 'r': 229}
    topScore = 10000
    counter = 0

    while len(attackSequences) >= 1:
        counter += 1
        attackSequences, topScore = newRound(attackSequences, topScore)
        solution1 = topScore

    bossStats = {'HP': int(input_list[0]), 'Damage': int(input_list[1]) + 1}
    jonoStats = {'HP': 49, 'Mana': 500}

    attackSequences = {'m': 53, 'd': 73, 's': 113, 'p': 173, 'r': 229}
    topScore = 10000
    counter = 0

    while len(attackSequences) >= 1:
        counter += 1
        attackSequences, topScore = newRound(attackSequences, topScore)
        solution2 = topScore

    return solution1, solution2

#Day 23
def day23_2015(part1_input):
    split_input = part1_input.split()
    input_list = []
    while len(split_input) > 0:
        if split_input[1][-1] == ',':
            input_list += [split_input[:3]]
            split_input = split_input[3:]
        else:
            input_list += [split_input[:2]]
            split_input = split_input[2:]

    def solver(regA, regB, inpt):
        step = 0
        while step <= len(inpt) - 1:
            if inpt[step][0] == 'hlf':
                if inpt[step][1] == 'a':
                    regA = int(regA / 2)
                else:
                    regB = int(regB / 2)
                step += 1
            elif inpt[step][0] == 'tpl':
                if inpt[step][1] == 'a':
                    regA = regA * 3
                else:
                    regB = regB * 3
                step += 1
            elif inpt[step][0] == 'inc':
                if inpt[step][1] == 'a':
                    regA += 1
                else:
                    regB += 1
                step += 1
            elif inpt[step][0] == 'jmp':
                if inpt[step][1][1:] == '0':
                    print('Jump 0 creates an infinate loop!')
                    break
                if inpt[step][1][0] == '+':
                    step += int(inpt[step][1][1:])
                elif inpt[step][1][0] == '-':
                    step -= int(inpt[step][1][1:])
                else:
                    print('No +/- sign for jump step.')
            elif inpt[step][0] == 'jie':
                if 'a' in inpt[step][1] and regA % 2 == 0:
                    if inpt[step][1][1:] == '0':
                        # To avoid an infinate loop, write a break clause for 'jump 0'
                        print('Jump 0 creates an infinate loop!')
                        break
                    elif inpt[step][2][0] == '+':
                        step += int(inpt[step][2][1:])
                    elif inpt[step][2][0] == '-':
                        step -= int(inpt[step][2][1:])
                    else:
                        print('No +/- sign for jump step.')
                        break
                elif 'b' in inpt[step][1] and regB % 2 == 0:
                    if inpt[step][1][1:] == '0':
                        print('Jump 0 creates an infinate loop!')
                        break
                    elif inpt[step][2][0] == '+':
                        step += int(inpt[step][2][1:])
                    elif inpt[step][2][0] == '-':
                        step -= int(inpt[step][2][1:])
                    else:
                        print('No +/- sign for jump step.')
                        break
                else:
                    step += 1
            elif inpt[step][0] == 'jio':
                if 'a' in inpt[step][1] and regA == 1:
                    if inpt[step][1][1:] == '0':
                        print('Jump 0 creates an infinate loop!')
                        break
                    if inpt[step][2][0] == '+':
                        step += int(inpt[step][2][1:])
                    elif inpt[step][2][0] == '-':
                        step -= int(inpt[step][2][1:])
                    else:
                        print('No +/- sign for jump step.')
                        break
                elif 'b' in inpt[step][1] and regB == 1:
                    if inpt[step][1][1:] == '0':
                        print('Jump 0 creates an infinate loop!')
                        break
                    if inpt[step][2][0] == '+':
                        step += int(inpt[step][2][1:])
                    elif inpt[step][2][0] == '-':
                        step -= int(inpt[step][2][1:])
                    else:
                        print('No +/- sign for jump step.')
                        break
                else:
                    step += 1

        return regB

    solution1 = solver(int(0), int(0), input_list)
    solution2 = solver(int(1), int(0), input_list)

    return solution1, solution2

#Day 24
def day24_2015(part1_input):
    import math
    split_input = part1_input.split()
    input_list = []
    while len(split_input) > 0:
        input_list += [int(split_input[0])]
        split_input = split_input[1:]

    groupWeight = sum(input_list) / 3

    def addPackage(group, remainingPackages, groupWeight, winner):
        for package in remainingPackages:
            newGroup1 = group + [package]
            if sum(newGroup1) == groupWeight:
                if winner['Group'] == [] or len(newGroup1) <= len(winner['Group']) - 1:
                    winner['Group'] = newGroup1
                    winner['Entanglement'] = math.prod(newGroup1)
                elif len(newGroup1) == len(winner['Group']):
                    if math.prod(newGroup1) <= winner['Entanglement']:
                        winner['Group'] = newGroup1
                        winner['Entanglement'] = math.prod(newGroup1)
            elif sum(newGroup1) <= groupWeight and (winner['Group'] == [] or len(newGroup1) <= len(winner[
                                                                                                       'Group']) - 1):  # can do -2, because if the subgroup is within 1 of the winning one, any subsequent combos will enherently have a greater product
                packagesLeft = remainingPackages[remainingPackages.index(package) + 1:]
                winner = addPackage(newGroup1, packagesLeft, groupWeight, winner)
        return winner

    winner = {'Group': [], 'Entanglement': 0}
    startingGroup = []
    winner = addPackage(startingGroup, input_list, groupWeight, winner)
    solution1 = winner['Entanglement']

    groupWeight = sum(input_list) / 4
    winner = {'Group': [], 'Entanglement': 0}
    startingGroup = []
    winner = addPackage(startingGroup, input_list, groupWeight, winner)
    solution2 = winner['Entanglement']

    return solution1, solution2

#Day 25
def day25_2015(part1_input, part2_input):
    seqPosition = 1
    columnRef = 1
    rowRef = 1
    while columnRef != int(part2_input) or rowRef != int(part1_input):
        if rowRef == 1:
            rowRef = columnRef + 1
            columnRef = 1
            seqPosition += 1
        else:
            columnRef += 1
            rowRef -= 1
            seqPosition += 1

    initialCode = 20151125

    def nextCode(inputCode):
        outputCode = (inputCode * 252533) % 33554393
        return outputCode

    code = initialCode
    for x in range(seqPosition - 1):
        code = nextCode(code)
        if x % 1000000 == 0:
            print('Processing code', x)

    solution1 = code
    solution2 = 'This star is for freeeee!'

    return solution1, solution2