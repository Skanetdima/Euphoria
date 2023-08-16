from django.contrib import admin
from .models import Clothes, UserAccount
# Register your models here.
@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('clothes_name','clothes_amount', 'clothes_price')
    pass

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    fields = ['email', 'password']
    pass
