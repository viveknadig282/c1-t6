from django.db import models

# Create your models here.
#scraper_articles, ingredients, food, ingredient_food
class ScraperArticle(models.Model):
    id                    = models.IntegerField(primary_key=True)
    article_url           = models.CharField(max_length = 50000)
    article_data          = models.CharField(max_length = 50000)
    #fix this on delete setting!!
    ingredients_id        = models.ForeignKey('Ingredient', models.SET_NULL, blank=True, null=True)
    classification_result = models.IntegerField(default=0)
 
class Ingredient(models.Model):
    id             = models.IntegerField(primary_key=True)
    name           = models.CharField(max_length = 50000)
    score          = models.IntegerField(default=0)
    within_food    = models.ManyToManyField('Food', through='IngredientFood')
    

class Food(models.Model):
    id                 = models.IntegerField(primary_key=True)
    name               = models.CharField(max_length = 50000)
    score              = models.IntegerField(default=0)
    ingredient_content = models.ManyToManyField('Ingredient', through='IngredientFood')
    

class IngredientFood(models.Model):
    id             = models.IntegerField(primary_key=True)
    ingredients = models.ForeignKey('Ingredient', models.SET_NULL, blank=True, null=True)
    foods       = models.ForeignKey('Food', models.SET_NULL, blank=True, null=True)