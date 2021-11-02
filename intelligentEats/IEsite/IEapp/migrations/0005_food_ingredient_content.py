# Generated by Django 3.2.8 on 2021-10-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0004_remove_food_ingredient_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ingredient_content',
            field=models.ManyToManyField(through='IEapp.ingredient_food', to='IEapp.ingredients'),
        ),
    ]
