import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

df = pd.ExcelFile(r'G:\Learning\Talent_Fair\Kalbe_Farma\kalbe_data.xlsx')
df_a1 = pd.read_excel(df,'A1')
df_a2 = pd.read_excel(df,'A2')

# Convert type data column day to date
df_a1.Day = pd.date_range(start='1/1/2023', periods=len(df_a1), freq='D')
df_a2.Day = pd.date_range(start='1/1/2023', periods=len(df_a2), freq='D')

def run():
    def user_input_category_a():
        a_symbol = st.sidebar.selectbox('Pilih Produk', ('Produk A1','Produk A2'))

        tickerData = yf.Ticker(a_symbol+'.JK')
        return a_symbol
    
    a_symbol = user_input_category_a()
    if a_symbol == 'Produk A1':
        st.dataframe(df_a1)
        # Plot product A
        fig = px.line(df_a1, x='Day', y='Sales', title='Sales Product A')
        st.plotly_chart(fig)
        st.write('-----')

    if a_symbol == 'Produk A2':
        st.dataframe(df_a2)
        #Plot product B
        fig = px.line(df_a2, x='Day', y='Sales', title='Sales Product A')
        st.plotly_chart(fig)

if __name__ == '__main__':
    run()