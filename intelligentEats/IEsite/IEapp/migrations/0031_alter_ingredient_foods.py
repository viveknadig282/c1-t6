# Generated by Django 3.2.4 on 2021-11-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0030_alter_ingredient_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='foods',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
    ]
