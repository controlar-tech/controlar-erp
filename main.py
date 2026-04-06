import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Controlar Tecnologia", layout="wide")

# Estilização (Fundo Escuro e Azul Celeste)
st.markdown("""
    <style>
    .main { background-color: #0B132B; color: white; }
    [data-testid="stSidebar"] { background-color: #1C2541; border-right: 1px solid #3A506B; }
    .stButton>button { width: 100%; background-color: #00B4D8; color: white; font-weight: bold; border-radius: 8px; }
    .menu-selecionado { color: #00B4D8 !important; font-weight: bold; font-size: 1.2rem; }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Tela de Login
if not st.session_state.logged_in:
    cols = st.columns([1,1.5,1])
    with cols[1]:
        st.write("# 🛡️ Controlar Tecnologia")
        st.divider()
        user_input = st.text_input("E-mail")
        pwd_input = st.text_input("Senha", type="password")
        if st.button("ACESSAR SISTEMA"):
            if user_input == "admin@controlar.com" and pwd_input == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")
else:
    # Sidebar
    st.sidebar.title("🛡️ Controlar")
    opcao = st.sidebar.radio("Menu Principal", ["🏠 Home", "📂 Cadastros", "💸 Financeiro"])
    if st.sidebar.button("🚪 Sair"):
        st.session_state.logged_in = False
        st.rerun()

    # Conteúdo
    st.title(f"Módulo: {opcao}")
    st.info("Sistema operando via GitHub / Streamlit Cloud")
