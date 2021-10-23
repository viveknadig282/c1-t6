from django.db import models

# Create your models here.

class scraper_articles(models.Model):
    id = models.IntegerField
    article_url = models.CharField(max_length = 50000)
    article_data = models.CharField(max_length = 50000)
    ingredients_id = models.IntegerField
    classification_result = models.IntegerField

class ingredients(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length = 50000)
    #FIGURE OUT HOW TO GET FROM scraper_articles.classification_result FOR BELOW
    score = models.IntegerField

class food(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length = 50000)
    #FIGURE OUT HOW TO GET FROM ingredients.score FOR BELOW
    score = models.IntegerField

class ingredient_food(models.Model):
    #FIGURE OUT HOW TO GET FROM ingredients.id FOR BELOW
    ingredient_id = models.IntegerField
    #FIGURE OUT HOW TO GET FROM food.id FOR BELOW
    food_id = models.IntegerField