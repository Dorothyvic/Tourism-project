from django.db import models


class Tour(models.Model):
    image = models.ImageField(blank=True, null=True, default='1.jpg')
    header = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.header


class Story(models.Model):
    image = models.ImageField(blank=True, null=True, default='1.jpg')
    header = models.CharField(max_length=100)
    paragraph = models.TextField()

    def __str__(self):
        return self.header


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()


