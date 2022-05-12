from django.db import models


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.TextField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.TextField(max_length=100, default=None)
    image = models.ImageField
    serial_no = models.CharField(max_length=100, default=None)
    specification = models.TextField(max_length=100, default=None)
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
