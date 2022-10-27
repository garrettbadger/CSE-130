# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program will search for an item in a list using a method with O(log n) efficiency
# 4. Algorithmic Efficiency
#      The algorithmic efficiency is O(log n) because this program halfs the input size with each iteration.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out the logic for the advanced search.
# 6. How long did it take for you to complete the assignment?
#      3 hours
import json

def read_json(file):
    # This function will take care of reading in the json file that the user wants.
    
    try:
        x = open(f'W06/Lab06.{file}')

    except:
        print(f"Unable to open file {file}")

    data = x.read()

    jsondata = json.loads(data)
    # Turn the json data into a python list.
    file = jsondata['array']
    return file

def find_search(file_list, search):
    # This function is the search function it takes the item to be search for and the list as parameters.

    # Make sure that the list isn't empty.
    if len(file_list) > 0:
        start = 0
        end = len(file_list) - 1
        
        #This is where the searching happens.
        while start <= end:
            midpoint = (start + end) // 2
            middle = file_list[midpoint]
            if search < middle:
                end = midpoint - 1 
            elif search > middle:
                start = midpoint + 1
            elif search == middle:
                return 0
            else:
                return 1
    else:
        print('This list is empty. ')

def main():
    # The main function gets the users input and calls the other two functions as necessary.

    file = input('What is the name of the file? ')
    search = input('What are we looking for? ')
    file_list = read_json(file)
    found = find_search(file_list, search)
    if found == 0:
        print(f'We found {search} in {file}.')
        
    else:
        print(f'We could not find {search} in {file}.')


if __name__ == "__main__":
    main()