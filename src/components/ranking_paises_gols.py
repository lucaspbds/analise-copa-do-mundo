import pandas as pd
import streamlit as st
import plotly.express as px
def ranking_paises_gols(df:pd.DataFrame) -> None:
    """
    Função responsável por criar o gráfico de linha que mostra a evolução de cada 
    país referente a quantidade de gols em cada edição da copa do mundo.

    Args:
        df (pd.Dataframe) = Dataframe de todas as partidas das copas do mundo.
    """
    #Selecionando o time da casa
    df_home_team = df[['Year', 'home_team','home_score', 'home_penalty']].rename(
        columns={'Year': 'Ano', 'home_team': 'País', 'home_score':'gols', 'home_penalty':'gols_penalty'})
    #Selecionando o time de fora
    df_away_team = df[['Year', 'away_team', 'away_score', 'away_penalty']].rename(
        columns={'Year': 'Ano', 'away_team': 'País', 'away_score':'gols', 'away_penalty':'gols_penalty'})
    #Juntando os dois dataframes em um só dataframe
    ranking_paises_gols = pd.concat([df_home_team, df_away_team])
    #Agrupando por Ano e País para tirar as duplicidades
    ranking_paises_gols = ranking_paises_gols.groupby(by=['Ano', 'País'])[['gols','gols_penalty']].sum().reset_index()
    ranking_paises_gols['Total_gols'] = ranking_paises_gols['gols'].fillna(0) + ranking_paises_gols['gols_penalty'].fillna(0)
    fig = px.line(
        ranking_paises_gols, 
        title='Evolução Histórica de Gols por Seleção (1930–2022)',
        x='Ano', 
        y='Total_gols', 
        color='País')
    fig.update_layout(
        xaxis=dict(
            title=dict(text="Ano"),
            # Define o modo de ticks como 'array'
            tickmode='array',
            # Passa a lista exata de anos que existem no seu agrupamento
            tickvals=ranking_paises_gols['Ano'].dropna(),
            # Rotaciona para evitar que os números batam uns nos outros
            tickangle=-45
        ),
        yaxis=dict(
            title=dict(text='Total de Gols')
        ),
        margin=dict(t=30,l=10,b=10,r=10)
    )
    fig.update_xaxes(
        range=[ranking_paises_gols['Ano'].min(), ranking_paises_gols['Ano'].max()])
    
    st.plotly_chart(fig)
