from .models import GoodItem
from django.forms import ModelForm, TextInput, widgets, DateTimeInput, NumberInput


class GoodItemForm(ModelForm):
    class Meta:
        model = GoodItem
        fields = ["title", "price", "modified_at", "vendor"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Название товара"}),
            "modified_at": DateTimeInput(attrs={"class": "form-control", "placeholder": "Дата изменений"}),
            "price": NumberInput(attrs={"class": "form-control", "placeholder": "Цена"}),
            "vendor": TextInput(attrs={"class": "form-control", "placeholder": "Поставщик"}),
        }
