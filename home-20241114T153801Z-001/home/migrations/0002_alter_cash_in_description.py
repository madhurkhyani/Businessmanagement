# Generated by Django 5.1.1 on 2024-10-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash_in',
            name='description',
            field=models.TextField(),
        ),
    ]
