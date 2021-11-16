import requests
import urllib
import json

class FoodAPI:
    #following constants should be replaced by production version and moved
    app_id = '5d3057d6'
    app_key = '0a61f1c8fb7cfe232b441f8faa2afd4f'

    def __init__(self, app_id, app_key):
        if app_id is not None and app_key is not None:
            self.app_id = app_id
            self.app_key = app_key

    def get_ingredients(self, upc_code):
        url = 'https://api.edamam.com/api/food-database/v2/parser'
        
        try:  
            response = requests.get(url, 
                                    params={'app_id':self.app_id, 
                                            'app_key':self.app_key, 
                                            'upc':upc_code, 
                                            'nutrition-type':'cooking'}, 
                                    headers={'Accept':'application/json'})
        
            response.raise_for_status()
            json_response = response.json()
            ingredient_str = json_response['hints'][0]['food']['foodContentsLabel']
            ingredients = ingredient_str.lower().split('; ')
        
            return ingredients
        except:
            return []
