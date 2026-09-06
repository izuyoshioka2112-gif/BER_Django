from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ListProductView.as_view(), name="product"),
    path(
        "product/<int:pk>/detail/",
        views.DetailListProductView.as_view(),
        name="product_detail",
    ),
    path("cart/add/", views.add_to_cart_api, name="add_to_cart_api"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/update/", views.update_cart_api, name="update_cart_api"),
    path("cart/remove/", views.remove_from_cart_api, name="remove_from_cart_api"),
    path("order/confirm/", views.order_confirm_view, name="order_confirm"),
    path("order/done/", views.order_done_view, name="order_done"),
]

# PHOTO
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
