from django.db import models

# Create your models here.
class UserAccount(models.Model):
    """Model representing users and their accounts"""
    email = models.EmailField(max_length=50, help_text="designer@gmail.com")
    password = models.CharField(max_length=50, help_text=" ")
    def __str__(self):
        """String for representing the Model Object."""
        return f'{self.email} {self.password}'

class Clothes(models.Model):
    """Model representing clothes and price on it"""
    clothes_amount = models.IntegerField(blank=True, null=True)
    clothes_name = models.CharField(max_length=40)
    clothes_price = models.IntegerField(blank=True, null=True)
    def __str__(self):
        """String for representing the Model Object."""
        return f'{self.clothes_amount} {self.clothes_name}'
