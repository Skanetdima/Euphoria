from django.db import models

# Create your models here.
class UserAccount(models.Model):
    """Model representing users and their accounts"""
    email = models.EmailField(max_length=50, help_text="designer@gmail.com")
    password = models.CharField(max_length=50, help_text=" ")
    def __str__(self):
        """String for representing the Model Object."""
        return self.name

class Clothes(models.Model):
    """Model representing clothes and price on it"""
    cloth_amount = models.IntegerField(max_digits=30)
    cloth_name = models.CharField(max_length=40)

