# Generated by Django 4.1.2 on 2022-10-08 14:08

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issued_on', models.DateField(auto_now_add=True)),
                ('Submit_by', models.DateField(default=app.models.expiry)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('Reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reader')),
            ],
        ),
    ]
