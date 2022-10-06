# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if the user is able to put a hotel on PA or not and then tells them how to do it.
# 4. What was the hardest part? Be as specific as possible.
#      I think the most challenging part of this assignment was making sure that I had all of the correct inputs and outputs in my program.
# 5. How long did it take for you to complete the assignment?
#      4 hours.

def Property_Counts():

    #Ask input on all properties in green color group.
    PA = int(input('What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    PC = int(input('What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    NC = int(input('What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))

    #Evaluate conditions of properties.
    if(PA == 5):
        print('You cannot purchase a hotel if the property already has one.')
    elif(PC == 5):
        print('Swap Pacific\'s hotel with Pennsylvania\'s 4 houses.')
    elif(NC == 5):
        print('Swap North Carolina\'s hotel with Pennsylvania\'s 4 houses.')
    else:
        Hotels_Count(PA, NC, PC)

def Hotels_Count(PA, NC, PC):
    
    #Ask for available houses and hotels.
    available_hotels = int(input('How many hotels are there to purchase? '))
    available_houses = int(input('How many houses are there to purchase? '))

    #Make sure there is enough hotels .
    if (available_hotels == 0):
        print('There are not enough hotels available for purchase at this time.')
    else:
        Num_Houses(PA, NC, PC, available_houses)

def Num_Houses(PA, NC, PC, av_houses):

    #Calculate how many houses are needed for a hotel on PA.
    PA_needed = 5 - PA
    NC_needed = 4 - NC
    PC_needed = 4 - PC
    total_houses_needed = PA_needed + NC_needed + PC_needed
    cash_needed = total_houses_needed * 200

    #Evaluate if there are enough houses.
    if (total_houses_needed < av_houses):
        print('There are not enough houses available for purchase at this time.')
    else:
        Cash(cash_needed, PA_needed, NC_needed, PC_needed)

def Cash(cash_needed, PA_needed, NC_needed, PC_needed):

    #Get available cash from user.
    available_cash = int(input('How much cash do you have to spend? '))
    
    #Evaluate if user has enough cash.
    if (available_cash < cash_needed):
        print('You do not have sufficient funds to purchase a hotel at this time.')
    else:
        Rec_Purchase(cash_needed, PA_needed, NC_needed, PC_needed)

def Rec_Purchase(cash_needed, PA_needed, NC_needed, PC_needed):

    total_houses = PC_needed + PA_needed + NC_needed

    #Evaluate how many houses to buy and where to put them.
    if(NC_needed and PC_needed < 4):
        print(f'This will cost ${cash_needed}.\n Purchase 1 hotel and {total_houses} house(s).\n Put 1 hotel on Pennsylvania and return any houses to the bank. \n '
        f'Put {NC_needed} house(s) on North Carolina. \n Put {PC_needed} house(s) on Pacific.')
    elif(NC_needed < 4):
        print(f'This will cost ${cash_needed}.\n Purchase 1 hotel and {total_houses} house(s).\n Put 1 hotel on Pennsylvania and return any houses to the bank. \n '
        f'Put {NC_needed} house(s) on North Carolina.')
    elif(PC_needed < 4):
        print(f'This will cost ${cash_needed}.\n Purchase 1 hotel and {total_houses} house(s).\n Put 1 hotel on Pennsylvania and return any houses to the bank. \n '
        f'Put {PC_needed} house(s) on Pacific.')
    else:
        print(f'This will cost ${cash_needed}.\n Purchase 1 hotel and {total_houses} house(s).\n Put 1 hotel on Pennsylvania and return any houses to the bank. \n ')

#Prompt the user if they own all green properties.
properties = input('Do you own all the green properties?(y/n) ')

#Evaluate if the user has all properties.
if(properties == 'y'):

    #If user has all properties start computing most efficient way to purchase hotel.
    Property_Counts()
else:
    print('You cannot purchase a hotel until you own all the properties of a given color group.')