#1
# 1. Даны строки S и S0. Найти количество вхождений строки S0 в строку S.
s = input('Введите строку: ')
s0 = input('Введите подстроку: ')
print(s.count(s0))  # для не перекрывающихся строк
count = 0
start = 0
i = -1
while True:  # для перекрывающихся строк (абабабабабабабаб)
    i = s.find(s0, i+1)
    if i == -1:
        print(count)
        break
    count += 1


#2
# 2. Даны строки S и S0. Удалить из строки S первую подстроку, совпадающую с S0. Если совпадающих подстрок нет,
# то вывести строку S без изменений.
s = input('Введите строку: ')
s0 = input('Введите подстроку: ')
if s.find(s0) >= 0:
    print(s.replace(s0, '', 1))
else:
    print(s)

#3
# 3. Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку S2.
s = input('Введите строку: ')
s1 = input('Введите строку1: ')
s2 = input('Введите строку2: ')
tmp = ''
if s.rfind(s) >= 0:
    s = s[:s.rfind(s1):]  # режем строку на две (начало (от 0 до индекса, на котором встречается искомая подстрока)
    new_s = s[s.rfind(s1)::]  # от индекса искомой подстроки до конца
    print(s + new_s.replace(s1, s2, 1))
else:
    print(s)


#4
# 4. Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку, расположенную между первым и вторым
# пробелом исходной строки. Если строка содержит только один пробел, то вывести пустую строку.
s = input('Введите строку: ')
i1 = s.find(' ')
i2 = s.find(' ', i1+1)
if i1 >= 0 and i2 >= 0:
    print(s[i1:i2:])
else:
    print('')


#5
# 5. Дана строка, содержащая по крайней мере один символ пробела.
# Вывести подстроку, расположенную между первым и последним пробелом исходной строки. Если строка содержит только один
# пробел, то вывести пустую строку.
s = input('Введите строку: ')
i1 = s.find(' ')
i2 = s.rfind(' ')
if i1 >= 0 and i2 >= 0:
    print(s[i1:i2:])
else:
    print('')


#6
# 6.Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими).Найти количество слов в строке
s = input('Введите строку: ')
s = s.split()
print(len(s))


#7
# 7. Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими)
# Найти количество слов, которые начинаются и заканчиваются одной и той же буквой.
s = input('Введите строку: ')
s = s.split()
count = 0
for i in range(len(s)):
    tmp = s[i]
    if tmp[0] == tmp[len(tmp)-1]:
        count += 1
print(count)


#8
# 8. Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими)
# Найти количество слов, которые содержат хотя бы одну букву «А».
s = input('Введите строку: ')
s = s.split()
count = 0
for i in range(len(s)):
    tmp = s[i]
    for k in range(len(tmp)):
        if tmp[k] == 'А':
            count += 1
            break
print(count)


#9
# 9. Дана строка-предложение с избыточными пробелами между  словами.
# Преобразовать ее так, чтобы между словами был ровно один пробел.
s = input('Введите строку: ')
s = s.split()
print(' '.join(s))


#10
# 10.Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими).
# Найти длину самого короткого слова.
s = input('Введите строку: ')
s = s.split()
mn = 10000
for i in range(len(s)):
    tmp = s[i]
    if len(tmp) < mn:
        mn = len(tmp)
print(mn)


#11
# 11.Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими)
# Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы на символ «.» (точка).
# Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У.». Количество пробелов между словами не изменять.
s = input('Введите строку: ')
new_s = ''
df = s[0]
new_s += s[0]
for i in range(1, len(s)):
    if s[i] != ' ' and df == '':
        df = s[i]
        new_s += s[i]
    if s[i] != ' ' and s[i-1] != ' ':
        if s[i] == df:
            new_s += '.'
        else:
            new_s += s[i]
    else:
        if s[i] == ' ':
            df = ''
            new_s += s[i]
print(new_s)


#12
# 12.Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами(одним или несколькими)
# Вывести строку, содержащую эти же слова, разделенные одним пробелом и расположенные в алфавитном порядке.
s = input('Введите строку: ')
s = s.split()
s.sort()
new_s = ' '.join(s)
print(new_s)


#13
# 13.Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке знаков препинания.
s = input('Введите строку: ')
prep = '!@#$%^&*().,?"{}[]:-_'
count = 0
for i in range(len(s)):
    if s[i] in prep:
        count += 1
print(count)



#14
# 14.Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке гласных букв.
s = input('Введите строку: ')
s = s.lower()
gl = 'аеёиоуыэюя'
count = 0
for i in range(len(s)):
    if s[i] in gl:
        count += 1
print(count)


#15
# 15.Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение.
# Выделить из этой строки имя файла (без расширения).
s = input('Введите строку: ')
i = s.rfind('.')
k = s.rfind('\\') + 1  # не включаем слеш (сдвигаемся сразу на первый символ названия файла
print(s[k:i:])


#16
# 16.Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение.
# Выделить из этой строки расширение файла (без предшествующей точки).
s = input('Введите строку: ')
i = s.rfind('.') + 1  # не включаем точку (сдвигаемся сразу на первыц символ названия расширения)
print(s[i::])


#17
# 17.Дана строка, содержащая полное имя файла. Выделить из этой строки название первого каталога (без символов «\»).
# Если файл содержится в корневом каталоге, то вывести символ «\».
s = input('Введите строку: ')
i = s.find('\\') + 1
k = s.find('\\', i)
if k < 0:
    print('\\')
else:
    print(s[i:k:])



#18
# 18.Дана строка-предложение на русском языке. Зашифровать ее, выполнив циклическую замену каждой буквы на следующую за
# ней в алфавите и сохранив при этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т. д.).
# Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки препинания и пробелы не изменять.
s = input('Введите строку: ')
new_s = ''
for i in range(len(s)):
    if 1040 < ord(s[i]) < 1103:
        if s[i] == 'Я':
            new_s += 'А'
        elif s[i] == 'я':
            new_s += 'а'
        else:
            new_s += chr(ord(s[i]) + 1)
    else:
        new_s += s[i]
print(new_s)


#19
# 19.Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать строку, выполнив циклическую замену
# каждой буквы на букву того же регистра, расположенную в алфавите на K-й позиции после шифруемой буквы
# (например, для K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.).
# Букву «ё» в алфавите не учитывать, знаки препинания и пробелы не изменять.
s = input('Введите строку: ')
k = int(input('Введите K: '))
new_s = ''
for i in range(len(s)):
    if 1040 <= ord(s[i]) <= 1071:
        if ord(s[i]) + k > 1071:
            new_s += chr(1039 + (ord(s[i]) + k - 1071))
        else:
            new_s += chr(ord(s[i]) + k)
    elif 1072 <= ord(s[i]) <= 1103:
        if ord(s[i]) + k > 1103:
            new_s += chr(1071 + (ord(s[i]) + k - 1103))
        else:
            new_s += chr(ord(s[i]) + k)
    else:
        new_s += s[i]
print(new_s)


#20
# 20.Дано зашифрованное предложение на русском языке(способ шифрования описан в предыдущем задании) и кодовое смещение K
# (0 < K < 10). Расшифровать предложение.
s = input('Введите строку: ')
k = int(input('Введите K: '))
new_s = ''
for i in range(len(s)):
    if 1040 <= ord(s[i]) <= 1071:
        if ord(s[i]) - k < 1040:
            new_s += chr(1072 - (1040 - (ord(s[i]) - k)))
        else:
            new_s += chr(ord(s[i]) - k)
    elif 1072 <= ord(s[i]) <= 1103:
        if ord(s[i]) - k < 1072:
            new_s += chr(1104 - (1072 - (ord(s[i]) - k)))
        else:
            new_s += chr(ord(s[i]) - k)
    else:
        new_s += s[i]
print(new_s)


#21
# 21.Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
# Если скобки расставлены правильно (то есть каждой открывающей соответствует закрывающая скобка того же вида), то
# вывести число 0. В противном случае вывести или номер позиции, в которой расположена первая ошибочная скобка, или,
# если закрывающих скобок не хватает, число –1.
s = input('Введите строку:')
sk1 = sk2 = sk3 = 0
for i in range(len(s)):
    if s[i] == '(':
        sk1 += 1
    if s[i] == ')':
        sk1 -= 1
    if s[i] == '[':
        sk2 += 1
    if s[i] == ']':
        sk2 -= 1
    if s[i] == '{':
        sk3 += 1
    if s[i] == '}':
        sk3 -= 1
    if sk1 + sk2 + sk3 < 0:
        print(i)
        break
skk = sk1 + sk2 + sk3
if skk == 0:
    print(0)
if skk > 0:
    print(-1)


