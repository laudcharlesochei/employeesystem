from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name
