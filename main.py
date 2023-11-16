from functions import number, number2
if __name__ == '__main__':
    sum,resarr = number(1, 0)
    print(sum)
    print(resarr)

    sum1,resarr1, verbose = number2(1, -2, True)
    print(sum1)
    print(resarr1)
    print(verbose)
