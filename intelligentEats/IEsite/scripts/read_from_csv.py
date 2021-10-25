import csv 

from IEapp.models import scraper_articles, ingredients, food, ingredient_food

#This will be called to run 
def run():
    to_read = [
    r'C:\Users\Admin\Downloads\scraper_articles_sql_1.csv', 
    ]
    for i in to_read:
        current_file = open(i, encoding='utf-8')
        reader = csv.reader(current_file)

        scraper_articles.objects.all().delete()
        ingredients.objects.all().delete()
        for row in reader:
            print(row)
            
        
        return
    return