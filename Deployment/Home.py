import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 
import yfinance as yf
import category_a, category_b

def run():
    def user_input():
        stock_symbol = st.sidebar.selectbox('Category', ('Category A', 'Category B'))

        tickerData = yf.Ticker(stock_symbol+'.JK')
        return stock_symbol

    stock_symbol = user_input()
    if stock_symbol == "Category A":
        category_a.run()
        st.write("""
            # Product Category A
                
            """)
        
    elif stock_symbol == "Category B":
        category_b.run()
        st.write("""
            # Product Category B
                
            """)

if __name__ == '__main__':
    run()
