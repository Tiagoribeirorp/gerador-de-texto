import streamlit as st

st.set_page_config(page_title="Sobre", page_icon="ℹ️")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")
    st.stop()

st.title("ℹ️ Sobre a Aplicação")
st.markdown("""
Este projeto foi desenvolvido para auxiliar na criação de conteúdo com foco em SEO e marketing digital.
""")
st.image("logo.png", width=100)