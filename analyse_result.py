import matplotlib.pyplot as plt

def main():
    f = open("result.txt", "r")
    f1 = f.readlines()

    max = 0
    numberlist = []
    for x in f1:
        num = int(x.split("]", 1)[1])
        numberlist.append(num)
        if num > max:
            max = num

    print("Max attainable values between 101-999: ", max)
    plt.plot(numberlist, linewidth=0.4)
    plt.ylabel('Possible answers')
    plt.xlabel('Card combinations')
    plt.show()
    f.close()


if __name__ == "__main__":
    main()


