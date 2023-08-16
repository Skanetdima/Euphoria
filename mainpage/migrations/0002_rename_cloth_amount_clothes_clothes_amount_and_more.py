# Generated by Django 4.2.4 on 2023-08-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='cloth_amount',
            new_name='clothes_amount',
        ),
        migrations.RenameField(
            model_name='clothes',
            old_name='cloth_name',
            new_name='clothes_name',
        ),
        migrations.AddField(
            model_name='clothes',
            name='clothes_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
