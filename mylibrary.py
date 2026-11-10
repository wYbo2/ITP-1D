## Business Logic ---------------------------------------------------------------------
## This file stores function(s) that implement the business logic.
## get_recommendations:
## Takes in a list of dictionaries, each dictionary has data for one attraction
## Takes in a list of the user's choices of categories  
## Currently, it returns by default the dictionary in attractions_list at index 0. 
## Modify the code so that it returns the attractions belonging to categories that the user chooses
## See the project brief slides for hints. 
## ------------------------------------------------------------------------------------

def get_recommendations(attractions_list, choices):
    out = []
    out.append(attractions_list[0])
    return out

## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own attractions with their own categories
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------