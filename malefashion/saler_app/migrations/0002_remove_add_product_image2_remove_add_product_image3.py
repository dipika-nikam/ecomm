# Generated by Django 4.0.6 on 2022-08-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='add_product',
            name='image3',
        ),
    ]
