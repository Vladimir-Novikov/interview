def type_of_number():
    number = input("Введите число: ")
    if number[0] in ["-", "+", "/", "*"]:  # убираем минус и прочие знаки
        number = number[1:]
    if number.isalpha():
        print("Введена буква")
    elif number.isdigit():
        print("Введено целое число")
    elif "," in number:
        print("Введено дробное число")
        print("Вместо точки использована запятая")
        left, right = number.split(",")
        if left == right:
            print("Совпадают")
            return True
        else:
            print("Не совпадают")
            return False
    else:
        print("Введено дробное число")
        left, right = number.split(".")
        if left == right:
            print("Совпадают")
            return True
        else:
            print("Не совпадают")
            return False


type_of_number()
