from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=256, verbose_name='name')

class Clothe(models.Model):
    # Clothe thype
    TOP = 0
    BOTTOM = 1
    SHOE = 2
    BLAZER = 3
    COAT = 4
    JACKET = 5
    TYPES = (
        (TOP, 'top'),
        (BOTTOM, 'bottom'),
        (SHOE, 'shoe'),
        (BLAZER, 'blazer'),
        (COAT, 'coat'),
        (JACKET, 'jacket'),
    )

    name = models.CharField(max_length=256, verbose_name="name")
    color = models.PositiveSmallIntegerField(verbose_name="color", choices=COLORS)
    type = models.PositiveSmallIntegerField(verbose_name='type', choices=TYPES)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.P
