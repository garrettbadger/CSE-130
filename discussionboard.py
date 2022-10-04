# text = """This is some \n multi-line text."""

# letter = text[0]

# substring = text[2:6]

# list = text.split("u")


array = ['22', '9', '45', '223', '308', '762']

search_value = '223'

array_elements = len(array)

while array_elements > 1:
    if (array[array_elements-1] == search_value):
        print("Found search item!")
        break
    else:
        array_elements -= 1
if(array_elements == 1):
    print("item not found!")