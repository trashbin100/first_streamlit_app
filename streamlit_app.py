import streamlit as st
import streamlit
import pandas as pd
import pandas
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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response)


# Make the JSON more Presentable 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Showcases the API as a reading as an Entry 
streamlit.dataframe(fruityvice_normalized)


