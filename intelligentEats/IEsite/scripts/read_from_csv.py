import csv 

from IEapp.models import ScraperArticle, Ingredient, Food, IngredientFood

#This will be called to run 
def run(): 
    # insert the files you want to read into the lists under the proper key
    to_read = {
    'Ingredients': [r'C:\Users\Admin\Downloads\ingredients_sql.csv'],
    'Foods': [r'C:\Users\Admin\Downloads\food_sql.csv'],
    'IngredientFoods':[r'C:\Users\Admin\Downloads\ingredient_food_sql.csv'],
    'ScraperArticles' : [r'C:\Users\Admin\Downloads\scraper_articles_sql_1.csv', 
                         r'C:\Users\Admin\Downloads\scraper_articles_sql_2.csv', 
                         r'C:\Users\Admin\Downloads\scraper_articles_sql_3.csv',
                         r'C:\Users\Admin\Downloads\scraper_articles_sql_4.csv'
                         ]
    }

    ScraperArticle.objects.all().delete() # get rid of any extra data stored in the database 
    Ingredient.objects.all().delete()      # just for now at least while im still editing the scripts and doing mass imports
    Food.objects.all().delete()             # ditto 
    IngredientFood.objects.all().delete()  # ditto

    #define a function to read the files into the database
    def filereader(files, current_table):
        #loops through the list within each key incase there are multiple csv files for a table
        for file in files:
            with open(file, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                #loops through all the rows in the csv file
                for row in csv_reader:
                    print(row)
                    #saves each row to their respective tables
                    if current_table == Ingredient:
                        current_table(
                            id = row['ID'],
                            name = row['NAME'],
                            score = row['SCORE']
                        ).save()
                    elif current_table == Food:
                        print('food time')
                        current_table(
                        id = row['id'],
                        name = row['name'],
                        
                        ).save()
                    elif current_table == IngredientFood:
                        current_table(
                        id = row['id'],
                        ingredients = Ingredient.objects.get(pk = int(row['ingredient_id'])),
                        foods = Food.objects.get(pk = int(row['food_id']))
                        ).save()
                    elif current_table == ScraperArticle:
                        current_table(
                        id = row['ID'],
                        article_url = row['ARTICLE_LINK'],
                        article_data = row['ARTICLE_DATA'],
                        ingredients_id = Ingredient.objects.get(pk = row["INGREDIENT_ID"]),
                        classification_result = row['CLASSIFICATION_RESULT']
                        ).save()
    filereader(to_read['Ingredients'], Ingredient)
    filereader(to_read['Foods'], Food)
    filereader(to_read['IngredientFoods'], IngredientFood)
    filereader(to_read['ScraperArticles'], ScraperArticle)