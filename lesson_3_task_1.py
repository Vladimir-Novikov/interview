import os


def getting_name(name):
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:  # перебор каталогов
            # print("Каталог:", os.path.join(dirpath, dirname))
            for filename in filenames:  # перебор файлов
                # print("Файл:", os.path.join(dirpath, filename))
                if filename == name:
                    # print("Файл:", os.path.join(dirpath, filename))
                    relative_path = os.path.join(dirpath, filename)  # относительный путь с ./
                    full_path = os.getcwd() + relative_path[1:]  # добавляем к нему cwd
                    name = os.path.basename(relative_path).split(".")[0]  # имя файла без расширения
                    return f"Файл найден, путь: {full_path},\nимя без расширения: {name}"
    name = name.split(".")[0]
    return f"*** Файл не найден***,\nимя без расширения: {name}"


print(getting_name("115.txt"))
