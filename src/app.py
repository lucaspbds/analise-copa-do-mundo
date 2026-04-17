import streamlit as st
import pandas as pd
from components.ranking_paises_titulos import ranking_paises_titulos
from components.evolucao_gols_copa_do_mundo import evolucao_gols_copa_do_mundo
from components.ranking_paises_gols import ranking_paises_gols
from components.cards import pais_menos_frequencia
from components.cards import pais_mais_gols
from components.cards import pais_mais_frequencia_final
from components.cards import pais_mais_frequencia
from pipeline import pipeline

df_partidas = pd.read_csv("data/raw/matches_1930_2022.csv")
print(df_partidas.info())
print(df_partidas.describe())

df_fifa_ranking = pd.read_csv("data/raw/fifa_ranking_2022-10-06.csv")
print(df_fifa_ranking.info())
print(df_fifa_ranking.describe())

df_copa_do_mundo = pd.read_csv("data/raw/world_cup.csv")
print(df_copa_do_mundo.info())
print(df_copa_do_mundo.describe())

#Processando os dados
pipeline()
df_partidas_processado = pd.read_csv("data/processed/matches_1930_2022.csv")
df_copa_do_mundo_processado = pd.read_csv("data/processed/world_cup.csv")

#Dashboard
st.title("Análise Exploratória da Copa do Mundo FIFA Masculino 1930 - 2022")
with st.container():
    column1, column2 = st.columns([2,1])
    with column1:
        ranking_paises_titulos(df_copa_do_mundo_processado)
    
    with column2:
        pais_menos_frequencia(df_partidas_processado)
        pais_mais_frequencia(df_partidas_processado)
        pais_mais_gols(df_partidas_processado)
        pais_mais_frequencia_final(df_partidas_processado)


evolucao_gols_copa_do_mundo(df_partidas_processado)
ranking_paises_gols(df_partidas_processado)

st.divider()

with st.expander("Dataset de Partidas 1930-2022"):
    st.header("Dataset de Partidas 1930-2022")
    st.text(f"Linhas: {df_partidas.shape[0]}, Colunas: {df_partidas.shape[1]}")
    st.dataframe(df_partidas)

with st.expander("Dataset da Copa do Mundo"):
    st.header("Dataset da Copa do Mundo")
    st.text(f"Linhas: {df_copa_do_mundo.shape[0]}, Colunas: {df_copa_do_mundo.shape[1]}")
    st.dataframe(df_copa_do_mundo)


