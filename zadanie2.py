films_dict = {"first": "Terminator", "second": "Aliens", "third": "Pirates of the Caribbean", "fourth": "Bladerunner 2049", "fifth": "The Matrix"}
films_spisok = ["Terminator", "Aliens", "Pirates of the Caribbean", "Bladerunner 2049", "The Matrix"]
films_mnozhestvo = {"Terminator", "Aliens", "Pirates of the Caribbean", "Bladerunner 2049", "The Matrix"}

if "second" in films_dict: # Поиск элемента в словаре
    print("Этот элемент есть в словаре:", films_dict["second"])
else:
    print("Такого элемента нет в словаре")

print(films_dict.get("second", "Такого элемента нет в словаре")) # Поиск элемента в словаре (вариант 2)

if "Aliens" in films_spisok: # Поиск элемента в списке
    print("Этот элемент есть в списке")
else:
    print("Такого элемента нет в списке")

if "Aliens" in films_mnozhestvo: # Поиск элемента в множестве
    print("Этот элемент есть в множестве")
else:
    print("Такого элемента нет в множестве")

# С точки зрения удобства, на мой взгляд, наименее удобным способом описать элементы является словарь, поскольку требуется дополнительно
# вводить значение ключа элемента, что увеличивает время написания кода. На мой взгляд, удобнее всего пользоваться списком, поскольку
# он менее затратный с точки зрения написания кода. При выводе элементы списка располагаются ровно в том порядке,в котором находились, в отличие от множества,
# при выводе которого элементы располагаются каждый раз в случайном порядке. Также списки удобнее тем, что потребляют меньше памяти, в отличие от словарей и множеств:

print("Потребление памяти словарем:", films_dict.__sizeof__())
print("Потребление памяти списком:", films_spisok.__sizeof__())
print("Потребление памяти множеством:",films_mnozhestvo.__sizeof__())
