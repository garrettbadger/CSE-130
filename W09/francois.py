def francois(num):
    if num == 1:
        num == 2
    elif num == 2:
        num == 1
    # for i in range(num-1):
    num = num-1 + num-2
    return num
        

def main():
    count = int(input("Which number would you like? "))
    print(francois(count))


if __name__ == '__main__':
    main()