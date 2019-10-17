from itertools import permutations, product, chain
from collections import OrderedDict


def calc(word, numset, opset, displayres):
    stack = []
    iopset = chain(opset)
    inumset = chain(numset)
    res = -1

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
                    break           # break if v1 / v2 is odd
                stack.append(v1 // v2)
            else:
                raise ValueError('invalid operator')
        else:
            raise ValueError('invalid character')

        if stack[-1] <= 0:
            break
        displayres.append(x)
    else:
        # only return the result actual if we did not break out of the
        # for loop else it stay -1
        res = stack.pop()
    return res


def solve(numbers, lang):
    assert(len(numbers) == 5)
    solutions = {}

    num_nums = 2
    num_ops = 1

    for lang_vec in lang:
        for numset in permutations(numbers, num_nums):
            for opset in product('+-*/', repeat=num_ops):  # generate iterator with nops^2'+', nops^2'-', nops^2'*'....
                for word in lang_vec:
                    displayres = []

                    res = calc(word, numset, opset, displayres)
                    if 101 <= res <= 999 and res not in solutions:
                            solutions[res] = displayres

        num_ops = num_ops + 1
        num_nums = num_nums + 1

    return solutions


def lang_k_rec(available_o, available_n, k, x, possible):
    if available_n > 0:
        lang_k_rec(available_o, available_n - 1, k + 'N', x + 1, possible)
        if x > 1:
            lang_k_rec(available_o - 1, available_n, k + 'O', x - 1, possible)
    if available_o == 0 and available_n == 0:
        possible.append('NN' + k + 'O')


def gen_lang():
    possible_k = [[], [], [], [], []]
    for av in range(5):
        lang_k_rec(av, av, '', 2, possible_k[av])
        possible_k[av].sort()
    return possible_k


# Function to remove duplicate elements
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def gen_number_list(cards):
    # Getting permutations of length 5 from list 'cards'
    perm = list(permutations(cards, r=5))

    # Removing all the obvious duplicates
    res = sorted(list(OrderedDict.fromkeys(perm)))

    # Sorting all the elements of 'res' in place ( 2 3 1 to 1 2 3 )
    sorted_list = []
    for x in res:
        sorted_list.append(sorted(x))

    # Removing the duplicates we made in the previous step
    removed_list = remove(sorted_list)
    return removed_list


if __name__ == "__main__":
    cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]

    number_lists = gen_number_list(cards)

    # Outputs to file for analysis
    file = open("result.txt", "w")
    for numbers in number_lists:
       lang = gen_lang()
       sol = solve(numbers, lang)
       file.write(str(numbers) + " ")
       file.write(str(len(sol)) + "\n")
       print(len(sol))

    file.close()

    # Testing code for manual input
    #
    # s = input("Type your string with spaces: ")
    #
    # numbers = list(map(int, s.split()))
    # print(numbers)
    # lang = gen_lang()
    # sol = solve(numbers, lang)
    #
    # print(sol)
    # print(len(sol))



