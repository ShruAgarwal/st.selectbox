import streamlit as st
import pandas as pd

st.title('**st.selectbox**')
st.write('*Allows the display of a select widget*')

# Fruit collection
df = pd.DataFrame({
     'fruit': ['Apple 🍎', 'Banana 🍌', 'Pear 🍐', 'Orange 🍊', 'Watermelon 🍉', 'Kiwi 🥝', 'Grapes 🍇'],
     'color': ['red', 'yellow', 'green', 'orange', 'pinkish', 'brown', 'violet-blackish']
     })

# Choose any fruit
fruit = st.selectbox(
     'What\'s your favorite fruit?',
     (df['fruit']))

# Matches color of the fruit
info = df[df['fruit'] == fruit]
color = info.iloc[0]['color']


st.write(fruit,' is your favorite fruit whoose color is ', color)