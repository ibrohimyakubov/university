# Generated by Django 3.1.7 on 2021-05-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_bookrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='returned_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]