from django.db import models

class Pizza(models.Model):
    SHAPE_CHOICES = (
        ('square', 'Square'),
        ('regular', 'Regular'),
    )
    SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    )

    name = models.CharField(max_length=20)
    toppings = models.CharField(max_length=100)
    shape = models.CharField(max_length=10,
                             choices=SHAPE_CHOICES,
                             default='regular')
    size = models.CharField(max_length=10,
                              choices=SIZE_CHOICES,
                              default='medium')

    def __str__(self):
        return self.name
