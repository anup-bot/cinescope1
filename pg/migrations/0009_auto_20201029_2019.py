# Generated by Django 3.1.2 on 2020-10-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0008_auto_20201029_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='price',
            field=models.DecimalField(decimal_places=0, default='', max_digits=10),
        ),
    ]