# Generated by Django 3.2.8 on 2021-11-06 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0021_auto_20211105_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='foods',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
    ]
