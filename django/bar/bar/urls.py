from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ListProductView.as_view(), name="product"),
    path(
        "product/<int:pk>/detail/",
        views.DetailListProductView.as_view(),
        name="product_detail",
    ),
]
