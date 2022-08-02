import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favs')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')

import pandas
streamlit.header('🍓🍌 Build Your Smoothie 🍍🍎')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the table on the page
streamlit.dataframe(my_fruit_list)
