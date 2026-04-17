import streamlit as st
import plotly.express as px
import pandas as pd
def ranking_paises_titulos(df:pd.DataFrame) -> None:
    """
    Função responsável por montar um gráfico de barras na horizontal
    mostrando o nome do país (eixo y) e o número de títulos (eixo x).
    
    Args:
        df (pd.DataFrame): Dataframe do arquivo world_cup.
    """

    ranking_paises = df.groupby("Champion").agg(
        qtd_titulos=("Champion", "count")).reset_index()
    fig = px.bar(ranking_paises, 
                 x="qtd_titulos",
                 y="Champion",
                 title="Ranking dos países de acordo com os títulos",
                 orientation='h',
                 color='Champion')
    fig.update_layout(
        xaxis=dict(
            title=dict(text='Títulos'),
            tickmode='array',
            tickvals=ranking_paises['qtd_titulos'].dropna()
        ),
        yaxis=dict(
            title=dict(text='Países'),
            categoryorder='total ascending'),
        legend=dict(
            title=dict(text='Países')
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)


