# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is meant to read a json object into python and then using the json authenticate users who present valid usernames and passwords
# 4. What was the hardest part? Be as specific as possible.
#      Remebering how to manipulate json
# 5. How long did it take for you to complete the assignment?
#      3 hours
import json

def read_json(file):

    try:
        x = open(f'W06/Lab06.{file}')

    except:
        print(f"Unable to open file {file}")

    data = x.read()

    jsondata = json.loads(data)

    file = jsondata['array']
    return file

def find_search(file_list, search):
    if len(file_list) > 0:
        start = 0
        end = len(file_list) - 1
        
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