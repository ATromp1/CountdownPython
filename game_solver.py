from itertools import permutations, product, chain
from sys import version_info
from collections import OrderedDict


def lang_k_rec(available_o, available_n, k, x, possible):
    if available_n > 0:
        lang_k_rec(available_o, available_n - 1, k + 'N', x + 1, possible)
    if available_o > 0 and x > 1:
        lang_k_rec(available_o - 1, available_n, k + 'O', x - 1, possible)
    if available_o == 0 and available_n == 0:
        possible.append('NN' + k + 'O')


def gen_lang():
    possible_k = [[], [], [], [], []]
    for av in range(5):
        lang_k_rec(av, av, '', 2, possible_k[av])
        possible_k[av].sort()
    return possible_k


def solve(nums, lang):
    assert(len(nums) == 5)
    solutions = {}
    for (lang_i, lang_vec) in enumerate(lang):
        nnums = lang_i + 2
        nops = lang_i + 1
        for numset in permutations(nums, nnums):
            for opset in product('+-*/', repeat=nops):
                for word in lang_vec:
                    displayres = []
                    stack = []
                    iopset = chain(opset)
                    inumset = chain(numset)
                    for c in word:
                        if c == 'N':
                            x = next(inumset)
                            stack.append(x)
                        elif c == 'O':
                            x = next(iopset) 
                            v1 = stack.pop()
                            v2 = stack.pop()
                            if x == '+':
                                stack.append(v1 + v2)
                            elif x == '-':
                                stack.append(v1 - v2)
                            # Ones are no good for * or /
                            elif v1 == 1 or v2 == 1:
                                break
                            elif x == '*':
                                stack.append(v1 * v2)
                            elif x == '/':
                                if v1 % v2 != 0:
                                    break
                                stack.append(v1 // v2)
                            else:
                                raise ValueError('invalid operator')
                        else:
                            raise ValueError('invalid character')

                        if stack[-1] <= 0:
                            break
                        displayres.append(x)
                    else:
                        # only check the result if we did not break out of the
                        # for loop
                        res = stack.pop()
                        if 101 <= res <= 999 and res not in solutions:
                            solutions[res] = displayres
    return solutions


# Function to remove duplicate elements
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


if __name__ == "__main__":
    cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]

    # Getting permutations of length 5 from list 'cards'
    perm = list(permutations(cards, r=5))

    # Removing all the obvious duplicates
    res = sorted(list(OrderedDict.fromkeys(perm)))

    # Sorting all the elements of 'res' in place ( 2 3 1 to 1 2 3 )
    sortedList = []
    for x in res:
        sortedList.append(sorted(x))

    # Removing the duplicates we made in the previous step
    removed_list = remove(sortedList)

    # Outputs to file for analysis
    #file = open("result.txt", "w")
    #for x in removed_list:
    #    lang = gen_lang()
    #    sol = solve(x, lang)
    #    file.write(str(x) + " ")
    #    file.write(str(len(sol)) + "\n")
    #    print(len(sol))

    # file.close()

    # Testing code for manual imput

    s = input("Type your string with spaces: ")
    numbers = list(map(int, s.split()))
    print(numbers)
    lang = gen_lang()
    sol = solve(numbers, lang)
    print(sol)
    print(len(sol))



