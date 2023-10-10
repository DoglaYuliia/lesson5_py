# 1. Дано целое число (int). Определить сколько нулей в этом числе.

number = 275002756205700
count_noll = str(number).count('0')
print(count_noll)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля

number = 27500275620570000
noll_in_end = len(str(number)) - len(str(number).rstrip('0'))
print(noll_in_end)

#решение учителя
#noll_in_end = len(str(number)) - len(str(number).strip('0'))

# 3. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

my_str = '43 больше чем 34 но меньше чем 56'

sum_digits = 0
for symbol in my_str.split(' '):
    if symbol.isdigit():
        sum_digits += int(symbol)
print(sum_digits)


#решение учителя
numb_list = []
for word in my_str.split():
    if word.isdigit():
        numb_list.append(int(word))
result = sum(numb_list)
print(result)
# или одной строкой
result = sum([int(word) for word in my_str.split() if word.isdigit()])
print(result)

# 4. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'

l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index:r_index]
print(sub_str)

# решение учителя

res_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(res_str)

# 5. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['alfa', 'number', 'alphabet', 'union', 'beauti', 'apricot', 'Aaaa', 'aaa']
list_first_a = []

for symbol in my_list:
    if symbol[0] == 'a':
        list_first_a.append(symbol)
print(list_first_a)

# 6. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['alfa', 'opel', 'number', 'alphabet', 'union', 'beauti', 'apricot', 'Aaaa']
list_any_a = []

for symbol in my_list:
    if 'a' in symbol:
        list_any_a.append(symbol)
print(list_any_a)

# 7. Дан список my_list в котором могут быть как строки (type str) так и целые числа
# (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [88, 'opel', 'number', 33, 55, 'union', 77, 'apricot', 111, 'happy', 'aaa']
new_list = []

for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)

# 8. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = 'We are going to heiven'
my_list = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

# решение учителя

for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

# 9. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = 'qwerty 123455'
my_str_2 = '123455 6789 qwe'

my_str_1_set = set(my_str_1)
my_str_2_set = set(my_str_2)

intersection_list = list(my_str_1_set.intersection(my_str_2))
print(intersection_list, type(intersection_list))

# решение учителя
res_list = list(set(my_str_1).intersection(set(my_str_2)))
print(res_list)

# 10. Даны две строки. Создать список в который поместить те символы, которые есть в
# обеих строках,но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в
# каждой строке по одному разу

my_str_1 = 'aaaasdf1'
my_str_2 = 'asdfff2'
new_list = []

for symbol in my_str_1:
    if my_str_1.count(symbol) == 1:
        if my_str_2.count(symbol) == 1:
            new_list.append(symbol)
print(new_list)

# решение учителя
res_list = []
for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)

# 11. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = 'abcda'
new_list = []

for i in range(0, len(my_str), 2):
    symbol = my_str[i:i + 2]
    if len(symbol) == 1:
        new_list.append(symbol + "_")
    else:
        new_list.append(symbol)

print(new_list)

# решение учителя
my_str = 'abcda'

if len(my_str) % 2:
    my_str += '_'
res_list = []
for index in range(0, len(my_str), 2):
    res_list.append(my_str[index: index + 2])
print(res_list)

# в две строки

my_str = my_str + '_' if len(my_str) % 2 else my_str
res_list = [my_str[index: index + 2] for index in range(0, len(my_str), 2)]
print(res_list)