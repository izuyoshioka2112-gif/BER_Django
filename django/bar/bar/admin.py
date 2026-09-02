from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.register(Product)
# これを書くことで管理画面から商品を編集できる
