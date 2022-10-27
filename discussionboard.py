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



word_list = ["26", "55", "13", "45"]
pivot = -1
step = -1
i_largest = word_list[pivot]
while abs(pivot) < len(word_list):
  	
  i_pivot = word_list[pivot]
  i_check = word_list[pivot + step]
  
  if i_check > i_largest:
    i_largest = i_check
    step -= 1
  elif abs(step) >= len(word_list)-1:
    replace = word_list.pop(pivot)
    word_list.insert(pivot, i_largest)
    word_list.insert(step, i_pivot)
    pivot-=1
  else:
    step -= 1
  
print(abs(pivot))