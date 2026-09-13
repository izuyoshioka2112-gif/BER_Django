from django.contrib import admin
from .models import Product, Staff, Order, OrderItem

# Register your models here.


# みやすくした
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_available")
    list_editable = ("is_available",)


class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "is_available")
    list_editable = ("is_available",)


admin.site.register(Product, ProductAdmin)
# これを書くことで管理画面から商品を編集できる
admin.site.register(Staff, StaffAdmin)
# ↓この下はなくても良い
admin.site.register(Order)
admin.site.register(OrderItem)
