# This Program Creat by M.M.N

def Selection_Sort(LST):
    minPos = 0
    temp = 0
    for i in range(0, len(LST), 1):
        minPos = i
        for j in range(i+1, len(LST), 1):
            if  LST[j] < LST[minPos] :
                minPos = j
        temp = LST[minPos]
        LST[minPos] = LST[i]
        LST[i] = temp
    
    Result = "\n\n The Sort List : [ "
    for z in range(0, 10, 1):
        Result += str(LST[z]) + " , "
    print(Result , "\b\b\b]")

def main():
    print("\n Algorithm Of Selection Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Selection_Sort(Numbers)

    input()

main()
