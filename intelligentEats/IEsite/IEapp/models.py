from django.db import models

# Create your models here.
#scraper_articles, ingredients, food, ingredient_food
class ScraperArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    article_url = models.CharField(max_length = 50000)
    article_data = models.CharField(max_length = 50000)
    ingredients_id = models.ForeignKey('Ingredient', on_delete=models.CASCADE, null=True)
    classification_result = models.IntegerField(default=0)
    class Meta:
        db_table = 'ScraperArticle'

class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50000)
    score = models.FloatField(default = 0.0)
    foods = models.ManyToManyField(through='IEapp.IngredientFood', to='IEapp.Food')
  
    class Meta:
        db_table = 'Ingredient'


class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50000)
    score = models.FloatField(default= 1.0)
    ingredients = models.ManyToManyField('Ingredient', through='IngredientFood')
    class Meta:
        db_table = 'Food'
    def __str__(self):
        return self.name + ' ' + str(self.score)

class IngredientFood(models.Model):
    id = models.IntegerField(primary_key=True)
    ingredients = models.ForeignKey('Ingredient', models.SET_NULL, blank=True, null=True)
    foods = models.ForeignKey('Food', models.SET_NULL, blank=True, null=True) 
    class Meta:
        db_table = 'ingredient_food'

