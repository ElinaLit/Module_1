# Задание 1
immutable_var = ("photo", True, 5, 3)
print(immutable_var)

# Задание 2
# immutable_var[2] = 200
# print(immutable_var)
# изменить значение объекта в кортеже невозможно

# Задание 3
mutable_list = [1, 3, 5, "Everest", False]
mutable_list.append("Nepal")
mutable_list.extend(["George Orwell", 1986])
mutable_list.remove(1)
print(mutable_list)
