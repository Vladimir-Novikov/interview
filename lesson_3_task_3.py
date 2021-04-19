key_list_1 = [chr(x) for x in range(ord("a"), ord("h") + 1)]
value_list_1 = [x for x in range(1, 27)]

key_list_2 = [chr(x) for x in range(ord("a"), ord("z") + 1)]
value_list_2 = [x for x in range(1, 15)]


def my_dict(keys, values):
    copy_value_list = values[:]  # создаем копию исходного списка, чтобы его не менять
    while len(keys) > len(copy_value_list):
        copy_value_list.append(None)
    new_dict = {key: value for key, value in zip(keys, copy_value_list)}
    return new_dict


print("*** Вариант 1 - ключей меньше, чем значений: ***\n", my_dict(key_list_1, value_list_1))

print("*** Вариант 2 - ключей больше, чем значений: *** \n", my_dict(key_list_2, value_list_2))
