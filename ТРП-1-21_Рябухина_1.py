import math

#1.1
print("1.1. Составить алгоритм вычисления значения функции y=7x+5, значение x вводится пользователем.")
x = int(input("Input  x:"))
print("y = ", 7 * x + 5)

#1.2
print("1.2. Составить алгоритм вычисления периметра квадрата, если известна его сторона, сторона квадрата вводится пользователем")
a = int(input("Input  a:"))
print("P = ", 4 * a)

#1.3
print("1.3. Составить алгоритм вычисления длины окружности, если известен ее радиус, радиус окружности вводится пользователем.")
R = int(input("Input  R:"))
print("C = ", 2 * math.pi * R)

#1.4
print("1.4. Составить алгоритм вычисления площади окружности, если известен ее диаметр, диаметр вводится пользователем.")
d = int(input("Input  d:"))
print("S = ", (math.pi * d * d) / 4)

#1.5
print("1.5. Составить алгоритм вычисления периметра прямоугольного треугольника, если известны его катеты, катеты вводятся пользователем.")
a = int(input("Input  a: "))
b = int(input("Input  b: "))
print("P = ", a + b + (math.sqrt(a * a + b * b)))

#1.6
print("1.6. Составить алгоритм вычисления площади кольца, если известны радиуса внешней и внутренней окружности, радиусы окружностей вводятся пользователем.")
R = int(input("Input  R: "))
r = int(input("Input  r: "))
print("S = ", math.pi * R * R - math.pi * r * r)

#1.7
print("1.7. Составить алгоритм вычисления периметра равнобедренной трапеции, если известны ее основания и высота, основания и высота вводятся пользователем.")
a = int(input("Введите большее основание: "))
b = int(input("Введите меньшее основание: "))
h = int(input("Введите высоту: "))
print("P = ", a + b + 2 * (math.sqrt(h * h + ((a - b) / 2)**2)))

#1.8
print("1.8. Дано число n (вводится пользователем). С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.")
n = int(input("Input n: "))
print("Time = ", n // 60 % 24, ":", n % 60)

#1.9
print("1.9. Создайте две переменные: пусть одна хранит ваше имя, а другая фамилию. Теперь напечатайте приветствие вроде такого: «Привет, Брандо Икетт!».")
name = "Владислава"
surname = "Рябухина"
print("Привет,", name, surname, "!")

#2.1
print("2.1. Составить алгоритм решения задачи для определения большего из двух вещественных чисел (не используя функцию min или max).")
a = float(input("Input a: "))
b = float(input("Input b: "))
if a > b:
    print(a)
else:
    print(b)

#2.2
print("2.2. Составить алгоритм решения задачи для определения меньшего из трех целых чисел (не используя функцию min или max). ")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
if a <= b:
    if a <= c:
        print(a)
    else:
        print(c)
elif b <= a:
    if b <= c:
        print(b)
    else:
        print(c)

#2.3
print("2.3. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого, не используя функцию min или max).")
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
if a <= b:
    if c <= a:
        print(a)
    elif c >= b:
        print(b)
    else:
        print(c)
elif b <= a:
    if c <= b:
        print(b)
    elif c >= a:
        print(a)
    else:
        print(c)



#2.4
print("2.4. Написать алгоритм определения четности/нечетности числа.")
n = float(input("Input n: "))
if n % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")

#2.5
print("2.5. Дано трехзначное натуральное число n. Имеется ли в нем цифра 1?")
n = int(input("Input n: "))
if n % 10 == 1:
    print("Yes")
elif n // 10 % 10 == 1:
    print("Yes")
elif n // 100 == 1:
    print("Yes")
else:
    print("No")

#2.6
print("2.6. Дано трехзначное натуральное число. Вычислить произведение ненулевых цифр этого числа.")
n = int(input("Input n: "))
a = 1
b = 1
c = 1
if n % 10 != 0:
    a = int(n % 10)
if n // 10 % 10 != 0:
    b = int(n // 10 % 10)
if n // 100 != 0:
    c = int(n // 100)
print(a * b * c)

#2.7
print("2.5. Составить алгоритм решения задачи для определения большей скорости: одно значение указано в километрах в час, а другое в метрах в секунду (1 м/с = 3,6 км/ч).")
V1 = int(input("Введите V1 (в км/ч): "))
V2 = int(input("Введите V2 (в м/с): "))
if V1 > V2 * 3.6:
    print("Большая скорость = ", V1, "км/ч")
else:
    print("Большая скорость = ", V2, "м/с")

#2.8
print("2.6. Написать программу определения размера стипендии. Пользователь вводит 3 натуральных числа: общее количество оценок, количество пятерок, количество четверок. Если все пятерки – стипендия 6000 руб., если одна четверка – 4500 руб., если две четверки – 3750 руб., если нет троек – 3000 руб., иначе – нет стипендии.")
n = int(input("Введите общее количество оценок: "))
p = int(input("Введите количество пятерок: "))
ch = int(input("Введите количество четверок: "))
if ch + p > n:
    print("Введены некорректные данные!")
elif p == n:
    print("Ваша стипендия = 6000 руб")
elif (p == n - 1) and (ch == 1):
    print("Ваша стипендия = 4500 руб")
elif (p == n - 2) and (ch == 2):
    print("Ваша стипендия = 3750 руб")
elif p + ch == n:
    print("Ваша стипендия = 3000 руб")
else:
    print("У Вас нет стипендии")

#2.9
print("2.7. Составить алгоритм решения задачи для определения большей площади, если известны радиус круга и сторона квадрата.")
r = int(input("Введите радиус круга: "))
b = int(input("Введите сторону квадрата: "))
if math.pi * r * r > b * b:
    print("Площадь круга больше и равна", math.pi * r * r)
else:
    print("Площадь квадрата больше и равна", b * b)

#2.10
print("2.8. Дана следующая функция y=f(x): y = 2x - 10, если x > 0; y = 0, если x = 0; y = 2 * |x| - 1, если x < 0. Требуется найти значение функции по переданному x (вводится пользователем).")
x = int(input("Введите x: "))
if x > 0:
    print("y =", 2 * x - 10)
elif x == 0:
    print("y =", x)
else:
    print("y =", 2 * math.fabs(x) - 1)

#2.11
print("2.9. Для данного x вычислить значение функции:.")
x = int(input("Введите x: "))
if x < -1:
    print("y =", 1 / x * x)
elif (x >= - 1) and (x < 2):
    print("y =", x * x)
elif x >= 2:
    print("y = ", 4)

#2.12
print("2.10 Даны действительные числа x, y вычислите u = 3*z*z - 2*z + 5")
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = 0
if x + y < 2:
    z = math.sqrt(x * x + y * y)
elif x + y == 8 or x + y == 3:
    z = 2 * x * y
elif x + y >= 10:
    z = x - y
else:
    z = 2 * x + 3 * y
print("u = ", 3 * z * z - 2 * z + 5)

#2.13
print("2.11. Составить алгоритм вывода названия дня недели по его порядковому номеру (1 – понедельник, 2 – вторник, 3 – среда, 4 – четверг, 5 – пятница, 6 – суббота, 7 – воскресенье, проверка вхождения числа в диапазон приветствуется).")
n = int(input("Введите порядковый номер: "))
if (n > 7) or (n < 1):
    print("Введены некорректные данные.")
elif n == 1:
    print("Понедельник")
elif n == 2:
    print("Вторник")
elif n == 3:
    print("Среда")
elif n == 4:
    print("Четверг")
elif n == 5:
    print("Пятница")
elif n == 6:
    print("Суббота")
elif n == 7:
    print("Воскресенье")

#2.14
print("2.12. Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.")
x = int(input("Введите координату по оси абсцисс: "))
y = int(input("Введите координату по оси ординат: "))
if x > 0:
    if y > 0:
        print("Точка принаджлежит I четверти")
    elif y < 0:
        print("Точка принаджелит IV четверти")
    else:
        print("Точка не принадлежит четверти")
elif x < 0:
    if y > 0:
        print("Точка принаджлежит II четверти")
    elif y < 0:
        print("Точка принаджелит III четверти")
    else:
        print("Точка не принадлежит четверти")
else:
    print("Точка не принаджелит четверти")

#2.15
print("2.13. Даны целые числа m, n. Если числа не равны, то заменить каждое из них одним и тем же числом, равным большему из исходных, а если равны, то заменить числа нулями.")
m = int(input("Введите m: "))
n = int(input("Введите n: "))
if m == n:
    m = 0
    n = 0
    print("m, n =", m , ",", n)
else:
    if m > n:
        n = m
        print("m, n =", m, ",", n)
    else:
        m = n
        print("m, n =", m, ",", n)
