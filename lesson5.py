"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""

my_str = 'blablacar'
my_symbol = 'bla'

result = my_str.count(my_symbol)
print(result)

"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""

my_str = 'blablacar'
my_symbol = 'bla'
my_symbol_count = my_str.count(my_symbol)
# result = f"{my_symbol}\n" * my_symbol_count
# result = result.strip()
# print(result, "........")

for my_count in range(my_symbol_count):
    print(my_symbol)

"""
3) У вас есть переменная my_str, тип - str. 
Большая и маленькая буква считается как один символ.
Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.  
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""

my_str = "bla BLA car"
lower_str = my_str.lower()

unique_symbols = []
for symbol in lower_str:
    if symbol not in unique_symbols:
        unique_symbols.append(symbol)

unique_symbols_count = len(unique_symbols)
print(unique_symbols_count)

#короче с помощью set множества

my_str = "bla BLA car"
lower_str = my_str.lower()

unique_symbols = set(lower_str)
print(unique_symbols)

unique_symbols_count = len(unique_symbols)
print(unique_symbols_count)


#в одну строку

my_str = "bla BLA car"

unique_symbols_count = len(set(my_str.lower()))
print(unique_symbols_count)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# val_1 = 123
# val_2 = 100
# #val_1 = val_1 + val_2
# val_1 += val_2
# print(val_1)



my_str = "dsghoqvuylgwshiaruahfq"
my_list = []
print(id(my_list), my_list)
new_str = my_str[::2]
# for symbol in new_str:
#     my_list.append(symbol)

my_list += list(new_str)  # НЕ ТО ЖЕ САМОЕ, ЧТО my_list = my_list + list(new_str)  меняется id
print(id(my_list), my_list)

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
from string import ascii_lowercase

my_str = "dfvjktdh"
str_index = [6, 5, 7, 7, 4, 2, 3]
my_list = []

for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
print(my_list)

"""
6)
Дано целое число (тип int). Определить сколько цифр в этом числе.
"""
number = 29327456829
number_count = len(str(number))
print(number_count)

"""
7)
Дано целое число (тип int). Определить наибольшую цифру в этом числе.
"""

number = 232745682
number_max = max(str(number))
print(number_max)

"""
8)
Дано целое число (тип int). Составить число (int) с цифрами в обратном порядке.
"""

number = 232745682
# str_number = str(number)
# str_number = str_number[::-1]
result_number = int(str(number)[::-1])
print(result_number, type(result_number))

"""
9)
Дано целое число (тип int). Составить число с цифрами в порядке 
возрастания(убывания).
"""
number = 2327458745643310932457

numb_str = str(number)
sort_numb_list = sorted(numb_str)
new_numb = "".join(sort_numb_list)
result = int(new_numb)
print(result)

# по убыванию
numb_str = str(number)
sort_numb_list = sorted(numb_str, reverse=True)  #отличие, тут созласться новый объкт со старым именем
new_numb = "".join(sort_numb_list)
result = int(new_numb)
print(result)


# разница sort метод только списка, текущий объект останется самим собой
my_list = [3, 6, 1, 8]
my_list.sort(reverse = True)
print(my_list)

"""
10) Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и
my_list_2 через один, начиная с my_list_1.
а) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30]
my_result = []

for index in range(len(my_list_1)):
    # to_extend = [my_list_1[index], my_list_2[index]]
    # my_result.extend(to_extend)
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
print(my_result)
"""
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = [10, 20, 30, 40, 50]
my_result = []

min_len_lists = min(len(my_list_1), len(my_list_2))
tail = my_list_1[min_len_lists:] + my_list_2[min_len_lists:]

for index in range(min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
my_result.extend(tail)
print(my_result)


##############  ord()  chr()    ########################

print(ord("b"))
print(chr(98))

##############  генератовы списков (list comprehension)    ############

# alphabet_list = []
# for index_ascii in range(ord('a'), ord('z') +1):
#     alphabet_list.append(chr(index_ascii))

alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') +1)]
#похож на терн оператор, переписали цикл в одну строку
alphabet = ''.join(alphabet_list)
print(alphabet)



result = [x ** 2 for x in range(10)]
print(result)

result2 = [x ** 3 for x in range(10) if x % 2 == 0]
print(result2)


#поместить в список только то, что больше 10
my_list = [12, -45, 23, 5, 0, 21, 900]
res = []
for value in my_list:
    if value > 10:
        res.append(value)
print(res)

#генератор списка
res = [value for value in my_list if value > 10 and not value % 2]
print(res)


res = [str(value) * 20 for value in my_list if value > 10]
print(res)
#чтоб ответ был удобно в линии
res = [str(value) * 20 for value in my_list if value > 10]
[print(line) for line in res]
# for line in res:
#     print(line)


##############  МНОЖЕСТВА (set)    ########################

# множества (set) - изменяемый тип, только один представитель для
# какждого объекта, порядок не сохраняется

my_list = [6, 1, 2, 3, 4, 5, 5, 1, 3, '1', '1', 10, 55]

my_list_unique = list(set(my_list))  # убрать дубли в списке

my_set = set(my_list)

#добавить элемент
my_set.add(100)
print(my_set, type(my_set))

# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set,
# не принадлежащие ни одному из other.

my_str_1 = 'eysrfgrdgfnghfd'
my_str_2 = 'swedfrtguyhijokpiuhygf'

my_str_1_set = set(my_str_1)
my_str_2_set = set(my_str_2)

same_symbols = my_str_1_set.intersection(my_str_2_set)
print(same_symbols)

all_symbols = my_str_1_set.union(my_str_2_set)
print(all_symbols)

difference_symbols = my_str_1_set.difference(my_str_2_set)
print(difference_symbols) # только эти симыолы есть в первой строке, а во второй нет

