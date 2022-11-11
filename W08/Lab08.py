#1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will sort a list from least to greatest. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was debugging it and finding where it wasn't working. I originally
#      had it so the second for loop went from 1 - pivot-1 but that wasn't working and it was 
#      skipping more lines than it should have so I got rid of the -1 and now it works as expected. 
# 5. How long did it take for you to complete the assignment?
#      4

import json

def read_json(file):
    # This function will take care of reading in the json file that the user wants.
    
    try:
        x = open(f'W08/Lab08.{file}')

    except:
        print(f"Unable to open file {file}")

    data = x.read()

    jsondata = json.loads(data)
    # Turn the json data into a python list.
    file = jsondata['array']
    return file

def sort_array(array):
    # Make sure we are given a python list.
    assert type(array) == list
    # Loop through all of the list items starting with the last one.
    for i_pivot in range(len(array)-1, 0, -1):
        i_largest = 0
        # Loop through all of the items from 1 to the pivot.
        for i_check in range(1, i_pivot, 1):
            # If the current item is bigger than the largest item, make the largest equal to the current.
            if array[i_check] > array[i_largest]:
                i_largest = i_check
        # If the largest item is bigger than the pivot, switch them. 
        if array[i_largest] > array[i_pivot]:
            array[i_pivot], array[i_largest] = array[i_largest], array[i_pivot]
    return array

def main():
    # The main function gets the user input and calls the other two functions as necessary.

    file = input('What is the name of the file? ')
    file_list = read_json(file)
    sorted_array = sort_array(file_list)
    print(sorted_array)


if __name__ == "__main__":
    main()