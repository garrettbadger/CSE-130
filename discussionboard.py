# text = """This is some \n multi-line text."""

# letter = text[0]

# substring = text[2:6]

# list = text.split("u")


# array = ['22', '9', '45', '223', '308', '762']

# search_value = '223'

# array_elements = len(array)

# while array_elements > 1:
#     if (array[array_elements-1] == search_value):
#         print("Found search item!")
#         break
#     else:
#         array_elements -= 1
# if(array_elements == 1):
#     print("item not found!")

if 'a' < 'b':
    print('true')
else:
    print('false')

# def ComputeTax(income):
#     if (income < 123700):
#         # 15% tax bracket
#         if (income >= 15100 and income <61300):
#             tax = 1510 + 0.15 * (income - 15100)
#         # 10% tax bracket
#         elif (income < 15100):
#             tax = income * 0.10
#         # 25% tax bracket
#         else:
#             tax = 8440 + 0.25 * (income - 61300)
#     else:
#         # 28% tax bracket
#         if(income >= 123700 and income < 188450):
#             tax = 24040 + 0.28 * (income - 123700)
#         # 33% tax bracket
#         elif(income < 336550):
#             tax = 42170 + 0.33 * (income - 188450)
#         # 35% tax bracket
#         else:
#             tax = 91043 + 0.35 * (income - 336550)
#     return tax


# path1 = 'W03/W03Lab.py'
# open(path1)



# whitelist = [chr(i) for i in range(65, 91)]+ [chr(i) for i in range(97, 123)]+ [str(i) for i in range(0, 10)]
# print(whitelist)

# def sanitize(list, word):
#   for item in list:
#     if item in word:
#       word.replace(item, '')
#   return word

# print(sanitize(whitelist, "Aslk;jg--asdfl'"))



word_list = ["26", "6", "90", "55"]
word_list = [int(i) for i in word_list]
pivot = -1
step = -1
i_largest = word_list[pivot]

while abs(pivot) + 1 <= len(word_list):
  	
    i_pivot = word_list[pivot]
    i_check = word_list[pivot + step]
  
    if i_check > i_largest:
        i_largest = i_check
        spot = step + pivot
        if abs(step + pivot) < len(word_list):  
            step -= 1
    
    elif abs(step) >= len(word_list)+pivot:
        if i_largest > i_pivot:
            word_list[pivot], word_list[spot] = word_list[spot], word_list[pivot]
            pivot-=1
            step = -1
            spot = pivot+step
            if abs(step + pivot) < len(word_list):
                i_largest = word_list[pivot + step]
        else:
            pivot -= 1
            step = -1
            spot = pivot+step
            i_largest = word_list[pivot + step]
    else:
        step -= 1
  
print(word_list)


word_list = ["26", "6", "90", "55", '79', '109', '108', '40', '200']
word_list = [int(i) for i in word_list]

len = len(word_list)
i = 1
while i < len:
    x = word_list[i]
    j = i - 1
    while (j >= 0 and word_list[j] > x):
        word_list[j + 1] = word_list[j]
        j = j - 1
    word_list[j+1] = x
    i += 1
# word_list[0], word_list[3] = word_list[3], word_list[0]
print(word_list)



# word_list = ["26", "6", "90", "55", '79', '109', '108', '40', '200']
# word_list = [int(i) for i in word_list]

# len = len(word_list)
# i = -1
# while i < len:
#     x = word_list[i]
#     j = i - 1
#     while (j <= 0 and word_list[j] > x):
#         word_list[j + 1] = word_list[j]
#         j = j - 1
#     word_list[j+1] = x
#     i -= 1

# print(word_list)