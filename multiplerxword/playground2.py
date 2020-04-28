from itertools import combinations


combos = combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8)
# print(len(combos))
# Flag = False
# test=[]
# for i in combos:
#     for letter in ['v','q','j']:
#         if letter in i:
#             Flag = True
#         else:
#             Flag = False
#             break
#     if Flag == True:
#         test.append(i)
# print(len(combos))
# print(len(test))
# print("finished")




for i in combos:
    print(i)