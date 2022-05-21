a = 0 # Посчитать сумму ряда 0 - 88888888
for i in range(0, 88888888):
    a = i + a
print(a)

spisok = [3, 4, 56, 100, 2, 2, 3] # Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
print(sum([3, 4, 56, 100, 2, 2, 3])/7)

string_1 = "asdxfghyxyx" # Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
print(string_1.replace("x", "y"))

spisok_2 = [3, 4, 56, 100, 15, 2, 20, 30] #Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5.
multiple = 1
for s in spisok_2:
    if s%5 == 0 or s%3 == 0:
        multiple *= s
print(multiple)

string_2 = "asdxfghyxyx" # Заменить все буквы "х" на "у" в исходной строке без использования дополнительной строки.
print(string_2.replace("x", "y"))
