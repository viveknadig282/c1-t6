import csv 

from IEapp.models import ScraperArticles, Ingredients, Food, IngredientFood

#This will be called to run 
def run(): 
    to_read = [
    r'C:\Users\Admin\Downloads\ingredients_sql.csv',
    r'C:\Users\Admin\Downloads\food_sql.csv',
    r'C:\Users\Admin\Downloads\ingredient_food_sql.csv',
    ]

    ScraperArticles.objects.all().delete() # get rid of any extra data stored in the database 
    Ingredients.objects.all().delete()      # ditto
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
                Ingredients(
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
                Ingredient = Ingredients.objects.get(pk = row[1]), 
                Food       = Food.objects.get(pk = row[2])
                ).save()
            
        
        
    