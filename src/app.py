import streamlit as st
import pandas as pd

df_partidas = pd.read_csv("data/raw/matches_1930_2022.csv")
print(df_partidas.info())
print(df_partidas.describe())
df_fifa_ranking = pd.read_csv("data/raw/fifa_ranking_2022-10-06.csv")
print(df_fifa_ranking.info())
print(df_fifa_ranking.describe())
df_copa_do_mundo = pd.read_csv("data/raw/world_cup.csv")
print(df_copa_do_mundo.info())
print(df_copa_do_mundo.describe())
st.title("Análise da Copa do Mundo FIFA Masculino 1930 - 2022")

st.header("Dataset de Partidas 1930-2022")
st.text(f"Linhas: {df_partidas.shape[0]}, Colunas: {df_partidas.shape[1]}")
st.dataframe(df_partidas)

st.header("Dataset da Copa do Mundo")
st.text(f"Linhas: {df_copa_do_mundo.shape[0]}, Colunas: {df_copa_do_mundo.shape[1]}")
st.dataframe(df_copa_do_mundo)

