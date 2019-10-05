def main():
    f = open("result.txt", "r")
    f1 = f.readlines()
    iteration = []
    amount = []
    for x in f1:
        result = x.split()
        #print(result)
        iteration.append(result[0])
        amount.append(int(result[1]))
    f.close()


if __name__ == "__main__":
    main()


