# Generated by Django 4.0.2 on 2022-02-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=200)),
                ('BookTitle', models.CharField(max_length=200)),
                ('BookAuthor', models.CharField(max_length=500)),
                ('YearOfPublication', models.CharField(max_length=500)),
                ('Publisher', models.CharField(max_length=500)),
                ('ImageURLS', models.CharField(max_length=500)),
                ('ImageURLM', models.CharField(max_length=500)),
                ('ImageURLL', models.CharField(max_length=500)),
            ],
        ),
    ]
