from django.urls import path

from .views import GoodList, GoodsListView, add_product, goods_list

urlpatterns = [
    # path("", index),
    path("", goods_list),
    path("add/", add_product),
    # path("ajax_test/", ajax_test),
    # path("goods_cbv/", GoodList.as_view()),
    # path("goods_cbv2/", GoodsListView.as_view()),
]
