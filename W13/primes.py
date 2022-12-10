# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program is meant to find all of the primes between 0 and a given number by the user
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this code was getting the lists sorted out. Making sure that each 
#      each list was doing what it was supposed to and accessing all of the correct indicies. 
# 5. How long did it take for you to complete the assignment?
#      3 hours
import math

def main():
    # The user enters a number that the program uses as an upper limit to find primes.
    number = int(input('Please enter a number: '))
    # Make sure the number variable is of type int and greater than 0
    try: 
        assert isinstance(number, int)
    except:
        return print("Number is not an integer!")
    try:    
        assert number > 0
    except:
        return print("Number is not greater than 0!")
        
    numbers = []
    # Create a list with an index for every number from 0-number and set the value to True
    for i in range(number+1):
        numbers.append(True)
    # Make sure the list is the correct length
    assert len(numbers) == number+1
    primes = prime(numbers, number)
    print(primes)

def prime(numbers, number):
    # Create an empty list for the values that are prime to be stored
    primes = []
    # Set the values of 0 and 1 to not prime by default
    numbers[0] = False
    numbers[1] = False
    # Using the sqaure root of the number iterate through multiples of the factor to 
    # find elements that are not prime
    for factor in range(2, math.floor(math.sqrt(number)+1)):
        if numbers[factor]:
            for multiple in range(factor*2, number+1, factor):
                numbers[multiple] = False
    # For the remaining elements that are prime, add them to the primes list
    for index in range(2, number+1):
        if numbers[index]:
            # Verify the numbers being put in the list are prime
            assert numbers[index] == True
            primes.append(index)

    return primes

if __name__ == "__main__":
    main()