# Задание 1
my_dict = {'Denis': 1976, 'Mila': 1998, 'Kira': 2015, 'Staisy': 2003}
print(my_dict)
print(my_dict.get('Kira'))
print(my_dict.get('Nina', 'Такого значения нет'))
my_dict.update({'Alex': 1996, 'Dima': 2011})
a = my_dict.pop('Mila')
print(a)
print(my_dict)

# Задание 2
my_set = {1, 3, 5, 7, 9, 2, 4, 1, 3, 'Nika', True, 'Zima', True, 'Nika'}
print(my_set)
my_set.add((8, 4.5, 'Leto'))
print(my_set)
my_set.remove(2)
print(my_set)
