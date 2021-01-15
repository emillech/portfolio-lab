from django.db import models
from django.conf import settings


TYPES = (
    (1, 'Foundation'),
    (2, 'Non-governmental organization'),
    (3, 'Local collection')
)


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):

        return f'{self.name}'


class Institution(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):

        return f'{self.name}'


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )


