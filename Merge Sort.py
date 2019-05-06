# This Program Creat by M.M.N

def Merge_Sort(LST):
    if len(LST)>1 :
        mid = int(len(LST)/2)
        Left = LST[0:mid]
        Right = LST[mid:len(LST)]

        Merge_Sort(Left)
        Merge_Sort(Right)

        i = 0
        j = 0
        k = 0
        
        while i < len(Left) and j < len(Right) :
            if Left[i] <= Right[j]:
                LST[k] = Left[i] 
                i += 1
                k += 1
            else: 
                LST[k] = Right[j] 
                j += 1
                k += 1
        while i < len(Left):
            LST[k] = Left[i] 
            i += 1
            k += 1
        while j < len(Right):
            LST[k] = Right[j] 
            j += 1
            k += 1 

def main():
    print("\n Algorithm Of Merge Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Merge_Sort(Numbers)

    Result = "\n\n The Sort List : [ "
    for z in range(0, len(Numbers), 1):
        Result += str(Numbers[z]) + " , "
    print(Result, "\b\b\b]")

    input()

main()