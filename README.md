🔎 O que o código faz:

Faz uma requisição HTTP ao site do IBGE simulando um navegador real (com User-Agent) para evitar bloqueios.

Utiliza BeautifulSoup para extrair os indicadores exibidos na página de cada estado.

Organiza os dados em um dicionário Python com pares Indicador → Valor.

Converte os dados em um DataFrame do pandas, estruturado em tabela.

Cria uma interface no Streamlit onde o usuário escolhe o estado por meio de um selectbox.

Exibe os indicadores em uma tabela interativa, diretamente no navegador.

🚀 Tecnologias utilizadas:

- Python
- Requests
- BeautifulSoup4
- Pandas
- Streamlit

💡 Como usar:

1 - Clone este repositório.

2 - Instale as dependências:
```
pip install -r requirements.txt
```
3 - No terminal rode o App com:
```
streamlit run extract_ibge.py ()
```

