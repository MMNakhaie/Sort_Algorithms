# This Program Creat by M.M.N

def Shell_Sort(LST, step):
    span = 0 
    k = 0 
    y = 0
    for i in range(0, len(step), 1):
        span = step[i]
        for j in range(span, len(LST), 1):
            y = LST[j]
            k = j - span
            while k >= 0 and y < LST[k] :
                LST[k + span] = LST[k]
                k -= span
            LST[k + span] = y

    Result = "\n\n The Sort List : [ "
    for z in range(0, 10, 1):
        Result += str(LST[z]) + " , "
    print(Result , "\b\b\b]")

def main():
    print("\n Algorithm Of Shell Sort !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")
    print("\n Steps is : [ 1, 3, 5, 7 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    steps = [ 1, 3, 5, 7 ]
    Shell_Sort(Numbers, steps)
    
    input()

main()
