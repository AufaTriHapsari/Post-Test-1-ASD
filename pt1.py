import os
os.system("cls")

#mergesort
def flatten(variabel):
    if isinstance(variabel, list):
        listkosong = []
        for i in variabel:
            listkosong.extend(flatten(i))
        return listkosong
    else:
        return [variabel]   

        
def mergeSort(arr): 
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left [0] < right [0]:
            result.append(left. pop(0))
        else :
            result.append(right. pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

variabel = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

print ("list belum terurut: ") 
print (variabel)
print ("list sudah terurut: ")
list_baru = flatten(variabel)
Hasil = mergeSort(list_baru)
print(Hasil)
