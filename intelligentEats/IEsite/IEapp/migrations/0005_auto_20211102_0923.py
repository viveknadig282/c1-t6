# Generated by Django 3.2.8 on 2021-11-02 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IEapp', '0004_auto_20211102_0910'),
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
            ],
        ),
        migrations.CreateModel(
            name='ScraperArticle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_url', models.CharField(max_length=50000)),
                ('article_data', models.CharField(max_length=50000)),
                ('classification_result', models.IntegerField(default=0)),
                ('ingredients_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='within_food',
        ),
        migrations.RemoveField(
            model_name='scraperarticles',
            name='ingredients_id',
        ),
        migrations.RemoveField(
            model_name='food',
            name='ingredient_content',
        ),
        migrations.DeleteModel(
            name='Ingredient_Food',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='ScraperArticles',
        ),
        migrations.AddField(
            model_name='ingredientfood',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.food'),
        ),
        migrations.AddField(
            model_name='ingredientfood',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IEapp.ingredient'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='foods',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food'),
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Ingredient'),
        ),
    ]
