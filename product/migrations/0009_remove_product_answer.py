# Generated by Django 3.2.14 on 2022-08-04 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20220804_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='answer',
        ),
    ]
