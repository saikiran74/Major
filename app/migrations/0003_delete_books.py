# Generated by Django 4.0.2 on 2022-02-05 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_books_delete_contactus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]