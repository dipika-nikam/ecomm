# Generated by Django 4.0.6 on 2022-08-09 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler_app', '0002_remove_add_product_image2_remove_add_product_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='saler_app.add_product')),
            ],
        ),
    ]
