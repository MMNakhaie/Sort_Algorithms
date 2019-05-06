# This Program Creat by M.M.N

def Bubble_Sort(LST):
    temp = 0
    for i in range(len(LST)-1, -1, -1):
        for j in range(0, i, 1):
            if LST[j] > LST[j+1] :
                temp = LST[j]
                LST[j] = LST[j+1]
                LST[j+1] = temp

    Result = "\n\n The Sort List : [ "
    for z in range(0, len(LST), 1):
        Result += str(LST[z]) + " , "
    print(Result, "\b\b\b]")

def main():
    print("\n Algorithm Of Bubble Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Bubble_Sort(Numbers)

    input()

main()
