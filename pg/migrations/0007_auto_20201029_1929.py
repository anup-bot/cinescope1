# Generated by Django 3.1.2 on 2020-10-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0006_auto_20201029_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='price',
            field=models.DecimalField(decimal_places=10, default='', max_digits=19),
        ),
    ]