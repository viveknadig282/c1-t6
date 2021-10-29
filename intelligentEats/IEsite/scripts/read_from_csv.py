import csv 

from IEapp.models import scraper_articles, ingredients, food, ingredient_food

#This will be called to run 
def run():
    x = 1 
    to_read = [
    r'C:\Users\Admin\Downloads\ingredients_sql.csv',
     
    ]
    for i in to_read:
        current_file = open(i, encoding='utf-8')
        reader = csv.reader(current_file)

        scraper_articles.objects.all().delete()
        ingredients.objects.all().delete()
        #reader
        for row in reader:
            print(row)
            
        
        
    