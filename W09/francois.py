master_francois = [2, 1]
def francois(num, m_list):
    if num <= len(m_list):
        return m_list[num-1]
    for i in range(2, num):
        m_list.append(m_list[-1] + m_list[-2])
    return m_list[-1]        



def main():
    another = True
    while another:
        count = int(input("Which number would you like? "))
        print(francois(count, master_francois))
        Y = input("Do you want to get another number? (y/n) ")
        if Y == 'y':
            another = True
        elif Y == 'n':
            another = False
    


if __name__ == '__main__':
    main()