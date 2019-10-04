from itertools import permutations, combinations
from collections import OrderedDict

cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]

perm = list(permutations(cards, r=5))

res = list(OrderedDict.fromkeys(perm))
print("OrderedDict permutations: ", len(res))

file = open("permutations.txt", "w")
for x in res:
    file.write(str(x) + "\n")
file.close()



