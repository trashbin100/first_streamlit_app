import streamlit as st
import streamlit
import pandas as pd
import pandas
import requests 
import snowflake.connector
from urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()        #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")




st.title("My Parents New Healthy Diner")

st.header("Breakfast Menu")

st.text("🥣 Omega 3 & Blueberry Oatmeal")

st.text("🥗 Kale, Spinach & Rocket Smoothie")

st.text("🐔 Hard-Boiled Free-Range Egg")

st.text("🥑🍞 Avocado Toast")


st.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
# don't run anything while troublle shooting 
#streamlit.stop()

# List chooses what things to include 

fruits_selected = st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# Snowflake Related Functions 
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  
# Add button to load fruit 
if streamlit.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
  

# Allow End User to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_curr.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding" + new_fruit
  
  
  
add_my_fruit = st.text_input("What fruit would you like information about?", "jackfruit")
if streamlit.button("Add a Fruit to the List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
  streamliit.text(back_from_function)
  
  
streamlit.write("The user entered", add_my_fruit)


# Shows the new section of Fruityvice Response 
# Create a the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

  # New Section to display fruityvice api response. 
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("PLease select a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruit_choice)
    streamlit.dataframe(back_from_function)
  except URLError as e:
    streamlit.error()

st.header("Fruityvice Fruit Advice!")

# This code will not work correctly 
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#display on page
st.dataframe(fruits_to_show)


# New Section to display fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("PLease select a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
  except URLError as e:
    streamlit.error()


# Enter a selection
fruit_choice = st.text_input("What fruit would you like information about?", "Kiwi")
streamlit.write("The user entered", fruit_choice)


# Creates a variable for internet response 
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)


# Make the JSON more Presentable 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Showcases the API as a reading as an Entry 
#streamlit.dataframe(fruityvice_normalized)


