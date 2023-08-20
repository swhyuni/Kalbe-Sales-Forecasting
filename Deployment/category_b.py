import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

df = pd.ExcelFile(r'G:\Learning\Talent_Fair\Kalbe_Farma\kalbe_data.xlsx')
df_b1 = pd.read_excel(df,'B1')
df_b2 = pd.read_excel(df,'B2')

# Convert type data column day to date
df_b1.Day = pd.date_range(start='1/1/2023', periods=len(df_b1), freq='D')
df_b2.Day = pd.date_range(start='1/1/2023', periods=len(df_b2), freq='D')

def run():
    def user_input_category_a():
        a_symbol = st.sidebar.selectbox('Pilih Produk', ('Produk B1','Produk B2'))

        tickerData = yf.Ticker(a_symbol+'.JK')
        return a_symbol
    
    a_symbol = user_input_category_a()
    if a_symbol == 'Produk B1':
        st.dataframe(df_b1)
        # Plot product A
        fig = px.line(df_b1, x='Day', y='Sales', title='Sales Product A')
        st.plotly_chart(fig)
        st.write('-----')

    if a_symbol == 'Produk B2':
        st.dataframe(df_b2)
        #Plot product B
        fig = px.line(df_b2, x='Day', y='Sales', title='Sales Product A')
        st.plotly_chart(fig)

if __name__ == '__main__':
    run()
