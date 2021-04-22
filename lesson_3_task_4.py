import os
import random


def open_file(link):
    print(f"Чтение из файла {link}: ")
    with open(link, encoding="UTF-8") as f:
        for i in f.readlines():
            print(i.strip())


def create_file(name):
    link = os.path.join(os.getcwd(), name)  # формируем ссылку для передачи во 2 функцию (чтения)
    letters = "abcdefghijklmnopqrstuvwxyz"  # набор для формирования случайных символов
    abc_list = [x for x in random.choices(letters, k=10)]  # генерация случайных букв
    num_list = [x for x in random.choices(range(100), k=10)]  # генерация случайных цифр
    random_strings = list(zip(abc_list, num_list))  # список строк из случайных букв и цифр
    try:  # пробуем создать через x, чтобы не затереть файл
        with open(name, "x", encoding="UTF-8") as f:
            for line in random_strings:
                f.writelines(str(line[0]) + str(line[1]) + "\n")
    except FileExistsError:
        print("*** Файл с таким именем уже существует ***\nФайл открыт на дозапись")
        with open(name, "a", encoding="UTF-8") as f:
            for line in random_strings:
                f.writelines(str(line[0]) + str(line[1]) + "\n")

    open_file(link)


create_file("115.txt")
