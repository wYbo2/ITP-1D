
import streamlit as st

## The logic for the calculation is stored in functions in mylibrary.py 
import mylibrary 

## User Interface ---------------------------------------------------------------------
## This file shows you streamlit code for three parts.
## Business Data - how to specify the data for the attractions in the theme park.
## Data Entry - how to make widgets to get the user inputs. 
## Calculation - how to get the result from the user inputs. 
## ------------------------------------------------------------------------------------


## Business Data ---------------------------------------------------------------------
## Attractions belong to one or more of three categories, "nature", "great views", "shows"
## ALL_CATEGORIES  is a list of strings containing all the categories
## ATTRACTIONS is a list of dictionaries. 
## each dictionary represents one attraction and has three key-value pairs 
## the "category" key stores a list, which means one attraction can have more than one category
## ------------------------------------------------------------------------------------

HOLLYWOOD = "hollywood"
SCI_FI_CITY = "sci fi city"
ANCIENT_EGYPT = "ancient egypt" 
THE_LOST_WORLD = "the lost world"
FAR_FAR_AWAY = "far far away"


ALL_CATEGORIES = [HOLLYWOOD, SCI_FI_CITY, ANCIENT_EGYPT, THE_LOST_WORLD, FAR_FAR_AWAY]

ATTRACTIONS = [ 
    { "name"    : "Lights, camera, action!", 
      "category": [ HOLLYWOOD ], 
      "description" : "experience your dreams as a reality in hollywood!"
    }, 
    { "name"    : "TRANSFORMERS: The Ride", 
      "category": [ SCI_FI_CITY ], 
      "description" : "join the autobots in the battle for the allspark!"
    }, 
    { "name"    : "Battlestar Galactica", 
      "category": [ SCI_FI_CITY ], 
      "description" : "the world's tallest dueling roller coasters featuring a fast seated track (Human) and an intense inverted track with inversions (Cylon)."
    }, 
    { "name"    : "Revenge of the Mummy", 
      "category": [ ANCIENT_EGYPT ], 
      "description" : "a high-speed, pitch-black indoor roller coaster combined with a thrilling dark ride through ancient Egyptian tombs."
    },
    { "name"    : "Jurassic Park Rapids Adventure", 
      "category": [ THE_LOST_WORLD ], 
      "description" : "a roaring river-rafting water ride through dinosaur territory that ends with a sudden, splash-heavy drop."
    },
    { "name"    : "Waterworld", 
      "category": [ THE_LOST_WORLD ], 
      "description" : "get splashed in this thrilling showcase in waterworld!"
    },
    { "name"    : "Donkey Live", 
      "category": [ FAR_FAR_AWAY ], 
      "description" : "interact with donkey in shrek, but beware, hes very insensitive"
    },
    { "name"    : "Shrek 4D adventure", 
      "category": [ FAR_FAR_AWAY ], 
      "description" : "immerse yourself in the world of shrek in this 4D adventure!"
    },   
]


## Data Entry -------------------------------------------------------------------------
## Shows you the code to 
## 1) write a title on the screen
## 2) how do you write a multiselect widget to allow the user to select more than one choice
## 3) how do you write text on the screen 
## The key attribute enables you to retrieve the data entered for that widget from st.session_state 
## ------------------------------------------------------------------------------------

st.title("What kind of attraction do you wish to visit at Universal Studios Singapore?") 

st.multiselect(
    label="Select your category",
    options=ALL_CATEGORIES,
    key="user_selection" 
    )

### Display user's choices as a debugging hint 
### This is stored in a datatype similar to a list
st.write(st.session_state.user_selection)

### Define a function to clear the user's choices
def reset_choices():
    st.session_state.user_selection = []

## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## 5) How do you declare a button to execute a function when clicked
## ------------------------------------------------------------------------------------ 

if st.button("Get me recommendations"):
    options = list( st.session_state.user_selection )  
    recs = mylibrary.get_recommendations(ATTRACTIONS, options)
    st.table(recs)

st.button("Reset Selections", on_click=reset_choices)
