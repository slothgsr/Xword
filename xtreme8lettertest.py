from itertools import combinations
import time

#timer start
tic = time.perf_counter()

combos = set(combinations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],8))

print(len(combos))

# Testing combos
# combos = [('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 't', 'u', 'v', 'w'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'r', 't', 'v', 'w', 'z'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 't', 'u', 'w', 'x', 'y', 'z'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'o', 'p', 'v', 'w', 'x', 'y'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'n', 'o', 'q', 's', 'u', 'v', 'w'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'o', 'q', 't', 'u', 'v', 'w', 'x'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'q', 'r', 't', 'u', 'z'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'q', 'r', 'u', 'v', 'x', 'z'),
#           ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'n', 'r', 's', 't', 'u', 'y', 'z')]

# words entered from first crossword
# needs to match 2 words for win
Grid1 = ['bridge', 'date', 'atom', 'pry', 'rib', 'substance', 'napkin', 'stack', 'mode', 'nut', 'mat',
         'vesel', 'brass', 'swim', 'unit', 'aunt', 'domestic', 'explain', 'day', 'reckless', 'taxi', 'nsal']

# words entered from second crossword
# needs to match 2 words for win
Grid2 = ['dress', 'iron', 'diagonal', 'ear', 'fatigue', 'dimnish', 'axle', 'rack', 'entry', 'else', 'aide',
         'fiddle', 'rot', 'most', 'end', 'imaginary', 'degre', 'shake', 'nice', 'owl', 'salary', 'eye']

# words entered from third crossword
# needs to match 2 words for win
Grid3 = ['list', 'sum', 'express', 'dodge', 'own', 'legend', 'pod', 'stereo', 'amuse']

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
win30 = 0
win20 = 0
win10 = 0
bonuswin = 0
wintoomuch = 0



# takes 64 seconds
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


# percentage complete display
percent = 0
test = 0
percent1= int(len(combos)/100)
percent100list=[]
for i in range(100):
    percent100list.append(i * percent1)

for i in combos:
    if test in percent100list: # Progress bar
        percent += 1
        test += 1
        print(f'Computing: {percent}% finished', end='\r')
    test += 1

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
print("Total combos checked " + str(len(combos)))
print("$10 wins = " + str(win10))
print("$20 wins = " + str(win20))
print("$30 wins = " + str(win30))
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