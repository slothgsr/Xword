from itertools import combinations
import time

def wordfinder(arg1, arg2): #arg1 = combo,  arg2 = setlist
    words = 0
    for word in arg2: # for each word in setlist
        candidate = True
        for letter in word:
            if letter in arg1:
                candidate = False
                break
        if candidate == True:
            words += 1
    return words


#timer start
tic = time.perf_counter()

# creating 8 letter combinations
combos = set(combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8))

# Words from each grid,  Need to automate this with OCR!!
Grid1 = ['adore', 'once', 'deer', 'dark', 'allocate', 'sweater', 'air', 'ininite', 'oven', 'fence', 'always',\
         'ahoy', 'oval', 'ear', 'ink', 'education', 'rlief', 'order', 'taxi', 'ram', 'elk', 'breeze']

Grid2 = ['ocen', 'amid', 'fragment', 'pie', 'essence', 'atlantic', 'flag', 'else', 'girl', 'range', 'office',\
         'fog', 'owl', 'ahe', 'bagel', 'nimble', 'newspaper', 'rat', 'pen', 'town', 'idle', 'escape']

Grid3 = ['assume', 'syrup', 'big', 'den', 'cheese', 'zinc', 'spy', 'ridge', 'expense']

# word list with duplicates removed
Grid1set = ["".join(set(x)) for x in Grid1]
Grid2set = ["".join(set(x)) for x in Grid2]
Grid3set = ["".join(set(x)) for x in Grid3]

win = 0
lose = 0
board1win = 0
board2win = 0
win300000 = 0
win30000 = 0
win10000 = 0
win1000 = 0
win500 = 0
win400 = 0
win200 = 0
win100 = 0
win50 = 0
win40 = 0
win20 = 0
win10 = 0
bonuswin = 0
wintoomuch = 0

for i in combos:
    combowinammount = 0
    combowin = 0
    combolose = 0
    count = wordfinder(i, Grid1set)

    if count < 2:
        combolose += 1
    elif count == 2:
        win10 += 1
        combowin += 1
        combowinammount += 10
        board1win += 1
    elif count == 3:
        win20 += 1
        combowin += 1
        combowinammount += 20
        board1win += 1
    elif count == 4:
        win40 += 1
        combowin += 1
        combowinammount += 40
        board1win += 1
    elif count == 5:
        win100 += 1
        combowin += 1
        combowinammount += 100
        board1win += 1
    elif count == 6:
        win200 += 1
        combowin += 1
        combowinammount += 200
        board1win += 1
    elif count == 7:
        win400 += 1
        combowin += 1
        combowinammount += 400
        board1win += 1
    elif count == 8:
        win1000 += 1
        combowin += 1
        combowinammount += 1000
        board1win += 1
    elif count == 9:
        win10000 += 1
        combowin += 1
        combowinammount += 10000
        board1win += 1
    elif count >= 10:
        win30000 += 1
        combowin += 1
        combowinammount += 30000
        board1win += 1

    count = wordfinder(i, Grid2set)
    if count < 2:
        combolose += 1
    elif count == 2:
        win10 += 1
        combowin += 1
        combowinammount += 10
        board2win += 1
    elif count == 3:
        win20 += 1
        combowin += 1
        combowinammount += 20
        board2win += 1
    elif count == 4:
        win50 += 1
        combowin += 1
        combowinammount += 50
        board2win += 1
    elif count == 5:
        win100 += 1
        combowin += 1
        combowinammount += 100
        board2win += 1
    elif count == 6:
        win500 += 1
        combowin += 1
        combowinammount += 500
        board2win += 1
    elif count == 7:
        win1000 += 1
        combowin += 1
        combowinammount += 1000
        board2win += 1
    elif count == 8:
        win10000 += 1
        combowin += 1
        combowinammount += 10000
        board2win += 1
    elif count == 9:
        win30000 += 1
        combowin += 1
        combowinammount += 30000
        board2win += 1
    elif count >= 10:
        win300000 += 1
        combowin += 1
        combowinammount += 300000
        board2win += 1

    count = wordfinder(i, Grid3set)
    if count < 2:
        combolose += 1
    elif count == 2:
        win10 += 1
        combowin += 1
        combowinammount += 10
        board2win += 1
    elif count == 3:
        win20 += 1
        combowin += 1
        combowinammount += 20
        board2win += 1
    elif count == 4:
        win50 += 1
        combowin += 1
        combowinammount += 50
        board2win += 1
    elif count >= 5:
        win100 += 1
        combowin += 1
        combowinammount += 100
        board2win += 1
    if combowin >= 1:
        win += 1
    else:
        lose += 1
    if combowinammount > 300000:
        wintoomuch += 1



print()
print("Grid1 = " + str(Grid1))
print()
print("Grid2 = " + str(Grid2))
print()
print("Grid3 = " + str(Grid3))
print()
print("Total combos checked " + str(len(combos)))
print("$10 wins = " + str(win10))
print("$20 wins = " + str(win20))
print("$40 wins = " + str(win40))
print("$50 wins = " + str(win50))
print("$100 wins = " + str(win100))
print("$200 wins = " + str(win200))
print("$400 wins = " + str(win400))
print("$500 wins = " + str(win500))
print("$1000 wins = " + str(win1000))
print("$10000 wins = " + str(win10000))
print("$30000 wins = " + str(win30000))
print("$300000 wins = " + str(win300000))
print("board1 wins = " + str(board1win))
print("board2 wins = " + str(board2win))
print("winning combos =" + str(win - wintoomuch))
print("losing combos = " + str(lose + wintoomuch))
print("won too much = " + str(wintoomuch))

toc = time.perf_counter()

print(f'Elapsed time : {toc - tic:0.4f} seconds')