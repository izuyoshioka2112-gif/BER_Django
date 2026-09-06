from django.db import models

# Create your models here.

CATEGORY = (("snack"), " スナック"), (("drink"), "ドリンク")


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return self.name
    # これでnameのデータだけ項目欄に表示される

class Staff(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.IntegerField()
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    # スタッフクラスと紐付け、スタッフがいない場合注文のスタッフの欄だけをヌルにする（いなくても動くために）
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # もしスタッフがいなくてヌルでも全体の操作（削除など）はそのまま動くように指示
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 注文された商品は管理画面から消せないように守ってる
    quantity = models.IntegerField()
