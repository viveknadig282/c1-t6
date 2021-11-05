from django.db import models

# Create your models here.
#scraper_articles, ingredients, food, ingredient_food
class scraper_articles(models.Model):
    id                    = models.IntegerField
    article_url           = models.CharField(max_length = 50000)
    article_data          = models.CharField(max_length = 50000)
    ingredients_id        = models.ForeignKey('ingredients', models.SET_NULL, blank=True, null=True)
    classification_result = models.IntegerField
    
    class Meta:
        db_table = 'scraper_articles'
 
class ingredients(models.Model):
    id             = models.IntegerField
    name           = models.CharField(max_length = 50000)
    within_food    = models.ManyToManyField('food', through='ingredient_food')
    score          = models.IntegerField
    
    class Meta:
        db_table = 'ingredients'

class food(models.Model):
    id                 = models.IntegerField
    name               = models.CharField(max_length = 50000)
    ingredient_content = models.ManyToManyField('ingredients', through='ingredient_food')
    score              = models.IntegerField
    
    class Meta:
        db_table = 'food'

class ingredient_food(models.Model):
    ingredient = models.ForeignKey('ingredients', models.SET_NULL, blank=True, null=True)
    iood       = models.ForeignKey('food', models.SET_NULL, blank=True, null=True)
    
    class Meta:
        db_table = 'ingredient_food'
