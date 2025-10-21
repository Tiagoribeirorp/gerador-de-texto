# Gerador de Conteúdo  🤖

## Visão Geral do Projeto

Este projeto é um Gerador de Conteúdo interativo desenvolvido com Streamlit, focado em otimização para SEO e Marketing Digital. Ele permite que os usuários gerem conteúdo personalizado para diversas plataformas, como Instagram, Facebook, LinkedIn, X (Twitter), Blog e E-mail, com base em parâmetros configuráveis como tema, tom, público-alvo e palavras-chave.

O aplicativo utiliza a API da OpenAI para a geração inteligente de texto, garantindo conteúdo relevante e de alta qualidade. Além disso, incorpora um sistema de autenticação de usuário simples para controlar o acesso à ferramenta.

## Funcionalidades

•Geração de Conteúdo Personalizado: Crie textos otimizados para diferentes plataformas e públicos.

•Otimização para SEO: Inclua palavras-chave específicas para melhorar o ranqueamento do conteúdo.

•Parâmetros Configuráveis: Defina tema, tom de voz, público-alvo, comprimento do texto, e opções para Call-to-Action (CTA) e hashtags.

•Validação de Limite de Caracteres: Alertas para limites de caracteres específicos de cada plataforma (ex: X/Twitter, LinkedIn).

•Autenticação de Usuário: Sistema de login básico para proteger o acesso à aplicação.

•Integração com OpenAI API: Utiliza modelos de linguagem avançados para gerar conteúdo criativo e persuasivo.

## Tecnologias Utilizadas

•Python: Linguagem de programação principal.

•Streamlit: Framework para construção de aplicações web interativas e de fácil implantação.

•OpenAI API: Para a geração de texto inteligente.

•python-dotenv: Para o gerenciamento de variáveis de ambiente.

•langchain-groq, langchain-core: Possivelmente para futuras integrações ou abstrações de modelos de linguagem, embora não explicitamente utilizados no app.py principal para a geração via OpenAI diretamente.

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Clonar o Repositório

Bash


git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

Bash


python -m venv venv
source venv/bin/activate  # No Linux/macOS
venc\Scripts\activate     # No Windows


### 3. Instalar as Dependências

Bash


pip install -r requirements.txt


### 4. Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e adicione sua chave da API da OpenAI:

Plain Text


OPENAI_API_KEY="sua_chave_aqui"


#### Importante: Nunca compartilhe sua chave de API publicamente. Certifique-se de que o arquivo .env esteja incluído no .gitignore.

### 5. Executar a Aplicação

Para iniciar a aplicação Streamlit, execute:

Bash


streamlit run login.py


A aplicação será aberta no seu navegador padrão. Você precisará fazer login para acessar o gerador de conteúdo. Os usuários padrão são:

•Usuário: admin / Senha: senha123

•Usuário: usuario / Senha: senha456

## Estrutura do Projeto

•app.py: Contém a lógica principal do gerador de conteúdo, interface Streamlit e integração com a OpenAI.

•login.py: Implementa o sistema de autenticação de usuário.

•sobre.py: Página com informações sobre a aplicação.

•requirements.txt: Lista as dependências do projeto.

•.env: Arquivo para variáveis de ambiente (não versionado).

•.gitignore: Define arquivos e diretórios a serem ignorados pelo Git.

## Como Contribuir

1.Faça um fork do projeto.

2.Crie uma nova branch (git checkout -b feature/nova-funcionalidade).

3.Faça suas alterações e commit (git commit -m 'Adiciona nova funcionalidade').

4.Envie para a branch original (git push origin feature/nova-funcionalidade).

5.Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato com [Seu Nome/Organização] via [Seu Email/Link de Contato].

