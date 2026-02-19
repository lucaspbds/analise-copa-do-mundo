import pandas as pd

#Dicionário para mapear os nomes dos países históricos para os nomes atuais
mapeando_paises = {
    "West Germany": "Germany",
    "Germany DR": "Germany",
    "Soviet Union": "Russia",
    "Yugoslavia": "Serbia",
    "FR Yugoslavia": "Serbia",
    "Serbia and Montenegro": "Serbia",
    "Czechoslovakia": "Czech Republic",
    "Zaire": "DR Congo",
    "Dutch East Indies": "Indonesia",
    "Türkiye": "Turkey",
    "IR Iran": "Iran",
    "China PR": "China"
}

def ler_arquivo_csv(df_path:str) -> pd.DataFrame:
    """
    Função para ler um arquivo CSB e retornar um DataFrame do pandas.
    
    Args:
        df_path (str): O caminho do arquivo CSV a ser lido.

    Returns:
        pd.DataFrame: O DataFrame resultante da leitura do arquivo CSV.
    """
    return pd.read_csv(df_path, encoding="utf-8")

def categorizar_fase(df_partidas:pd.DataFrame) -> pd.DataFrame:
    """ 
    Função para categorizar as fases do campeonato em "Final", "Semi-finals", 
    "Quarter-finals", "Round of 16" e "Other stages".
    Args:
        df_partidas (pd.DataFrame): O DataFrame contendo os dados das partidas.
    Returns:
        pd.DataFrame: O DataFrame com a nova coluna "Round_clean" contendo as categorias das fases do campeonato.
    """

    df_partidas["Round_clean"] = df_partidas.apply(lambda linha: "Other stages" if linha["Round"] not in ["Final", "Semi-finals", "Quarter-finals", "Round of 16"] else linha["Round"], axis=1)
    return df_partidas

def corrigir_nomes_paises_historicos(df:pd.DataFrame, colunas:list) -> pd.DataFrame:
    """
    Função para corrigir os nomes dos países históricos no DataFrame.
    
    Args:
        df (pd.DataFrame): O DataFrame com nomes de países a serem corrigidos.
        colunas (list): A lista de colunas a serem corrigidas (ex: ["home_team", "away_team"]).

    Returns:
        pd.DataFrame: O DataFrame com os nomes dos países corrigidos.
    """
    for coluna in colunas:
        df[coluna] = df[coluna].apply(lambda nome_pais: mapeando_paises.get(nome_pais, nome_pais))
    return df

def salvar_dataframe(df:pd.DataFrame, path:str):
    """
    Função para salvar um DataFrame em um arquivo CSV.
    
    Args:
        df (pd.DataFrame): O DataFrame a ser salvo.
        path (str): O caminho do arquivo CSV onde o DataFrame será salvo.
    """
    df.to_csv(path, index=False, encoding="utf-8")

def pipeline():
    df_partidas = ler_arquivo_csv("data/raw/matches_1930_2022.csv")
    df_copa_do_mundo = ler_arquivo_csv("data/raw/world_cup.csv")

    #Separando as fases do campeonato em "Final", "Semi-finals", "Quarter-finals", "Round of 16" e "Other stages"
    df_partidas = categorizar_fase(df_partidas)

    #Atualizando os nomes dos países históricos para os nomes atuais
    df_partidas = corrigir_nomes_paises_historicos(df_partidas, ["home_team", "away_team"])
    df_copa_do_mundo = corrigir_nomes_paises_historicos(df_copa_do_mundo, ["Champion", "Runner-Up"])  

    #Salvando os DataFrames atualizados
    salvar_dataframe(df_partidas, "data/processed/matches_1930_2022.csv")
    salvar_dataframe(df_copa_do_mundo, "data/processed/world_cup.csv")