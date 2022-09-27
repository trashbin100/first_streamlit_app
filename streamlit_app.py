import streamlit as st
import pandas as pd
import requests 



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")




st.title("My Parents New Healthy Diner")

st.header("Breakfast Menu")

st.text("🥣 Omega 3 & Blueberry Oatmeal")

st.text("🥗 Kale, Spinach & Rocket Smoothie")

st.text("🐔 Hard-Boiled Free-Range Egg")

st.text("🥑🍞 Avocado Toast")


st.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

# List chooses what things to include 

fruits_selected = st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Shows the new section of Fruityvice Response 
streamlit.header("Fruityvice Fruit Advice!")
#display on page
st.dataframe(fruits_to_show)

# Creates a variable for internet response 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
