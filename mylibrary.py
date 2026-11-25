## Business Logic ---------------------------------------------------------------------
## This file stores function(s) that implement the business logic.
## get_recommendations:
## Takes in a list of dictionaries, each dictionary has data for one attraction
## Takes in a list of the user's choices of categories  
## Currently, it returns by default the dictionary in attractions_list at index 0. 
## Modify the code so that it returns the attractions belonging to categories that the user chooses
## See the project brief slides for hints. 
## ------------------------------------------------------------------------------------

import random


def load_attractions(filepath):
    attractions = []
    with open(filepath, 'r', encoding1  ='utf-8') as file:
        for line_num, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            
            if not line or line.startswith("#"):
                continue  

            parts = [part.strip() for part in line.split("|")]
            if len(parts) != 5:
                raise ValueError(
                    f"Line {line_num} in '{filepath}' must have 5 pipe-separated fields (got {len(parts)})."
                )
            name, categories_str, ages_str, heights_str, description = parts

            attractions.append({
                "name": name,
                "category": [c.strip() for c in categories_str.split(",") if c.strip()],
                "age": [a.strip() for a in ages_str.split(",") if a.strip()],
                "height": [h.strip() for h in heights_str.split(",") if h.strip()],
                "description": description,
            })    

            return attractions



def get_recommendations(attractions_list, choices):
    out = []
    out.append(random.choice(attractions_list))
    return out

## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own attractions with their own categories
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------