# Generated by Django 3.0.7 on 2020-07-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
