from email.message import Message
import streamlit as st
from controller.controller import ControladorSupermercado

def main(caminho):
    controlador = ControladorSupermercado(caminho)
    controlador.modelo.criar_coluna_mes()
    st.sidebar.markdown(' :balloon: __Nossas Opções__ :ballon: ')
    mes = st.sidebar.radio("Mês", controlador.modelo.df["Mes"].unique())
    controlador.executar(mes)

if __name__ == "__main__":
    st.set_page_config(page_title="Exemplo Final", page_icon="😎", layout="wide")
    main("./assets/imobiliariaDados.csv")