1

import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣 - Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 - Kale, Spinach and Smoothie')
streamlit.text('🐔 - Hard-boiled free range eggs')
streamlit.text('🥑🍞 - Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index),['Lemon', 'Lime'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
