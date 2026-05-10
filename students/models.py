from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100)

    age = models.IntegerField(
        validators=[
            MinValueValidator(16),
            MaxValueValidator(60)
        ]
    )

    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name