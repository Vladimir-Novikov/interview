class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # получаем доступ к _переменным в родительском классе
    def get_parent_data(self):
        return f"{self._name} {self._price}"

    def set_price(self, price):  # установка цены
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):  # добавление аргумента discount
        super().__init__(name, price)
        self.discount = discount

    # тк доступ к _переменным нужно реализовать в родительском классе - отсюда убрал
    # def get_parent_data(self):
    #     return f"{self.name} {self.price}"

    def get_info(self):  # полиморфизм - получаем имя
        return self._name

    def __str__(self):
        if self.discount > 90:  # если скидка больше 90% - выводим сообщение и цену без скидки
            return f"Скидка больше 90 % Ошибка \n{self._name} {self._price}"
        new_price = self._price * (1 - (self.discount / 100))
        return f"{self._name} {new_price:.2f}"


class ItemDiscountReport_2(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_info(self):  # полиморфизм - получаем цену
        return self._price


instance_1 = ItemDiscount("фен", 3500)
print(
    "Информация из родительского класса, полученная в дочернем классе:\n",
    ItemDiscountReport.get_parent_data(instance_1),
)
instance_1.set_price(4599)  # установка цены
print("Цена после установки новой цены: ", instance_1._price)
print("Цена после установки новой цены: ", ItemDiscountReport.get_parent_data(instance_1))
instance_2 = ItemDiscountReport("холодильник", 25499, 10)
instance_3 = ItemDiscountReport("холодильник", 25499, 95)
print("Цена со скидкой: ", instance_2)
print(instance_3)
instance_4 = ItemDiscountReport_2("утюг", 5000, 5)
print("Ф-ция 1 метод 1", instance_2.get_info())
print("Ф-ция 1 метод 2", ItemDiscountReport.get_info(instance_3))
print("Ф-ция 2 метод 1", instance_4.get_info())
print("Ф-ция 2 метод 2", ItemDiscountReport_2.get_info(instance_4))
