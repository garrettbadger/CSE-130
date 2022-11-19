
def francois(num):
    m_list = [1, 2]
    if num > 2:
        for i in range(3, num+1):
            m_list[i % 2] = m_list[0] + m_list[1]
    value = m_list[num % 2]
    return value
    # if num <= len(m_list):
    #     return m_list[num-1]
    # for i in range(2, num):
    #     m_list.append(m_list[-1] + m_list[-2])
    # return m_list[-1]        



def main():
    another = True
    while another:
        count = int(input("Which number would you like? "))
        print(francois(count))
        Y = input("Do you want to get another number? (y/n) ")
        if Y == 'y':
            another = True
        elif Y == 'n':
            another = False
    


if __name__ == '__main__':
    main()