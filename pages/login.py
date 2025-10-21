# pages/login.py

import streamlit as st

# Usuários e senhas armazenados localmente (ideal para uso interno), aqui conseguimos incrementar os usuários que quisermos
USERS = {
    "admin": "senha123",
    "usuario": "senha456"
}

# Função de autenticação
def login():
    st.sidebar.title("🔒 Login")
    username = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")
    login_button = st.sidebar.button("Entrar")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"✅ Bem-vindo, {username}!")
            #st.experimental_rerun()
        else:
            st.sidebar.error("Usuário ou senha inválidos")

# Controle de sessão
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()
else:
    st.success(f"Você já está logado como {st.session_state['username']}.")
    st.markdown("Acesse a [página principal](../app.py) pelo menu lateral.")
