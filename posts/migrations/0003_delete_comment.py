# Generated by Django 4.1 on 2023-02-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
