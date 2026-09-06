from django.contrib import admin
from .models import Product, Staff, Order, OrderItem

# Register your models here.

admin.site.register(Product)
# これを書くことで管理画面から商品を編集できる
admin.site.register(Staff)

# ↓この下はなくても良い
admin.site.register(Order)
admin.site.register(OrderItem)