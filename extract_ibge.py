# Bibliotecas
import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

# função procura estado
def scraping_uf(uf:str):
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    browsers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0"}
    page = requests.get(uf_url, headers=browsers)

    soup = BeautifulSoup(page.content, "html.parser")
    indicadores = soup.select(".indicador")
    
    uf_dict = {
        dado.select(".ind-label")[0].text: dado.select(".ind-value")[0].text
        for dado in indicadores
    }

    return uf_dict
    
estado = scraping_uf("sp")

for indicador in estado:
    if "]" in estado[indicador]:
        estado[indicador] = estado[indicador].split("]")[0][:-8]
    else:
        estado[indicador] = estado[indicador]


# ufs válidas
ufs = [
    "","ac","al","ap","am","ba","ce","df","es","go","ma","mt","ms","mg",
    "pa","pb","pr","pe","pi","rj","rn","rs","ro","rr","sc","sp","se","to"
]

# Interface no Streamlit
st.title("📊 Indicadores por Estado - IBGE")

uf_input = st.selectbox("Escolha o estado:", ufs)

if uf_input:
    try:
        estado = scraping_uf(uf_input.lower())
        df = pd.DataFrame(estado.values(), index=estado.keys(), columns=["Informação"])
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao buscar os dados: {e}")