from django import forms
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import GoodItem
from .forms import GoodItemForm
from django.core import serializers


def index(request):
    all_goods = GoodItem.objects.all()
    if request.method == "POST":
        form = GoodItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = GoodItemForm()
    context = {"page_header": "Товары", "goods": all_goods, "form": form}
    return render(request, template_name="index.html", context=context)


# def ajax_handler(request):
#     all_goods = GoodItem.objects.all()
#     data = serializers.serialize("json", all_goods)
#     return HttpResponse(data, content_type="text/html")


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
    context = {
        "page_header": "Добавление товаров",
        "form": form,
        "error": error,
    }
    return render(request, template_name="add_product.html", context=context)
