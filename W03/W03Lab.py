
from tkinter import Y


def Property_Counts():
    #Ask input on all properties in green color group
    PA = int(input('What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    PC = int(input('What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    NC = int(input('What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    if(PA == 5):
        print('You cannot purchase a hotel if the property already has one.')
    elif(PC == 5):
        print('Swap Pacific\'s hotel with Pennsylvania\'s 4 houses.')
    elif(NC == 5):
        print('Swap North Carolina\'s hotel with Pennsylvania\'s 4 houses.')
    else:
        Hotels_Count(PA, NC, PC)
def Hotels_Count(PA, NC, PC):
    available_hotels = int(input('How many hotels are there to purchase? '))
    available_houses = int(input('How many houses are there to purchase? '))
    if (available_hotels == 0):
        print('There are not enough hotels available for purchase at this time.')
    else:
        Num_Houses(PA, NC, PC, available_houses)
def Num_Houses(PA, NC, PC, av_houses):
    PA_needed = 5 - PA
    NC_needed = 4 - NC
    PC_needed = 4 - PC
    total_houses_needed = PA_needed + NC_needed + PC_needed
    cash_needed = total_houses_needed * 200
    if (total_houses_needed < av_houses):
        print('There are not enough houses available for purchase at this time.')
    else:
        Cash(cash_needed, PA_needed, NC_needed, PC_needed)
def Cash(cash_needed, PA_needed, NC_needed, PC_needed):
    available_cash = int(input('How much cash do you have to spend? '))
    
    if (available_cash < cash_needed):
        print('You do not have sufficient funds to purchase a hotel at this time.')
    else:
        Rec_Purchase(cash_needed, PA_needed, NC_needed, PC_needed)

def Rec_Purchase(cash_needed, PA_needed, NC_needed, PC_needed):
    total_houses = PC_needed + PA_needed + NC_needed
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

#Prompt the user if they own all green properties
properties = input('Do you own all the green properties?(y/n) ')
#Evaluate the value of properties
if(properties == 'y'):
    Property_Counts()
else:
    print('You cannot purchase a hotel until you own all the properties of a given color group.')