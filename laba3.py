'''
12.	Формируется матрица F следующим образом: если в В количество простых чисел в нечетных столбцах в области 2 больше,
чем сумма чисел в четных строках в области 1, то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*А– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
'''

import random

def printm(matrix):
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()

def prostoe(n):
    if n < 1:
        return False
    k=2
    while k*k <= n and n % k != 0:
        k+= 1
    return (k*k>n)

print("Введите число для задания размерности квадратной матрицы(не менее 4)")
N = int(input())
print("Введите число <K> ")
K = int(input())

if N < 4:
    print("Вы ввели слишком маленькую размерность матрицы")
    exit(0)

print("Квадратная матрица А")
matrixA = [[random.randint(-10, 10) for i in range(N)] for j in range(N)] ##
printm(matrixA)
print("-------------------")

matrixF = [[elem for elem in raw] for raw in matrixA]
print("Подматрица F")
printm(matrixF)

matrixB = [[0 for i in range((N//2))] for j in range((N//2))] ##B
if N % 2 == 0:
    for i in range(0, N // 2, 1):
        for j in range(0, N // 2, 1):
            matrixB[i][j] = matrixA[i][j] ##B
else:
    for i in range(0, N // 2, 1):
        for j in range(0, N // 2, 1):
            matrixB[i][j] = matrixA[i][j] ##B
print("Подматрица B")
printm(matrixB)
print("-------------------")

matrixE = [[0 for i in range((N//2))] for j in range((N//2))] ##B
if N % 2 == 0:
    for i in range(0, N//2, 1):
        for j in range(0, N // 2, 1):
            matrixE[i][j] = matrixA[i+N//2][j+N//2] ##B
else:
    for i in range(0, N // 2, 1):
        for j in range(0, N // 2, 1):
            matrixE[i][j] = matrixA[i+N//2+1][j+N//2+1] ##B
print("Подматрица E")
printm(matrixE)
#exit(0)
print("-------------------")

matrixE1 = [[elem for elem in raw] for raw in matrixE]

matrixF = [[elem for elem in raw] for raw in matrixA]
print("Начальная матрица F")
printm(matrixF)
print("-------------------")

l1 = N//2
ch = []  # числа второй области по нечетным столбцам
summ = 0  # сумма чисел по периметру четвертой области

if l1 == 2:  # если матрица B размерностью 2x2
    ch.append(matrixB[0][0])
    ch.append(matrixB[0][1])

if l1 == 3:  # если матрица B размерностью 3x3
    ch.append(matrixB[0][0])
    ch.append(matrixB[0][2])

dl = 1
dl1 = 2
n = 1
kolprostoe = 0
if l1 > 3: # если матрица размерностью 4x4 и более
    if l1 % 2 == 0: # если матрица четной размерности
        for i in range(0, len(matrixB[0])//2, 2):
            for j in range(0, dl):
                if prostoe(matrixB[j][i]):
                    #ch.append(matrixB[j][i])
                    kolprostoe += 1
            dl += 2
        for i in range(len(matrixB[0])-2, (len(matrixB[0])//2)-1, -2):
            for j in range(0, dl1):
                if prostoe(matrixB[j][i]):
                    #ch.append(matrixB[j][i])
                    kolprostoe += 1
            dl1 += 2

    else:  # если матрица нечетной размерности
        for i in range(0, (len(matrixB[0])//2)+1, 2):
            for j in range(0, dl):
                if prostoe(matrixB[j][i]):
                    #ch.append(matrixB[j][i])
                    kolprostoe += 1
            dl += 2
        dl=1
        for i in range(len(matrixB[0])-1, (len(matrixB[0])//2), -2):
            for j in range(0, dl):
                if prostoe(matrixB[j][i]):
                    #ch.append(matrixB[j][i])
                    kolprostoe += 1
            dl += 2

print("количество простых чисел в 2 области в нечётных столбцах -",kolprostoe)
symma = 0
dl = 2
dl1 = 1
dl2 = 2
if l1 % 2 == 0:
    for i in range(1,l1//2+1, 2):
        for j in range(0, dl, 1):
            symma = symma + matrixB[i][j]
            #print(matrixB[i][j])
        dl += 2
    for i in range(l1-1, l1 // 2, -2):
        for j in range(0, dl1, 1):
            symma = symma + matrixB[i][j]
            #print(matrixB[i][j])
        dl1 += 2
else:
    for i in range(1, l1//2+1, 2):
        for j in range(0, dl, 1):
            symma = symma + matrixB[i][j]
        dl += 2
    for i in range(l1-2, l1//2, -2):
        for j in range(0, dl2, 1):
            symma = symma + matrixB[i][j]
        dl2 += 2
print("сумма чисел 1 области в чётных строках ", symma)
printm(matrixB)

printm(matrixE)
if kolprostoe > symma: # меняем в E 1 и 2 область
    print("---------------кол-во простых чисел больше суммы----------------")
    l1 = len(matrixE)
    dl = 1
    dl1 = 1
    for i in range(0, l1 // 2, 1):
        for j in range(0, dl, 1):
            matrixE1[i][j] = matrixE[j][i]
            matrixE1[j][i] = matrixE[i][j]
        dl += 1
    for i in range(l1 - 1, l1 // 2 - 1, -1):
        for j in range(0, dl1, 1):
            matrixE1[i][j] = matrixE[j][i]
            matrixE1[j][i] = matrixE[i][j]
        dl1 += 1
    print("---------------RESULT----------------")
    printm(matrixE)
    printm(matrixE1)
else: # меняем C и E местами
    print("---------------кол-во простых чисел меньше суммы----------------")
    xuy = len(matrixF) // 2
    #printm(matrixA)
    matrixF2 = [[elem for elem in raw] for raw in matrixF]
    if N % 2 == 0:
        for i in range(0, len(matrixF) // 2):
            for j in range(len(matrixF) // 2, N):
                matrixF2[i][j] = matrixF[i + len(matrixF) // 2][j]
                matrixF2[i + len(matrixF) // 2][j] = matrixF[i][j]
        printm(matrixF)
        printm(matrixF2)
        matrixF = [[elem for elem in raw] for raw in matrixF2]
    else:
        for i in range(0, len(matrixF) // 2):
            for j in range(len(matrixF) // 2, N):
                matrixF2[i][j] = matrixF[i + len(matrixF) // 2 + 1][j]
                matrixF2[i + len(matrixF) // 2 + 1][j] = matrixF[i][j]
        printm(matrixF)
        printm(matrixF2)
        matrixF = [[elem for elem in raw] for raw in matrixF2]

# (K*A)*F-K*A(T)
matrixKA = [[element * K for element in row] for row in matrixA] # K * A
print("Матрица A умножить на K")
printm(matrixKA)

matrixKAF = [[elem for elem in raw] for raw in matrixF]
for i in range(N):  # A*(F+A)
        for j in range(N):
            matrixKAF[i][j] = matrixF[i][j] * matrixKA[i][j]
print("(Матрица A умножить на K) умножить на матрицу F")
printm(matrixKAF)

transposeA = [[row[i] for row in matrixA] for i in range(len(matrixA[0]))]
print("Транспонированная матрица A")
printm(transposeA)

matrixTAK = [[element * K for element in row] for row in transposeA] # K * A(T)
print("Транспонированная матрица A умножить на K")
printm(matrixTAK)

matrix_KAF_plus_TAK = [[elem for elem in raw] for raw in matrixKAF]
for i in range(N):  # KAF - KA(T)
        for j in range(N):
            matrix_KAF_plus_TAK[i][j] = matrixKAF[i][j] + matrixTAK[i][j]
print("Матрица (A*K)*F-K*A(T)")
printm(matrix_KAF_plus_TAK)