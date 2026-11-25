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
    # if the user did not select any category, recommend everything
    if len(choices) == 0:
        return attractions_list

    out = []
    for attraction in attractions_list:
        for category in attraction["category"]:
            if category in choices:
                out.append(attraction)
                break  # stop checking, so the same attraction isn't added twice
    return out

## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own attractions with their own categories
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------