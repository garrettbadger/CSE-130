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
try:
    x = open('C:/Users/flipp/CSE-130/W02/Lab02.json')

except:
    print("Unable to open file Lab02.json")

data = x.read()

jsondata = json.loads(data)

usernames = jsondata['username']
passwords = jsondata['password']

username = input("Please enter a username: ")
password = input("Please enter a password: ")

u_location = -1
p_location = -2

for i in range(len(usernames)):
    if (usernames[i] == username):
        u_location = i
    
for i in range(len(passwords)):
    if (passwords[i] == password):
        p_location = i
    

if(p_location == u_location):
    print("You are authenticated!")
else:
    print("You are not authorized to use this system.")