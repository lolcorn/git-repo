def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, b)
    print(c)
    print('Без аргументов')


print_params()
print_params(2, 'точка', "Старт")
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'Залип', False]
values_dict = {'a': 3, 'b': 'проверка', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
