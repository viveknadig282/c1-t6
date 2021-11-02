# Generated by Django 3.2.8 on 2021-11-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ingredient_content',
            field=models.ManyToManyField(through='IEapp.ingredient_food', to='IEapp.Ingredients'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='within_food',
            field=models.ManyToManyField(through='IEapp.ingredient_food', to='IEapp.Food'),
        ),
    ]
