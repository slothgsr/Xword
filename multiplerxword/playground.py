import time

#timer start
tic = time.perf_counter()

#  NO IDEA WHAT THIS DOES
from itertools import chain,repeat,islice,count
from collections import Counter

def combinations_without_repetition(r, iterable=None, values=None, counts=None):
    if iterable:
        values, counts = zip(*Counter(iterable).items())

    f = lambda i,c: chain.from_iterable(map(repeat, i, c))
    n = len(counts)
    indices = list(islice(f(count(),counts), r))
    if len(indices) < r:
        return
    while True:
        yield tuple(values[i] for i in indices)
        for i,j in zip(reversed(range(r)), f(reversed(range(n)), reversed(counts))):
            if indices[i] != j:
                break
        else:
            return
        j = indices[i]+1
        for i,j in zip(range(i,r), f(count(j), islice(counts, j, None))):
            indices[i] = j

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
    

test = combinations_without_repetition(8, iterable=['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'])

print(len(test))


Grid1 = ['timid', 'aside', 'substance', 'sign', 'oxen', 'able', 'one', 'afar', 'lap', 'kennel', 'else', 'oil', 
        'layout', 'sabotage', 'mob', 'snorkel', 'dot', 'argue', 'undo', 'sock', 'ballot', 'pineapple']

Grid2 = ['chef', 'haze', 'tweezers', 'once', 'astute', 'east', 'forecast', 'circus', 'iris', 'salute', 'gate', 
        'traffic', 'how', 'eat', 'rural', 'fee', 'use', 'court', 'here', 'something', 'epic', 'splint']
Grid1set = ["".join(set(x)) for x in Grid1]
Grid2set = ["".join(set(x)) for x in Grid2]
    
# combos = set(combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8))

