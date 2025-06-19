from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    split_type = models.CharField(max_length=20)  # 'equal' or 'percentage'

class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.FloatField(null=True, blank=True)
    amount_owed = models.FloatField()
