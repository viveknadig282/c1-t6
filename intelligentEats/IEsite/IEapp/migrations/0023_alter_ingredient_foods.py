# Generated by Django 3.2.8 on 2021-11-06 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0022_alter_ingredient_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='foods',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
    ]
