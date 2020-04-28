''' Skip the unused letters while in wordfinder'''
# started with copy of MultixUnused
#TODO  find missing letters in each grid, add argument to wordfinder  if grid = 2 omit unused grid2
# finished..  Saved 1 sec  :(

from itertools import combinations
import time
import string

#timer start
tic = time.perf_counter()

def wordfinder(combo, gridlist, unused):
    counts=[]
    x = 0
    for grid in gridlist:   
        for letter in combo:
            if len(grid) <=1:
                break
            if letter in unused[x]:
                continue
            remove = []
            for word in grid:
                if letter in word:
                    remove.append(word)             
            for i in remove:
                grid.remove(i)
        counts.append(len(grid))
        x += 1
    return counts   


def checker():
    global combos
    alph = 'abcdefghijklmnopqrstuvwxyz'
    checker = input("enter your letters: ")
    combo = ''
    for i in alph:
        if i in checker:
            continue
        else:
            combo += i
    combos = tuple([combo])
    print(combos)
    return combos


def unused_generator(Gridlist):
    letterdic = dict.fromkeys(string.ascii_lowercase, 0)
    unused = []
    for grid in Gridlist:
        for word in grid:
            for letter in word:
                if letter in letterdic:
                    letterdic[letter] += 1
                else:
                    letterdic[letter] = 1
        unused.append(set([k for k,v in letterdic.items() if v == 0]))
    return unused


# 48.22,48.93
combos = set(combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8))


# question = input("would you like to check your ticet?")
# if question.lower() == "y" or question.lower() == "yes":
#     checker()

Grid1 = ['timid', 'aside', 'substance', 'sign', 'oxen', 'able', 'one', 'afar', 'lap', 'kennel', 'else', 'oil', 
        'layout', 'sabotage', 'mob', 'snorkel', 'dot', 'argue', 'undo', 'sock', 'ballot', 'pineapple']

# ords entered from second crossword
# needs to match 2 words for win
Grid2 = ['chef', 'haze', 'tweezers', 'once', 'astute', 'east', 'forecast', 'circus', 'iris', 'salute', 'gate', 
        'traffic', 'how', 'eat', 'rural', 'fee', 'use', 'court', 'here', 'something', 'epic', 'splint']
         
Grid1set = ["".join(set(x)) for x in Grid1]
Grid2set = ["".join(set(x)) for x in Grid2]

Gridlist = [Grid1set,Grid2set]


unused = unused_generator(Gridlist)
print(unused)

win = 0
lose = 0
board1win = 0
board2win = 0
win100000 = 0
win10000 = 0
win1000 = 0
win500 = 0
win400 = 0
win200 = 0
win100 = 0
win60 = 0
win50 = 0
win40 = 0
win25 = 0
win20 = 0
win15 = 0
win10 = 0
win5 = 0

bonuswin = 0
wintoomuch = 0

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
    
    Gridlist= [Grid1set[:],Grid2set[:]]
    count = wordfinder(i, Gridlist,unused)



    if count[0] < 2:
        combolose += 1
    elif count[0] == 2:
        win5 += 1
        combowin += 1
        combowinammount += 5
        board1win += 1
    elif count[0] == 3:
        win10 += 1
        combowin += 1
        combowinammount += 10
        board1win += 1
    elif count[0] == 4:
        win20 += 1
        combowin += 1
        combowinammount += 20
        board1win += 1
    elif count[0] == 5:
        win40 += 1
        combowin += 1
        combowinammount += 40
        board1win += 1
    elif count[0] == 6:
        win60 += 1
        combowin += 1
        combowinammount += 60
        board1win += 1
    elif count[0] == 7:
        win200 += 1
        combowin += 1
        combowinammount += 200
        board1win += 1
    elif count[0] == 8:
        win400 += 1
        combowin += 1
        combowinammount += 400
        board1win += 1
    elif count[0] == 9:
        win1000 += 1
        combowin += 1
        combowinammount += 1000
        board1win += 1
    elif count[0] >= 10:
        win10000 += 1
        combowin += 1
        combowinammount += 10000
        board1win += 1
    

   
    if count[1] < 2:
        combolose += 1
    elif count[1] == 2:
        win5 += 1
        combowin += 1
        combowinammount += 5
        board2win += 1
    elif count[1] == 3:
        win15 += 1
        combowin += 1
        combowinammount += 15
        board2win += 1
    elif count[1] == 4:
        win25 += 1
        combowin += 1
        combowinammount += 25
        board2win += 1
    elif count[1] == 5:
        win50 += 1
        combowin += 1
        combowinammount += 50
        board2win += 1
    elif count[1] == 6:
        win100 += 1
        combowin += 1
        combowinammount += 100
        board2win += 1
    elif count[1] == 7:
        win500 += 1
        combowin += 1
        combowinammount += 500
        board2win += 1
    elif count[1] == 8:
        win1000 += 1
        combowin += 1
        combowinammount += 1000
        board2win += 1
    elif count[1] == 9:
        win10000 += 1
        combowin += 1
        combowinammount += 10000
        board2win += 1
    elif count[1] >= 10:
        win100000 += 1
        combowin += 1
        combowinammount += 100000
        board2win += 1

    if combowin >= 1:
        win += 1
    else:
        lose += 1
    if combowinammount > 100000:
        wintoomuch += 1



print()
print("Total combos checked " + str(len(combos)))
print("$5 wins = " + str(win5))
print("$10 wins = " + str(win10))
print("$15 wins = " + str(win15))
print("$20 wins = " + str(win20))
print("$25 wins = " + str(win25))
print("$40 wins = " + str(win40))
print("$50 wins = " + str(win50))
print("$60 wins = " + str(win60))
print("$100 wins = " + str(win100))
print("$200 wins = " + str(win200))
print("$400 wins = " + str(win400))
print("$500 wins = " + str(win500))
print("$1000 wins = " + str(win1000))
print("$10000 wins = " + str(win10000))
print("$100000 wins = " + str(win100000))
print("board1 wins = " + str(board1win))
print("board2 wins = " + str(board2win))
print("winning combos = " + str(win - wintoomuch))
print("losing combos = " + str(lose + wintoomuch))
print("won too much = " + str(wintoomuch))

toc = time.perf_counter()

print(f'Elapsed time : {toc - tic:0.4f} seconds')