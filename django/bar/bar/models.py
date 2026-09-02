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
