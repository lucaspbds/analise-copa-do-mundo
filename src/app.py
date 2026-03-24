import streamlit as st
import pandas as pd
from components.ranking_paises_titulos import ranking_paises_titulos
from components.evolucao_gols_copa_do_mundo import evolucao_gols_copa_do_mundo
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
st.title("Análise da Copa do Mundo FIFA Masculino 1930 - 2022")
st.header("Copa do Mundo 1930-2022")
ranking_paises_titulos(df_copa_do_mundo_processado)
evolucao_gols_copa_do_mundo(df_partidas_processado)
st.divider()

st.header("Dataset de Partidas 1930-2022")
st.text(f"Linhas: {df_partidas.shape[0]}, Colunas: {df_partidas.shape[1]}")
st.dataframe(df_partidas)

st.header("Dataset da Copa do Mundo")
st.text(f"Linhas: {df_copa_do_mundo.shape[0]}, Colunas: {df_copa_do_mundo.shape[1]}")
st.dataframe(df_copa_do_mundo)
freq = df_copa_do_mundo["Champion"].value_counts()

