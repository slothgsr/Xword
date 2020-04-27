from itertools import combinations


combos = list(combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 7))
print(len(combos))
Flag = False
for i in combos:
    for letter in i:
        if letter in ['k', 'a', 'r', 'n', 'o', 'e','d']:
            Flag = True
        else:
            Flag = False
            break
    if Flag == True:
        print(i)
print(len(combos))
print("finished")