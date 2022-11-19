# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program is meant to compute the given francois number 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this program was getting the loop to work correctly.
# 5. How long did it take for you to complete the assignment?
#      3.5 hours

def francois(num):
    #Make sure the number is within proper bounds
    assert num > 0
    m_list = [1, 2]
    #Make sure that the list is in the proper order
    assert m_list[0] == 1
    if num > 2:
        #If the number is above two then we will enter the loop otherwise return one of the numbers already in the list
        assert num > 2
        for i in range(3, num+1):
            #Loop to compute the francois number
            m_list[i % 2] = m_list[0] + m_list[1]
    value = m_list[num % 2]
    return value
 
def main():
    #This main program gets the number from the user that they want from the sequence
    #It also loops so the user can get multiple francois numbers
    another = True
    while another:
        #Get the number from the user
        count = int(input("Which number would you like? "))
        print(francois(count))
        #Ask the user if they want to get another number
        again = input("Do you want to get another number? (y/n) ")
        if again == 'y':
            another = True
        elif again == 'n':
            another = False
    
if __name__ == '__main__':
    main()