import requests
import csv

API_KEY = "AIzaSyD_DGKh2WQHfycaU9d_AvYbndut5FFyFvE"
SEARCH_ENGINE_ID = "a2bf933286d2f6720"

# #/ means the ingredient has already been scraped
# # means it still needs to be scraped, but its over the daily quota

ingredients = [ #/'Calcium+Carbonate',
                #/'Iron',
                #/'Zinc+%28mineral+nutrients%29',
                #/'Vitamin+C+%28sodium+ascorbate%29',
                #/'A+B+Vitamin+%28niacinamide%29',
                #/'Vitamin+B6+%28pyridoxine+hydrochloride%29',
                #/'Vitamin+A+%28palmitate%29',
                #/'Vitamin+B1+%28thiamin+mononitrate%29',
                #/'A+B+Vitamin+%28folic+acid%29',
                #/'Vitamin+B12',
                #/'Vitamin+D3',
                #/'wheat+flour',
                #/'niacin+(Vitamin+B3)',
                #/'thiamine+mononitrate+(Vitamin+B1)',
                #/'riboflavin+(Vitamin+B2)',
                #/'Pork',
                #/'Chicken',
                #/'Beef',
                #/'dextrose',
                #/'lactic+acid',
                #/'sodium+nitrite',
                #/'sodium+ascorbate',
                #/'BHA',
                #/'BHT',
                #/'Citric+acid',
                #/'Pyrophosphate',
                #/'Tuna',
                #/'Carbonated+Water',
                #/'Sucrose',
                #/'Glucose',
                #/'Taurine',
                #/'Sodium+Bicarbonate',
                #/'Magnesium+Carbonate',
                #/'Caffeine',
                #/'Niacinamide',
                #/'Calcium+Pantothenate',
                #/'Pyridoxine+HCI',
                #/'Food+Colors+Red',
                #/'Food+Colors'
                #/'High+Fructose+Corn+Syrup',
                #/'Caramel+Color',
                #/'Phosphoric+Acid',
                #/'Natural+Flavors',
                #/'Corn+Meal',
                #/'Ferrous+Sulfate',
                #/'Vegetable+Oil',
                #/'Whey',
                #'Cheddar+Cheese'
               #/ 'Milk',
               #/ 'Cheese+Cultures',
                #/ 'Canola+Oil',
               # 'Maltodextrin',
               # 'Whey+Protein+Concentrate',
              #  'Monosodium+Glutamate',
               # 'Artificial+Color+Yellow+6'
              ]

def scan_ingredient(ingredient, out_file_writer, page_number): 
    print(ingredient + " BEGIN")
    for page in range(page_number):
        
        start = page * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q=is+{ingredient}+healthy&start={start}"
        
        response = requests.get(url)
        data = response.json()

        if data is None:
            continue
        
        search_items = data.get("items")
        
        if search_items is None:
            continue
        
        for i, search_item in enumerate(search_items, start=start):
    
            title = search_item.get("title")
            snippet = search_item.get("snippet")
            link = search_item.get("link")

            out_file_writer.writerow([ingredient,title,snippet,link])         

    print(ingredient + "   DONE!")
        
csv_file = open('c:\dev\data\ingredient_search_results.csv', mode='a', newline='', encoding='utf-8')
writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for ingredient in ingredients:
    scan_ingredient(ingredient, writer, 2)

csv_file.close()
