# Generated by Django 4.2.7 on 2023-12-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Bio do Carro'),
        ),
    ]
