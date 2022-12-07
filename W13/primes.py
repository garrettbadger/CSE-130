import math

def main():
    number = int(input('Please enter a number: '))
    numbers = []
    for i in range(number+1):
        numbers.append(True)
    
    primes = prime(numbers, number)
    print(primes)

def prime(numbers, number):
    primes = []
    numbers[0] = False
    numbers[1] = False

    for factor in range(2, math.floor(math.sqrt(number)+1)):
        if numbers[factor]:
            for multiple in range(factor*2, number+1, factor):
                numbers[multiple] = False

    for index in range(2, number+1):
        if numbers[index]:
            primes.append(index)

    return primes




if __name__ == "__main__":
    main()