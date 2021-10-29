import csv 

from IEapp.models import scraper_articles, ingredients, food, ingredient_food

#This will be called to run 
def run(): 
    to_read = [
    r'C:\Users\Admin\Downloads\ingredients_sql.csv',
    r'C:\Users\Admin\Downloads\food_sql.csv',
    r'C:\Users\Admin\Downloads\ingredient_food_sql.csv',
    ]

    scraper_articles.objects.all().delete() # get rid of any extra data stored in the database 
    ingredients.objects.all().delete()      # ditto
    food.objects.all().delete()             # ditto 
    ingredient_food.objects.all().delete()  # ditto

    for index, file in enumerate(to_read):
        current_file = open(file, encoding='utf-8') # define the file to open and how to read it 
        reader = csv.reader(current_file)        # read the file using csv module
        next(reader)                             # advance past the header

        

        #reader
        for row in reader:
            print(row)
            if index == 0:
                ingredients(
                id   = row[0], 
                name = row[1]
                ).save()
                

            if index == 1:
                food(
                id   = row[0], 
                name = row[1]
                ).save()
                

            if index == 2: 
                ingredient_food(
                id         = row[0], 
                Ingredient = ingredients.objects.get(pk = row[1]), 
                Food       = food.objects.get(pk = row[2])
                ).save()
            
        
        
    