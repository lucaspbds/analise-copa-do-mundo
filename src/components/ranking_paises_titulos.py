import streamlit as st
import pandas as pd
def ranking_paises_titulos(df:pd.DataFrame):
    st.subheader("Ranking dos países de acordo com os títulos")
    freq = df["Champion"].value_counts()
    st.bar_chart(freq, x_label="Títulos", y_label="Países", horizontal=True, sort=False)
