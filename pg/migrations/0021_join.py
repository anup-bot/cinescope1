# Generated by Django 3.1.3 on 2020-11-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0020_auto_20201101_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
            ],
        ),
    ]