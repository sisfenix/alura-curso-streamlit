import streamlit as st
import requests
import pandas as pd
import plotly.express as px


def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value = value / 1000
    return f'{prefix} {value:.2f} milhões'

st.title('DASHBOARD DE VENDAS :shopping_trolley:')

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

col1, col2 = st.columns(2)
with col1:
    st.metric("Receita", format_number(dados['Preço'].sum(), 'R$'))
with col2:
    st.metric("Quantidade de vendas", format_number(dados.shape[0]))

st.dataframe(dados)
