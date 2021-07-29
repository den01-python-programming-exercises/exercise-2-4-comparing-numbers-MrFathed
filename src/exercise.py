def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        print("{} is greater than {}".format(num1, num2))
    elif num2 > num1:
        print("{} is smaller than {}".format(num1, num2))
    else:
        print("{} is equal to {}".format(num1, num2))

if __name__ == '__main__':
    main()
