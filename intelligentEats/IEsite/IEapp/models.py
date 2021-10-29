from django.db import models

# Create your models here.
#scraper_articles, ingredients, food, ingredient_food
class scraper_articles(models.Model):
    id                    = models.IntegerField(primary_key=True)
    article_url           = models.CharField(max_length = 50000)
    article_data          = models.CharField(max_length = 50000)
    #fix this on delete setting!!
    ingredients_id        = models.ForeignKey('ingredients', models.SET_NULL, blank=True, null=True)
    classification_result = models.IntegerField(default=0)
 
class ingredients(models.Model):
    id             = models.IntegerField(primary_key=True)
    name           = models.CharField(max_length = 50000)
    score          = models.IntegerField(default=0)
    within_food    = models.ManyToManyField('food', through='ingredient_food')
    

class food(models.Model):
    id                 = models.IntegerField(primary_key=True)
    name               = models.CharField(max_length = 50000)
    score              = models.IntegerField(default=0)
    ingredient_content = models.ManyToManyField('ingredients', through='ingredient_food')
    

class ingredient_food(models.Model):
    id             = models.IntegerField(primary_key=True)
    Ingredient = models.ForeignKey('ingredients', models.SET_NULL, blank=True, null=True)
    Food       = models.ForeignKey('food', models.SET_NULL, blank=True, null=True)