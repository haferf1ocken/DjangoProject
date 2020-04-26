from django.db import models


class Deal(models.Model):
    customer = models.CharField(verbose_name='логин покупателя', max_length=100)
    item = models.CharField(verbose_name='наименование товара', max_length=200)
    total = models.IntegerField(verbose_name='сумма сделки')
    quantity = models.IntegerField(verbose_name='количество товара')
    date = models.DateTimeField(verbose_name='дата и время регистрации сделки')

    def __str__(self):
        return self.customer and self.item

