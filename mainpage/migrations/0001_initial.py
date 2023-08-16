# Generated by Django 4.2.4 on 2023-08-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_amount', models.IntegerField(blank=True, null=True)),
                ('cloth_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='designer@gmail.com', max_length=50)),
                ('password', models.CharField(help_text=' ', max_length=50)),
            ],
        ),
    ]
