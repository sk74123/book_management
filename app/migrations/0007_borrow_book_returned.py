# Generated by Django 4.1.2 on 2022-10-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_borrow_book_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow_book',
            name='Returned',
            field=models.BooleanField(default=False),
        ),
    ]
