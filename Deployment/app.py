import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import Home, Forecasting


pageicon = Image.open('Yuni.jpg')

st.set_page_config(page_title = 'Your personal Digital Financial Advisory for Mutual Funds',page_icon=pageicon, layout='wide', initial_sidebar_state='expanded')

st.subheader('Kalbe Forecasting Product')
st.write('-----')


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home', 'Forecasting'],
        icons=['house','cash'],
        menu_icon='',
        default_index=0,
    )

if selected == 'Home':
    Home.run()


elif selected == 'Forecasting':
    Forecasting.run()
