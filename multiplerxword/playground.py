import time

#timer start
tic = time.perf_counter()

def wordfinder(arg1, arg2): #arg1 = combo,  arg2 = Gridlist
    counts=[]
    for grid in arg2:   
        for letter in arg1:
            if len(grid) <=1:
                break
            remove = []
            for word in grid:
                if letter in word:
                    remove.append(word)             
            for i in remove:
                grid.remove(i)
        counts.append(len(grid))
    return counts   
    
Grid1 = ['timid', 'aside', 'substance', 'sign', 'oxen', 'able', 'one', 'afar', 'lap', 'kennel', 'else', 'oil', 
        'layout', 'sabotage', 'mob', 'snorkel', 'dot', 'argue', 'undo', 'sock', 'ballot', 'pineapple']

Grid2 = ['chef', 'haze', 'tweezers', 'once', 'astute', 'east', 'forecast', 'circus', 'iris', 'salute', 'gate', 
        'traffic', 'how', 'eat', 'rural', 'fee', 'use', 'court', 'here', 'something', 'epic', 'splint']
Grid1set = ["".join(set(x)) for x in Grid1]
Grid2set = ["".join(set(x)) for x in Grid2]
    
combos =(['o', 'n', 'g', 'f', 'y','j','q','v'],['a', 'k', 'e', 'u', 's','t'])


for i in combos:
    Gridlist= [Grid1set[:],Grid2set[:]]
    count = wordfinder(i, Gridlist)



toc = time.perf_counter()

print(f'Elapsed time : {toc - tic:0.4f} seconds')
# combos = set(combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8))

# print(len(combos))


# Grid1 = ['timid', 'aside', 'substance', 'sign', 'oxen', 'able', 'one', 'afar', 'lap', 'kennel', 'else', 'oil', 
#         'layout', 'sabotage', 'mob', 'snorkel', 'dot', 'argue', 'undo', 'sock', 'ballot', 'pineapple']

# Grid2 = ['chef', 'haze', 'tweezers', 'once', 'astute', 'east', 'forecast', 'circus', 'iris', 'salute', 'gate', 
#         'traffic', 'how', 'eat', 'rural', 'fee', 'use', 'court', 'here', 'something', 'epic', 'splint']
      

# letterdic = dict.fromkeys(string.ascii_lowercase, 0)
# for word in Grid1:
#     for letter in word:
#         if letter in letterdic:
#             letterdic[letter] += 1
#         else:
#             letterdic[letter] = 1

# for word in Grid2:
#     for letter in word:
#         if letter in letterdic:
#             letterdic[letter] +=1
#         else:
#             letterdic[letter] = 1
# sorted_d = sorted(((value, key) for (key,value) in letterdic.items()),reverse = True)
# print(sorted_d)

# unused =[k for k,v in letterdic.items() if v == 0]
# print(unused)
# combo2 = ((ele for ele in sub if ele not in unused) for sub in combos)


# test = list(combo2)

# print(len(test))