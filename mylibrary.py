## Business Logic ---------------------------------------------------------------------
## This file stores function(s) that implement the business logic.
## get_recommendations:
## Takes in a list of dictionaries, each dictionary has data for one attraction
## Takes in a list of the user's choices of categories  
## Currently, it returns by default the dictionary in attractions_list at index 0. 
## Modify the code so that it returns the attractions belonging to categories that the user chooses
## See the project brief slides for hints. 
## ------------------------------------------------------------------------------------

## read_attractions:
## Reads the attractions from a text file and returns a list of dictionaries.
## Each line in the file looks like:
##   name | categories | ages | heights | description
## categories, ages and heights can have more than one value, separated by a comma.
def read_attractions(filename):
    attractions = []
    file = open(filename, "r", encoding="utf-8")
    for line in file:
        line = line.strip()

        # skip empty lines and comment lines starting with #
        if line == "" or line.startswith("#"):
            continue

        parts = line.split("|")
        attraction = {
            "name"       : parts[0].strip(),
            "category"   : split_values(parts[1]),
            "age"        : split_values(parts[2]),
            "height"     : split_values(parts[3]),
            "description": parts[4].strip()
        }
        attractions.append(attraction)
    file.close()
    return attractions

## split_values:
## Turns text like "< 13 years old, > 13 years old" into ["< 13 years old", "> 13 years old"]
def split_values(text):
    values = []
    for value in text.split(","):
        values.append(value.strip())
    return values


## matches:
## Returns True if at least one of the attraction's values is in the user's selection.
## If the user selected nothing, it returns True (no filter for that question).
def matches(attraction_values, selected):
    if len(selected) == 0:
        return True
    for value in attraction_values:
        if value in selected:
            return True
    return False


## get_recommendations:
## An attraction is recommended only if it matches the category, age AND height selections.
def get_recommendations(attractions_list, choices, ages, heights):
    out = []
    for attraction in attractions_list:
        if (matches(attraction["category"], choices)
                and matches(attraction["age"], ages)
                and matches(attraction["height"], heights)):
            out.append(attraction)
    return out

## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own attractions with their own categories
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------

## Booking System ---------------------------------------------------------------------
## Functions used by the booking form in myapp.py
## ------------------------------------------------------------------------------------

ADULT_PRICE = 83
CHILD_PRICE = 62

## calculate_price:
## Returns the total price for the number of adults and children.
def calculate_price(adults, children):
    return adults * ADULT_PRICE + children * CHILD_PRICE


## is_valid_phone:
## The country code must start with "+" followed by digits, e.g. "+65".
## The phone number must contain only digits.
## Country code digits + phone digits together must be MORE than 7.
def is_valid_phone(country_code, phone):
    if not country_code.startswith("+"):
        return False
    code_digits = country_code[1:]
    if not code_digits.isdigit() or not phone.isdigit():
        return False
    return len(code_digits) + len(phone) > 7


## save_booking:
## Adds one booking as a line to the file, in the format:
##   name | phone | date | adults | children | total price
def save_booking(filename, name, phone, date, adults, children, total):
    file = open(filename, "a", encoding="utf-8")
    file.write(f"{name} | {phone} | {date} | {adults} | {children} | {total}\n")
    file.close()
