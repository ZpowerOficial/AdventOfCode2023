def load():
    file = open('entradasdia4.txt')
    lines = file.readlines()
    file.close()
    arr = []
    for line in lines:
        values = [int(val.strip()) for val in line.strip().split(":")[1].split("|")[0].split()]
        check = [int(val.strip()) for val in line.strip().split(":")[1].split("|")[1].split()]
        arr.append([values, check])
    return arr
 
 
def Task1(arr):
    summ = 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i][0])):
            if arr[i][0][j] in arr[i][1]:
                count += 1
        if count >= 1:
            help = 1
            while count > 1:
                count -= 1
                help *= 2
        else:
            help = 0
        summ += help
    return summ
 
def Task2(arr):
    coppy = [1]*len(arr)
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i][0])):
            if arr[i][0][j] in arr[i][1]:
                count += 1
        while count >0:
            coppy[i+count] += 1 *coppy[i]
            count -= 1
    return sum(coppy)
 
 
print(Task1(load()))
print(Task2(load()))
