import requests
import csv

API_KEY = "AIzaSyD_DGKh2WQHfycaU9d_AvYbndut5FFyFvE"
SEARCH_ENGINE_ID = "a2bf933286d2f6720"

ingredients = [ 'apple',
                'celery'
                ]

def scan_ingredient(ingredient, out_file_writer, page_number): 

    for page in range(page_number):
       
        start = page * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q=is+{ingredient}+healthy&start={start}"
        
        response = requests.get(url)
        data = response.json()
        
        search_items = data.get("items")
        
        for i, search_item in enumerate(search_items, start=start):
    
            title = search_item.get("title")
            snippet = search_item.get("snippet")
            link = search_item.get("link")

            out_file_writer.writerow([ingredient,title,snippet,link])         

csv_file = open('c:\dev\data\ingredient_search_results.csv', mode='w', newline='', encoding='utf-8')
writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for ingredient in ingredients:
    scan_ingredient(ingredient, writer, 2)

csv_file.close()
