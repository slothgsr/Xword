# import time

# # 6.1-6.3 seconds to run without removing unused.  
# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)

# tic = time.perf_counter()
# combos = combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8)


# x=0
# for i in combos:
#     x+= 1

# print(x)

# toc = time.perf_counter()

# print(f'Elapsed time : {toc - tic:0.4f} seconds')

######################################################################################################################################

# import time

# # 8.1 seconds to run with:  pool[i] not in unused) 
# # 7.5 seconds to run with: pool[i] != 'v' or pool[i] != 'j' or pool[i] != 'q')
# def combinations(iterable, r, unused):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices if pool[i] != 'v' or pool[i] != 'j' or pool[i] != 'q')  #  change this 
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices if pool[i] != 'v' or pool[i] != 'j' or pool[i] != 'q') # change this

# tic = time.perf_counter()
# unused = ('v','j','q')
# combos = combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8, unused)


# x=0
# for i in combos:
#     x+= 1

# print(x)

# toc = time.perf_counter()

# print(f'Elapsed time : {toc - tic:0.4f} seconds')



######################################################################################################################################
# #  .5 seconds to run!!!!
# from itertools import combinations
# import time
# tic = time.perf_counter()
# combos = combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8)

# x=0
# for i in combos:
#     x+= 1

# print(x)


# toc = time.perf_counter()

# print(f'Elapsed time : {toc - tic:0.4f} seconds')




######################################################################################################################################


# 3.5 seconds to run
from itertools import combinations
import time
tic = time.perf_counter()
def combobreaker(arg1):
    unused = arg1
    for value in combinations(['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q'], 8):
        com =[]
        for letter in value:
            if letter not in unused:
                com.append(letter)
        yield com

combos = combobreaker()

x=0
for i in combos:
    x += 1
    # print(i)
print(x)

toc = time.perf_counter()

print(f'Elapsed time : {toc - tic:0.4f} seconds')
