from random import random, randrange, randint


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:4d}'.format(matrix[i][j]), end='')
        print()
    return ''

#1
# 1. Даны целые положительные числа M и N. Сформировать
# целочисленную матрицу размера M × N, у которой все элементы Iй строки имеют значение 10*I (I = 1, …, M).
m = int(input('Введите m: '))
n = int(input('Введите n: '))
a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = 10 * (i + 1)
print(a)


#2
# 2. Даны целые положительные числа M и N. Сформировать
# целочисленную матрицу размера M × N, у которой все элементы Jго столбца имеют значение 5*J (J = 1, …, N).
m = int(input('Введите m: '))
n = int(input('Введите n: '))
a = [[0] * n for i in range(m)]
for j in range(n):
    for i in range(m):
        a[i][j] = 5 * (j + 1)
print(a)


#3
# 3. Даны целые положительные числа M, N, число D и набор из M чисел. Сформировать матрицу размера M × N,  у которой
# первый столбец совпадает с исходным набором чисел, а элементы каждого следующего столбца равны сумме
# соответствующего элемента предыдущего столбца и числа D (в результате каждая строка
# матрицы будет содержать элементы арифметической прогрессии).
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
d = int(input("Введите число d: "))
a = [[0] * n for i in range(m)]
b = input("Введите список: ").split()
for i in range(m):
    a[i][0] = int(b[i])
    for j in range(1, n):
        a[i][j] = a[i][j - 1] + d
print(a)


#4
# 4. Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). Вывести элементы K-й строки данной матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[randint(-10, 10)] * n for i in range(m)]
k = int(input("Введите число k: "))
print('Исходный массив: ', a)
for i in range(m):
    for j in range(n):
        if i == k - 1:
            print(a[i][j], end = ' ')


#5
# 5. Дана матрица размера M × N и целое число K (1 ≤ K ≤ N). Вывести
# элементы K-го столбца данной матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[randint(-10, 10)] * n for i in range(m)]
k = int(input("Введите число k: "))
print('Исходный массив: ', a)
for j in range(n):
    for i in range(m):
        if j == k - 1:
            print(a[i][j], end = ' ')
 


#6
# 6. Дана матрица размера M × N. Вывести ее элементы, расположенные в строках с четными номерами (2, 4, …).
# Вывод элементов производить по строкам, условный оператор не использовать.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[randint(-10, 10)] * n for i in range(m)]
print('Исходный массив: ', a)
for i in range(1, m, 2):
    for j in range(n):
        print(a[i][j], end=' ')
  

#7
# 7. Дана матрица размера M × N. Вывести ее элементы, расположенные в столбцах с нечетными номерами (1, 3, …).
# Вывод элементов производить по столбцам, условный оператор не использовать.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for j in range(0, n, 2):
    for i in range(m):
        print(mas[i][j], end=' ')


#8
# 8. Треугольник Паскаля. Вывести на экран треугольник Паскаля из n строк. Придумать структуру данных для хранения
# треугольника Паскаля (например, стандартная матрица, что, однако, не экономно).
# Реализовать показ треугольника по данным из этой структуры.
n = int(input("Введите число n: "))
a = [[1]]
for j in range(1, n):
    l = [0] * (len(a[j - 1]) + 1)
    for i in range(len(a[j - 1])):
        l[i] += a[j - 1][i]
    for i in range(len(a[j - 1])):
        l[i + 1] += a[j - 1][i]
    a.append(l)
print(printMatrix(a))


#9
# 9. Дана матрица размера M × N и целое число K (1 ≤ K ≤ M).
# Найти сумму и произведение элементов K-й строки данной матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
k = int(input("Введите число k: "))
p = 1
for j in range(n):
    p *= mas[k-1][j]
print('Произведение = ', p)
print('Сумма = ', sum(mas[k-1]))


#10
# 10.Дана матрица размера M × N и целое число K (1 ≤ K ≤ N). Найти
# сумму и произведение элементов K-го столбца данной матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
k = int(input("Введите число k: "))
p = 1
s = 0
for i in range(m):
    p *= mas[i][k-1]
    s += mas[i][k-1]
print('Произведение = ', p)
print('Сумма = ', s)


#11
# 11.Дана матрица размера M × N. В каждой строке матрицы найти минимальный элемент.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    print('Минимум', i + 1, 'строки = ', min(mas[i]))


#12
# 12.Дана матрица размера M × N. В каждом столбце матрицы найти максимальный элемент.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for j in range(n):
    mx = mas[0][j]
    for i in range(m):
        if mas[i][j] > mx:
            mx = mas[i][j]
    print('Максимум', j + 1, 'столбца = ', mx)

#13
# 13.Дана матрица размера M × N. Найти максимальный среди минимальных элементов ее строк.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
   tmp.append(min(mas[i]))
print(max(tmp))



#14
# 14.Дана целочисленная матрица размера M × N. Найти элемент, являющийся максимальным в своей строке и
# минимальным в своем столбце. Если такой элемент отсутствует, то вывести 0.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))

for i in range(m):
   tmp.append(min(mas[i]))
print(max(tmp))

#15
# 15.Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 < K2 ≤ M).
# Поменять местами строки матрицы с номерами K1 и K2.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
k1 = int(input("Введите число k1: "))
k2 = int(input("Введите число k2: "))
mas[k1 - 1], mas[k2 - 1] = mas[k2 - 1], mas[k1 - 1]
print(printMatrix(mas))


#16
# 16. Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 < K2 ≤ N).
# Поменять местами столбцы матрицы с номерами K1 и K2.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
k1 = int(input("Введите число k1: "))
k2 = int(input("Введите число k2: "))
for i in range(m):
    mas[i][k1 - 1], mas[i][k2 - 1] = mas[i][k2 - 1], mas[i][k1 - 1]
print(printMatrix(mas))



#17
# 17.Дана матрица размера M × N. Преобразовать матрицу, поменяв
# местами минимальный и максимальный элемент в каждой строке.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    x = mas[i].index(max(mas[i]))
    y = mas[i].index(min(mas[i]))
    mas[i][x], mas[i][y] = mas[i][y], mas[i][x]
print(printMatrix(mas))


#18
# 18.Дана матрица размера M × N. Преобразовать матрицу, поменяв
# местами минимальный и максимальный элемент в каждом столбце.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for j in range(n):
    mx = mas[0][j]
    mn = mas[0][j]
    y = 0; x = 0
    for i in range(m):
        if mas[i][j] < mn:
            mn = mas[i][j]
            x = i
        elif mas[i][j] > mx:
            mx = mas[i][j]
            y = i
    mas[x][j], mas[y][j] = mas[y][j], mas[x][j]
print(printMatrix(mas))


#19
# 19.Дана квадратная матрица A порядка M. Найти сумму элементов ее главной диагонали, то есть диагонали,
# содержащей следующие элементы: A1,1, A2,2, A3,3, …, AM,M.
m = int(input("Введите число m: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
s = 0
i = 0; j = 0
while i < m and j < m:
    s += mas[i][j]
    i += 1
    j += 1
print(s)


#20
# 20.Дана квадратная матрица A порядка M. Найти среднее арифметическое элементов ее побочной диагонали, то есть
# диагонали, содержащей следующие элементы: A1,M, A2,M–1, A3,M–2, …, AM,1
m = int(input("Введите число m: "))
mas = []
tmp = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
s = 0
i = 0; j = m-1
while i < m and j >= 0:
    s += mas[i][j]
    i += 1
    j -= 1
print(s/m)


#21
# 21.Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали, параллельной главной (начиная с
# одноэлементной диагонали A1,M).
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
i = 0
while i < m - 1:
    sum = 0
    j = m - 1 - i
    i = 0
    while j <= m - 1:
        sum += mas[i][j]
        j += 1
        i += 1
    print(sum)
for i in range(1, m):
    sum = 0
    for j in range(i, m):
        sum += mas[j][j - i]
    print(sum)


#22
# 22.Дана квадратная матрица A порядка M. Найти минимальный элемент для каждой ее диагонали,
# параллельной главной (начиная с одноэлементной диагонали A1,M).
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
i = 0; j = 0
mn = mas[i][j]
while i < m - 1:
    j = m - 1 - i
    i = 0
    while j <= m - 1:
        mn = min(mn, mas[i][j])
        j += 1
        i += 1
for i in range(1, m):
    for j in range(i, m):
        mn = min(mn, mas[j][j - i])
print(mn)



#23
# 23.Дана целочисленная матрица размера M × N. Найти номер  последней из ее строк, содержащих только четные числа.
# Если таких строк нет, то вывести 0.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
count = 0
tmp = 0
for i in range(m):
    for j in range(n):
        if mas[i][j] % 2 == 0:
            count += 1
    if count == n:
        tmp = i + 1
    count = 0
print(tmp)


#24
# 24.Дана целочисленная матрица размера M × N. Найти количество ее строк, все элементы которых различны.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
count = 0
for i in range(m):
    d = {}
    f = True
    for j in range(n):
        if d.get(mas[i][j]) is not None:
            d[mas[i][j]] += 1
        else:
            d[mas[i][j]] = 1
    l = 0
    while l < n:
        if d[mas[i][l]] > 1:
            f = False
            break
        else:
            l += 1
    if f:
        count += 1
print(count)

#25
# 25.Дана матрица размера M × N. Поменять местами строки, содержащие минимальный и максимальный элементы матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(a))
mn = 0
mx = 0
k = 0; l = 0
for i in range(m):
    for j in range(n):
        if a[i][j] < a[mn][k]:
            mn = i
            k = j
        if a[i][j] > a[mx][l]:
            mx = i
            l = j
a[mx], a[mn] = a[mn], a[mx]
print(printMatrix(a))

#26
# 26.Дана матрица размера M × N. Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(a))
mn = 0
mx = 0
k = 0; l = 0
for i in range(m):
    for j in range(n):
        if a[i][j] < a[k][mn]:
            mn = j
            k = i
        if a[i][j] > a[l][mx]:
            mx = j
            l = i
for i in range(m):
    a[i][mx], a[i][mn] = a[i][mn], a[i][mx]
print(printMatrix(a))

#27
# 27.Дана матрица размера M × N. Упорядочить ее строки так, чтобы их первые элементы образовывали возрастающую
# последовательность.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(a))
for i in range(m - 1):
    for l in range(i + 1, m):
        if a[i][0] > a[l][0]:
            for j in range(n):
                a[i][j], a[l][j] = a[l][j], a[i][j]
print(printMatrix(a))


#28
# 28.Дана матрица размера M × N. Упорядочить ее столбцы так, чтобы их последние элементы образовывали убывающую
# последовательность.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(a))
for j in range(n - 1):
    for l in range(j + 1, n):
        if a[m - 1][j] < a[m - 1][l]:
            for i in range(m):
                a[i][j], a[i][l] = a[i][l], a[i][j]
print(printMatrix(a))


#29
# 29.Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). Перед строкой матрицы с номером K вставить строку из нулей.
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = []
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(a))
k = int(input("Введите число k: "))
new = []
tmp = [0] * n
for i in range(m):
    if i == (k - 1):
        new.append(tmp)
    new.append(a[i])
print(printMatrix(new))


#30
# 30.Дана квадратная матрица порядка M. Обнулить элементы матрицы, лежащие ниже главной диагонали.
# Условный оператор не использовать.
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    for j in range(i):
        mas[i][j] = 0
print(printMatrix(mas))


#31
# 31.Дана квадратная матрица порядка M. Обнулить элементы матрицы, лежащие одновременно выше главной диагонали
# и выше побочной диагонали. Условный оператор не использовать.
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    for j in range(i + 1, m - i - 1):
        mas[i][j] = 0
print(printMatrix(mas))


#32
# 32.Дана квадратная матрица A порядка M. Зеркально отразить ее элементы относительно главной диагонали
# (при этом элементы главной диагонали останутся на прежнем месте, элемент A1,2 поменяется местами с A2,1,
# элемент A1,3 — с A3,1 и т. д.). Вспомогательную матрицу не использовать.
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    for j in range(i, m):
        mas[i][j], mas[j][i] = mas[j][i], mas[i][j]
for i in range(m):
    for j in range(m):
        print('{:4d}'.format(mas[i][j]), end='')
    print()


#33
# 33.Дана квадратная матрица A порядка M. Повернуть ее на угол 90° в положительном направлении,
# то есть против часовой стрелки (при этом элемент A1,1 перейдет в AM,1, элемент AM,1 — в AM,M и т. д.).
# Вспомогательную матрицу не использовать.
m = int(input("Введите число m: "))
mas = []
for i in range(m):
    mas.append([])
    for j in range(m):
        mas[i].append(randint(-10, 10))
print('Исходный массив: ')
print(printMatrix(mas))
for i in range(m):
    mas[i].reverse()
zipped_rows = zip(*mas)
new_m = [list(row) for row in zipped_rows]
print(printMatrix(new_m))