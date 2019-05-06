# This Program Creat by M.M.N

def Insertion_Sort(LST):
    temp = 0
    for i in range(1, len(LST), 1):
        temp = LST[i]
        j = i
        while j > 0 and LST[j - 1] > temp :
            LST[j] = LST[j-1]
            j -= 1
        LST[j] = temp

    Result = "\n\n The Sort List : [ "
    for z in range(0, 10, 1):
        Result += str(LST[z]) + " , "
    print(Result , "\b\b\b]")

def main():
    print("\n Algorithm Of Insertion Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Insertion_Sort(Numbers)

    input()

main()
