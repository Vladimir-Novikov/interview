from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from .models import GoodItem
from .forms import GoodItemForm


def goods_list(request):
    all_goods = GoodItem.objects.all()
    # goods_str = ", ".join(str(good) for good in all_goods)
    context = {
        "page_header": "Товары",
        "goods": all_goods,
    }
    return render(request, template_name="goods_list.html", context=context)


def add_product(request):
    error = ""
    if request.method == "POST":
        form = GoodItemForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
        else:
            error = "Форма заполнена некорректно"
    form = GoodItemForm()
    context = {"page_header": "Добавление товаров", "form": form, "error": error}
    return render(request, template_name="add_product.html", context=context)


class GoodList(TemplateView):
    template_name = "goods_list.html"

    def get_context_data(self, **kwargs):
        all_goods = GoodItem.objects.all()
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_header": "Все товары",
                "goods": all_goods,
            }
        )
        return context


class GoodsListView(ListView):
    template_name = "goods_list.html"
    model = GoodItem
    context_object_name = "goods"
