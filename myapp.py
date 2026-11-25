
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
MALE = "male"
FEMALE = "female"
UNDER_13 = "< 13 years old"
OVER_13 = "> 13 years old"
UNDER_100CM = "< 100cm"
BETWEEN_100CM_TO_132CM = "100cm - 132cm"
OVER_132CM = "> 132cm"


ALL_CATEGORIES = [HOLLYWOOD, SCI_FI_CITY, ANCIENT_EGYPT, THE_LOST_WORLD, FAR_FAR_AWAY]
GENDER = [MALE, FEMALE]
AGE = [UNDER_13, OVER_13]
HEIGHT = [UNDER_100CM, BETWEEN_100CM_TO_132CM, OVER_132CM]

ATTRACTIONS = mylibrary.read_attractions("attractions.txt")


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

st.multiselect(
    label="Select your age",
    options=AGE,
    key="user_age_selection"
)

st.multiselect(
    label="Select your height",
    options=HEIGHT,
    key="user_height_selection"
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
    ages = list( st.session_state.user_age_selection )
    heights = list( st.session_state.user_height_selection )
    recs = mylibrary.get_recommendations(ATTRACTIONS, options, ages, heights)
    st.table(recs)

st.button("Reset Selections", on_click=reset_choices)


## Booking System ---------------------------------------------------------------------
## Lets the user book tickets and shows the final price.
## ------------------------------------------------------------------------------------

st.header("Book your tickets")

st.text_input("Name", key="booking_name")

col1, col2 = st.columns([1, 3])
with col1:
    st.text_input("Country code", placeholder="+65", key="booking_country_code")
with col2:
    st.text_input("Phone number", placeholder="91234567", key="booking_phone")

st.date_input("Date of visit", key="booking_date")

st.number_input(f"Adults (${mylibrary.ADULT_PRICE} each)", min_value=1, step=1, key="booking_adults")
st.number_input(f"Children (${mylibrary.CHILD_PRICE} each)", min_value=0, step=1, key="booking_children")

total = mylibrary.calculate_price(st.session_state.booking_adults, st.session_state.booking_children)
st.subheader(f"Total price: ${total}")

if st.button("Book"):
    name = st.session_state.booking_name.strip()
    country_code = st.session_state.booking_country_code.strip()
    phone = st.session_state.booking_phone.strip()

    if name == "":
        st.error("Please enter your name.")
    elif not mylibrary.is_valid_phone(country_code, phone):
        st.error("Please enter a valid phone number. The country code must start with + (e.g. +65), "
                 "and the country code and number together must have more than 7 digits.")
    else:
        full_phone = country_code + " " + phone
        mylibrary.save_booking("bookings.txt", name, full_phone, st.session_state.booking_date,
                               st.session_state.booking_adults, st.session_state.booking_children, total)
        st.success("Booking confirmed!")
        st.table({
            "Name": [name],
            "Phone": [full_phone],
            "Date": [str(st.session_state.booking_date)],
            "Adults": [st.session_state.booking_adults],
            "Children": [st.session_state.booking_children],
            "Total price": [f"${total}"],
        })
