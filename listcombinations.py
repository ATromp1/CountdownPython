from itertools import permutations
from collections import OrderedDict


cards = [1, 1, 2, 3]# , 3] #, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]

perm = list(permutations(cards, r=3))                                                                                   # Every permutation from the list Cards
print("Amount of permutations: ", len(perm))
print(perm)


res = sorted(list(OrderedDict.fromkeys(perm)))                                                                          # Removes all duplicates with orderedDict since the list is sorted
print("Amount after removing obvious duplicates: ", len(res))
print(res)

sortedlist = []
for x in res:
    sortedlist.append(sorted(x))                                                                                        # Each individual value in res will be sorted from low to high


def remove(duplicate):
    '''
    This function looks for values already existing in final_list. If not, there is no duplicate of that value.
    '''
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


final_list = remove(sortedlist)                                                                                         # uses the function remove to find all unique values that are sorted
print("Final amount of permutations after removing duplicates twice: ", len(final_list))
print(final_list)

file = open("permutations.txt", "w")                                                                                    # writing all possibilities to file permutations.exe
for x in final_list:
    file.write(str(x) + "\n")
file.close()



