from tkinter import CASCADE
from django.db import models

from django.forms import IntegerField






class Amount(models.Model):
    amount = IntegerField()

    def __str__(self):
        return self.amount



class SponsorJ(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    payment_amount = models.ForeignKey(Amount , on_delete=models.CASCADE)
    name_com = models.CharField(max_length=200)

    class Meta:
        ordering = ['full_name', 'name_com']

    def __str__(self):
        return self.full_name






class SponsorY(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    payment_amount = models.ForeignKey(Amount, on_delete=models.CASCADE)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name






class type_degree(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type





class Otm(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name




class Student(models.Model):
    full_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    univer_name = models.ForeignKey(Otm, on_delete=models.CASCADE)
    degree = models.ForeignKey(type_degree, on_delete=models.CASCADE)
    contract_amount = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.full_name} {self.degree} {self.univer_name} {self.contract_amount}'