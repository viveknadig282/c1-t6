# Generated by Django 3.2.8 on 2021-11-06 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0024_auto_20211105_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='score',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='foods',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
    ]
