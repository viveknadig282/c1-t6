# Generated by Django 3.2.8 on 2021-10-24 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0002_scraper_articles_ingredients_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ingredient_content',
            field=models.ManyToManyField(through='IEapp.ingredient_food', to='IEapp.ingredients'),
        ),
        migrations.AddField(
            model_name='ingredient_food',
            name='Food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.food'),
        ),
        migrations.AddField(
            model_name='ingredient_food',
            name='Ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.ingredients'),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='within_food',
            field=models.ManyToManyField(through='IEapp.ingredient_food', to='IEapp.food'),
        ),
    ]