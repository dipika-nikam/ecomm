# Generated by Django 4.0.6 on 2022-08-04 07:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogs_descripation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='descripation',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
