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
        yaxis={'categoryorder':'total ascending'}
    )
    st.plotly_chart(fig)
