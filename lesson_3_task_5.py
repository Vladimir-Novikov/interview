import os
import random
import re


def open_file(link):
    print(f"Чтение из файла {link}: ")
    rand_sign = "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890"))  # случайный символ для поиска в тексте
    with open(link, encoding="UTF-8") as f:
        lines = f.readlines()
        for i in lines:
            index = i.find(rand_sign)
            if index == -1:
                index = "Нет символа в строке"
            all_matches = re.findall(rand_sign, i)
            print(
                i.strip(),
                f"Индекс первого вхождение в строку символа {rand_sign}: {index}, Все вхождения: {all_matches}",
            )

    print("\nЗначения после замены: \n")
    with open(
        link, "w+", encoding="UTF-8"
    ) as f:  # открываем в режиме w+ и полностью перезаписываем файл, и далее читаем его
        for i in lines:
            if index == -1:
                f.write(i)
            f.write(re.sub(rand_sign, " ** NEW_value ** ", i))
        f.seek(0)  # перевод указателя в начало документа
        lines = f.readlines()
        for i in lines:
            print(i.strip())

        print("\nСтроки, без пробелов в тексте:\n")
        f.seek(0)
        for i in lines:
            if re.match(r"^\S+[^\s]$", i):
                print(i.strip())


def create_file(name):
    link = os.path.join(os.getcwd(), name)  # формируем ссылку для передачи во 2 функцию (чтения)
    letters = "abcdefghijklmnopqrstuvwxyz "  # набор для формирования случайных символов + пробел
    word_list = []
    while len(word_list) < 10:  # пока не наберем 10 слов в словарь
        new_word = "".join(random.choices(letters, k=random.randint(2, 15)))  # длина слова от 2 до 15 символов
        word_list.append(new_word)
    num_list = [x for x in random.choices(range(100), k=10)]  # генерация случайных цифр
    random_strings = list(zip(word_list, num_list))  # список строк из случайных букв и цифр
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
