import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# CSS para diminuir o padding da página no Streamlit
st.markdown(
    """
    <style>
    /* Reduzir o espaçamento superior e lateral da página */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Produtos")

data = pd.read_excel('teste-01.xlsx')
st.write(data)

id_txt = st.text_input("Digite o código do produto:", "").upper()

if id_txt:
    produto = data[data['id_produto'] == id_txt]
    
    if not produto.empty:
        codigo = produto.iloc[0]['id_produto']
        nome = produto.iloc[0]['nome_produto']
        
        st.write(f"**Código do Produto:** {codigo}")
        st.write(f"**Nome do Produto:** {nome}")
        
        # Caminho da imagem do produto
        imagem_path = f"{codigo}.png"  # Substitua pela pasta correta onde as imagens estão
        st.image(imagem_path)
    else:
        st.error("Produto não encontrado.")