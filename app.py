import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Proteção por login
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")
    st.stop()

# Configuração da página
st.set_page_config(
    page_title="Gerador de conteúdo 🤖", 
    page_icon="🤖",
    layout="centered"
)

st.title("Gerador de Conteúdo 🤖")

# Verificar se a chave da API está configurada
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ Chave da API da OpenAI não encontrada. Configure no arquivo .env")
    st.stop()

client = OpenAI(api_key=api_key)

# Função de carregamento do modelo
@st.cache_resource
def load_model():
    return "gpt-4o"  # ou outro modelo disponível

# Geração via OpenAI
def llm_generate(prompt, model="gpt-4o", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": "Você é um especialista em marketing digital com foco em SEO e escrita persuasiva."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Erro ao chamar a API da OpenAI: {e}")
        return None

# Função para limites por plataforma
def get_char_limit(platform):
    limits = {
        "LinkedIn": (500, 1000),
        "X": (0, 280),
        "Facebook": (480, 2000),
        "Instagram": (0, 2000),
    }
    return limits.get(platform, (0, 0))  # (mínimo, máximo)

# Sidebar
with st.sidebar:
    st.image("logo.png")  # Logo
    st.markdown("<div style='text-align: center; font-weight: bold;'>Ideatore.</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.header("Configurações")
    st.info("O agente de texto lhe auxiliará a criar conteúdos otimizados para SEO, adaptados ao seu público e plataforma.")
    st.markdown("---")
    st.caption("© 2025 Ideatore. Todos os direitos reservados.")

# Formulário principal
st.subheader("📝 Configurações do Conteúdo")

col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Tema:", placeholder="Ex: saúde mental, alimentação saudável, prevenção, etc.")
    platform = st.selectbox("Plataforma:", ['Instagram', 'Facebook', 'LinkedIn', 'X', 'Blog', 'E-mail'])
    tone = st.selectbox("Tom:", ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'])

with col2:
    length = st.selectbox("Tamanho:", ['Curto', 'Médio', 'Longo'])
    audience = st.selectbox("Público-alvo:", ['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Empresário', 'Revenda', 'Especialistas', 'Adolescentes'])

st.write("---")

col3, col4 = st.columns(2)
with col3:
    cta = st.checkbox("Incluir CTA")
    hashtags = st.checkbox("Retornar Hashtags")

with col4:
    keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: bem-estar, medicina preventiva...")

# Botão de geração
if st.button("🚀 Gerar Conteúdo", type="primary", use_container_width=True):
    if not topic:
        st.warning("⚠️ Por favor, insira um tema para gerar o conteúdo.")
    else:
        min_chars, max_chars = get_char_limit(platform)

        # Prompt com base nas escolhas
        prompt = f"""
        Escreva um texto com SEO otimizado sobre o tema '{topic}'.
        Retorne em sua resposta apenas o texto final e não inclua ela dentro de aspas.

        - Onde será publicado: {platform}.
        - Tom: {tone}.
        - Público-alvo: {audience}.
        - Comprimento: {length}.
        - {"Inclua uma chamada para ação clara." if cta else "Não inclua chamada para ação"}
        - {"Retorne ao final do texto hashtags relevantes." if hashtags else "Não inclua hashtags."}
        {"- Palavras-chave que devem estar presentes nesse texto (para SEO): " + keywords if keywords else ""}
        {"- O texto deve conter no máximo " + str(max_chars) + " caracteres." if max_chars > 0 else ""}
        {"- O texto deve conter no mínimo " + str(min_chars) + " caracteres." if min_chars > 0 else ""}
        """

        with st.spinner("🤖 Gerando conteúdo personalizado..."):
            model = load_model()
            response = llm_generate(prompt, model=model)

            if response:
                st.success("✅ Conteúdo gerado com sucesso!")
                st.write("---")
                st.subheader("📋 Seu Conteúdo:")
                st.markdown(f"**Plataforma:** {platform} | **Tom:** {tone} | **Público:** {audience}")
                st.write("---")
                st.markdown(response)

                # Contador de caracteres
                char_count = len(response)
                st.markdown(f"📏 **Total de caracteres:** `{char_count}`")

                # Validação de limite
                if max_chars > 0 and char_count > max_chars:
                    st.warning(f"⚠️ O texto excede o limite de {max_chars} caracteres para {platform}.")
                elif min_chars > 0 and char_count < min_chars:
                    st.warning(f"⚠️ O texto está abaixo do mínimo de {min_chars} caracteres para {platform}.")

