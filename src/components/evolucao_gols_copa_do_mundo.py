import pandas as pd
import streamlit as st
import plotly.express as px

def evolucao_gols_copa_do_mundo(df: pd.DataFrame) -> None:
    
    # Total de gols por partida
    df['total_gols'] = (
        df['home_score'].fillna(0) +
        df['home_penalty'].fillna(0) +
        df['away_score'].fillna(0) +
        df['away_penalty'].fillna(0)
    )
    
    # Agrupamento por ano
    gols_por_ano = df.groupby('Year').agg(
        total_gols=('total_gols', 'sum'),
        total_jogos=('total_gols', 'count')
    ).reset_index()
    
    # Média de gols por jogo
    gols_por_ano['media_gols'] = (
        gols_por_ano['total_gols'] / gols_por_ano['total_jogos']
    )

    # Gráfico
    fig = px.line(
        gols_por_ano,
        x="Year",
        y="media_gols",
        title='Média de Gols por Jogo na Copa do Mundo',
        markers=True,
        range_x=[gols_por_ano['Year'].min(), gols_por_ano['Year'].max()]
    )

    fig.update_layout(
        xaxis=dict(
            title=dict(text="Ano"),
            # Define o modo de ticks como 'array'
            tickmode='array',
            # Passa a lista exata de anos que existem no seu agrupamento
            tickvals=gols_por_ano['Year'],
            # Rotaciona para evitar que os números batam uns nos outros
            tickangle=-45 
        ),
        yaxis=dict(
            title=dict(text="Média de gols por jogo"),
            rangemode='tozero'
        )
    )

    fig.update_xaxes(
        range=[gols_por_ano['Year'].min(), gols_por_ano['Year'].max()]
    )
    st.plotly_chart(fig)
