word_list = ["26", "6", "90", "55", "54", "100", "1"]
word_list = [int(i) for i in word_list]
pivot = -1
step = -1
i_largest = word_list[pivot]

while abs(pivot) + 1 < len(word_list):
  	
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