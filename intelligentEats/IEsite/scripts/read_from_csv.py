import csv 

from IEapp.models import ScraperArticle, Ingredient, Food, IngredientFood

#This will be called to run 
def run(): 
    to_read = [
    r'C:\Users\Admin\Downloads\ingredients_sql.csv',
    r'C:\Users\Admin\Downloads\food_sql.csv',
    r'C:\Users\Admin\Downloads\ingredient_food_sql.csv',
    ]

    ScraperArticle.objects.all().delete() # get rid of any extra data stored in the database 
    Ingredient.objects.all().delete()      # ditto
    Food.objects.all().delete()             # ditto 
    IngredientFood.objects.all().delete()  # ditto

    for index, file in enumerate(to_read):
        current_file = open(file, encoding='utf-8') # define the file to open and how to read it 
        reader = csv.reader(current_file)        # read the file using csv module
        next(reader)                             # advance past the header

        

        #reader
        for row in reader:
            print(row)
            if index == 0:
                Ingredient(
                id   = row[0], 
                name = row[1]
                ).save()
                

            if index == 1:
                Food(
                id   = row[0], 
                name = row[1]
                ).save()
                

            if index == 2: 
                IngredientFood(
                id         = row[0], 
                ingredients = Ingredient.objects.get(pk = row[1]), 
                foods       = Food.objects.get(pk = row[2])
                ).save()
            
        
        
    