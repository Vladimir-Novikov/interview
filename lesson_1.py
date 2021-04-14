def multiplication_table(a, b):
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print(f"{i} x {j} = {i * j}")


def num_input():
    # exit = False     лишнее условие
    while True:  # замена exit на True
        numbers = input("Введите 2 целых числа через пробел (или q для выхода): ").split()[:2]
        # if numbers[0] == "q" or numbers[0] == "й": замена на то, входит ли значение в массив
        if numbers[0] in ["q", "й"]:
            # exit = True
            break
        if len(numbers) < 2:
            print("Нужно ввести 2 числа")
            continue
        try:
            int(numbers[0])
            int(numbers[1])
        except ValueError:
            print("Нужно вводить целые числа")
            continue

        multiplication_table(int(numbers[0]), int(numbers[1]))


num_input()
