# Generated by Django 3.2.8 on 2021-11-02 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0007_alter_ingredient_food_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50000)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientFood',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.food')),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='within_food',
        ),
        migrations.RenameModel(
            old_name='scraper_articles',
            new_name='ScraperArticle',
        ),
        
        migrations.AddField(
            model_name='ingredient',
            name='within_food',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
        migrations.AlterField(
            model_name='food',
            name='ingredient_content',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Ingredient'),
        ),
        migrations.AlterField(
            model_name='scraperarticle',
            name='ingredients_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.ingredient'),
        ),
    ]
