# This Program Creat by M.M.N

def Split(LST, first, last, pos):
    temp = 0
    left = first 
    right = last 
    pivot = LST[first]

    while  left < right :
        while  LST[right] > pivot :
            right -=1

        while  LST[left] <= pivot :
            left +=1

        if  left < right :
            temp = LST[left]
            LST[left] = LST[right]
            LST[right] = temp

    pos = right
    LST[first] = LST[pos]
    LST[pos] = pivot
    return pos

def Quick_Sort(LST, first, last):
    pos = 0
    if first < last :
        pos = Split(LST, first, last, pos)
        Quick_Sort(LST, first, pos - 1)
        Quick_Sort(LST, pos + 1, last)

def main():
    print("\n Algorithm Of Quick Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Quick_Sort(Numbers, 0, len(Numbers)-1)

    Result = "\n\n The Sort List : [ "
    for z in range(0, 10, 1):
        Result += str(Numbers[z]) + " , "
    print(Result , "\b\b\b]")

    input()

main()
