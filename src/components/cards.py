import streamlit as st
import pandas as pd

st.markdown("""
<style>
.card {
    background-color: #1A1D24;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #2A2E39;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

def pais_menos_frequencia(df):
    df_paises = pd.concat([df['home_team'], df['away_team']], axis=0)
    paises_freq = df_paises.value_counts().reset_index()
    pais_menos_freq = paises_freq.iloc[-1].values
    st.markdown(f'<div class="card">País com menos frequência na copa<br><b>{pais_menos_freq[0]} - {pais_menos_freq[1]} vez</b></div>', unsafe_allow_html=True)

def pais_mais_frequencia(df):
    df_paises = pd.concat([df['home_team'], df['away_team']], axis=0)
    paises_freq = df_paises.value_counts().reset_index()
    pais_mais_freq = paises_freq.iloc[0].values
    print(pais_mais_freq)
    st.markdown(f'<div class="card">País com mais frequência na copa<br><b>{pais_mais_freq[0]} - {pais_mais_freq[1]} vezes</b></div>', unsafe_allow_html=True)

def pais_mais_gols(df):
    df_home_team = df[['home_team', 'home_score']].rename(
        columns={'home_team':'País','home_score':'Gols'}
    )
    df_away_team = df[['away_team', 'away_score']].rename(
        columns={'away_team':'País','away_score':'Gols'}
    )
    df_paises_gols = pd.concat([df_home_team, df_away_team])
    df_paises_gols = df_paises_gols.groupby('País')[['Gols']].sum().reset_index()
    df_paises_gols =df_paises_gols.sort_values(by='Gols', ascending=False)
    pais_gols = df_paises_gols.iloc[0].values
    st.markdown(f'<div class="card">País com mais gols<br><b>{pais_gols[0]} - {pais_gols[1]} gols</b></div>', unsafe_allow_html=True)


def pais_mais_frequencia_final(df):
    df_home_team = df[['home_team', 'Round']].rename(
        columns={'home_team':'País','Round':'Rodada'}
    )
    df_away_team = df[['away_team', 'Round']].rename(
        columns={'away_team':'País','Round':'Rodada'}
    )
    df_paises_rodadas = pd.concat([df_home_team, df_away_team])
    df_paises_rodadas = df_paises_rodadas.groupby(['País'])[['Rodada']].value_counts().reset_index()
    df_paises_rodada_final = df_paises_rodadas[df_paises_rodadas['Rodada'] == 'Final'].sort_values(by=['count'], ascending=False)
    pais_freq_final = df_paises_rodada_final.iloc[0].values
    st.markdown(f'<div class="card">País com mais frequência nas finais<br><b>{pais_freq_final[0]} - {pais_freq_final[2]} vezes</b></div>', unsafe_allow_html=True)