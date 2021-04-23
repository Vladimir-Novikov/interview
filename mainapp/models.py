from django.db import models


class GoodItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="Изменено")
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)
    vendor = models.TextField(verbose_name="Поставщик")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка товара"
        verbose_name_plural = "Карточки товаров"
