import streamlit as st
from pathlib import Path
import base64
from PIL import Image

from roi_calculator import render_roi_calculator  # <- módulo da calculadora

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# ============================================================
# CSS HÍBRIDO (neon nos pontos-chave, corpo mais clean)
# ============================================================
CUSTOM_CSS = """
<style>

/* Fundo geral */
body, .stApp {
    background-color: #050608;
    color: #f2f2f2;
    font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
}

/* Container central */
.main-block {
    max-width: 1000px;
    margin: 0 auto;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #00ff9a;
    font-weight: 700;
}

/* Divisores */
.section-divider {
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin: 3rem 0 2rem 0;
}

/* Cards genéricos usados nos passos e depoimentos */
.plan-card {
    background: rgba(255,255,255,0.03);
    border-radius: 16px;
    border: 1px solid rgba(0,255,154,0.20);
    box-shadow: 0 0 14px rgba(0,255,154,0.20);
    padding: 1.2rem 1.3rem;
    transition: 0.2s;
}
.plan-card:hover {
    box-shadow: 0 0 22px rgba(0,255,154,0.35);
    transform: translateY(-2px);
}

/* Botões de link (st.link_button) */
a[kind="secondary"], a[kind="primary"] {
    display: inline-block;
    border: 2px solid #00ff9a;
    color: #ff7a1a !important;
    background: transparent !important;
    padding: 0.55rem 1.7rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none !important;
    cursor: pointer;
    transition: 0.18s ease-in-out;
}
a[kind="secondary"]:hover,
a[kind="primary"]:hover {
    box-shadow: 0 0 12px #00ff9a;
    transform: translateY(-2px);
}

/* Botões normais */
.stButton>button {
    background: linear-gradient(90deg, #00ff9a, #ff7a1a);
    color: #050608 !important;
    border-radius: 999px;
    border: none;
    padding: 0.6rem 1.8rem;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    transition: 0.2s ease-in-out;
}
.stButton>button:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
}

/* Textos auxiliares */
.hero-subtitle {
    font-size: 1.05rem;
    color: #d7d7d7;
}
.subtle-center {
    text-align:center;
    color:#d7d7d7;
}

/* Pequeno destaque em laranja */
.highlight {
    color: #ff7a1a;
    font-weight: 600;
}

/* Depoimentos */
.testimonial-role {
    color:#ff7a1a;
    font-size:0.85rem;
    text-align:right;
}

/* Ajustes mobile */
@media (max-width: 768px) {
    .main-block {
        padding: 0 0.6rem;
    }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================
# FUNÇÃO DE IMAGEM CIRCULAR COM NEON (para sua foto, se quiser)
# ============================================================
def circular_image(path, size=120):
    p = Path(path)
    if not p.exists():
        return ""
    img_bytes = p.read_bytes()
    img_b64 = base64.b64encode(img_bytes).decode()
    return f"""
    <div style="
        width:{size}px;
        height:{size}px;
        border-radius:50%;
        overflow:hidden;
        margin:12px 0 18px 0;
        border:3px solid #00ff9a;
        box-shadow:0 0 15px rgba(0,255,154,0.8);
    ">
        <img src="data:image/png;base64,{img_b64}"
             style="width:100%;height:100%;object-fit:cover;filter:grayscale(100%);">
    </div>
    """

# ============================================================
# LOGO PHOENIX
# ============================================================
try:
    logo = Image.open("Logo_phoenix.png")
    st.markdown(
        "<div style='display:flex; align-items:center; justify-content:flex-start; margin:10px 0 25px 0;'>",
        unsafe_allow_html=True
    )
    st.image(logo, width=260)
    st.markdown("</div>", unsafe_allow_html=True)
except:
    st.warning("⚠️ Logo não encontrada: coloque Logo_phoenix.png na mesma pasta do app.")

# ============================================================
# INÍCIO DO CONTEÚDO
# ============================================================
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

# ------------------------------------------------------------
# HERO
# ------------------------------------------------------------
st.markdown("""
<div style='text-align:center; margin-top:1.5rem;'>
    <h1 style='color:#00ff9a; font-size:2.5rem; font-weight:700; margin-bottom:0.2rem;'>
        Phoenix Strategy
    </h1>
    <p style='color:#ff7a1a; font-size:1.15rem; margin-top:0;'>
        O algoritmo que transforma análise técnica em precisão real.
    </p>
    <p style='color:#d7d7d7; max-width:700px; margin:0.8rem auto 1.4rem auto; font-size:1.02rem;'>
        Uma plataforma que monitora centenas de ativos em tempo real, calcula probabilidades
        e envia <span class="highlight">alertas prontos de entrada e saída</span> para você operar
        com clareza — mesmo sem ficar na tela o dia inteiro.
    </p>
    <div style='margin-top:1.2rem;'>
        <a href="https://phoenix-strategy.onrender.com/dashboard_geral" target="_blank"
           style="
               display:inline-block;
               background:linear-gradient(90deg, #00ff9a, #ff7a1a);
               padding:0.85rem 2.4rem;
               border-radius:999px;
               color:#050608 !important;
               font-weight:700;
               font-size:1.05rem;
               text-decoration:none;
               box-shadow:0 0 15px rgba(0,255,154,0.45);
               margin-right:0.6rem;
           ">
            🚀 Acessar Plataforma
        </a>
        <a href="https://phoenix-strategy.streamlit.app/Planos" target="_blank"
           style="
               display:inline-block;
               border:2px solid #00ff9a;
               padding:0.8rem 2.0rem;
               border-radius:999px;
               color:#00ff9a !important;
               font-weight:700;
               font-size:0.98rem;
               text-decoration:none;
           ">
            Ver planos e valores
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# O QUE É A PHOENIX STRATEGY
# ------------------------------------------------------------
st.markdown("### O que é a Phoenix Strategy?")
st.markdown("""
A **Phoenix Strategy** é um sistema quantitativo que combina análise técnica clássica,
leitura de fluxo, volatilidade e price action em um único algoritmo.

Enquanto um trader humano acompanha poucos ativos, a Phoenix monitora
**centenas de ações e opções a cada poucos minutos**, identifica padrões de alta probabilidade
e envia **sinais objetivos** de compra e venda.
""")

st.markdown("""
Não é uma “sala de sinais” tradicional.  
É uma **infraestrutura algorítmica** criada para entregar:

- Leituras consistentes, sem emoção  
- Alertas claros, com entrada, alvo e stop  
- Monitoramento contínuo do mercado  
- Operações com horizonte médio de **15 dias**, permitindo girar o capital duas vezes por mês
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# COMO FUNCIONA NA PRÁTICA — 3 PASSOS
# ------------------------------------------------------------
st.markdown(
    "<h2 style='color:#00ff9a; text-align:center;'>Como funciona na prática</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p class='subtle-center'>O processo é simples: o algoritmo faz o trabalho pesado, você executa com clareza.</p>",
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown("""
    <div class="plan-card" style="text-align:center;">
        <h3 style="color:#00ff9a; font-size:1.05rem;">1. O algoritmo monitora</h3>
        <p style="font-size:0.9rem; color:#d7d7d7;">
            A Phoenix avalia dezenas de variáveis em centenas de ativos:
            tendência, fluxo, volatilidade, assimetrias e contexto.
        </p>
    </div>
    """, unsafe_allow_html=True)

with step2:
    st.markdown("""
    <div class="plan-card" style="text-align:center;">
        <h3 style="color:#00ff9a; font-size:1.05rem;">2. Você recebe o alerta</h3>
        <p style="font-size:0.9rem; color:#d7d7d7;">
            Quando uma oportunidade é validada, você recebe um alerta com
            <strong>entrada, alvo e stop</strong> diretamente no celular.
        </p>
    </div>
    """, unsafe_allow_html=True)

with step3:
    st.markdown("""
    <div class="plan-card" style="text-align:center;">
        <h3 style="color:#00ff9a; font-size:1.05rem;">3. Executa em segundos</h3>
        <p style="font-size:0.9rem; color:#d7d7d7;">
            Basta executar a ordem na sua corretora preferida conforme o alerta.
            A plataforma acompanha tudo em tempo real.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# ROI & PAYBACK + CALCULADORA
# ------------------------------------------------------------
st.markdown(
    "<h2 style='color:#00ff9a; text-align:center;'>Entenda o ROI e o tempo de payback</h2>",
    unsafe_allow_html=True
)

st.markdown("""
<p style='text-align:center; color:#d7d7d7; max-width:800px; margin:0 auto;'>
<strong>ROI (Return on Investment)</strong> é o retorno sobre o capital que você coloca nas operações.  
<strong>Payback</strong> é o tempo que a assinatura leva para se pagar com os resultados das operações.
<br><br>
Como as operações da Phoenix costumam durar em média <strong>15 dias</strong> entre entrada e saída,
o capital gira aproximadamente <strong>duas vezes por mês</strong>, acelerando naturalmente o payback.
Use a calculadora abaixo para simular, de forma educacional, diferentes cenários de capital, plano e horizonte de tempo.
</p>
""", unsafe_allow_html=True)

# Calculadora (HTML via st.components)
render_roi_calculator()

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# DEPOIMENTOS
# ------------------------------------------------------------
st.markdown(
    "<h2 style='color:#00ff9a; text-align:center;'>O que os usuários dizem</h2>",
    unsafe_allow_html=True
)

d1, d2, d3 = st.columns(3)

with d1:
    st.markdown("""
    <div class="plan-card">
        <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Nunca tinha operado ações. Hoje só sigo os alertas e executo pelo celular.
            A sensação de ter alguém filtrando o mercado por mim é absurda.”
        </p>
        <p class='testimonial-role'>— Investidor Iniciante</p>
    </div>
    """, unsafe_allow_html=True)

with d2:
    st.markdown("""
    <div class="plan-card">
        <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Eu não tenho tempo para ficar em frente ao gráfico. Os sinais chegam objetivos,
            com entrada e stop definidos. Isso devolveu confiança e disciplina.”
        </p>
        <p class='testimonial-role'>— Investidor Intermediário</p>
    </div>
    """, unsafe_allow_html=True)

with d3:
    st.markdown("""
    <div class="plan-card">
        <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Como profissional, uso o scanner para validar rapidamente o que antes levava horas.
            A curadoria algorítmica economiza tempo e evita vieses.”
        </p>
        <p class='testimonial-role'>— Trader Avançado</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# SOBRE O CRIADOR (VERSÃO CURTA)
# ------------------------------------------------------------
col1, col2 = st.columns([0.35, 1])

with col1:
    st.markdown(circular_image("eu.png", size=130), unsafe_allow_html=True)

with col2:
    st.markdown("""
    #### Quem está por trás da Phoenix Strategy?
    Sou estrategista financeiro, certificado no Brasil e formado em programação e inteligência artificial na Europa.
    Minha especialidade é integrar análise técnica, derivativos e automação — para transformar metodologia em processo
    repetível e escalável.
    
    A Phoenix Strategy é o resultado dessa jornada: um algoritmo que honra os princípios clássicos da análise,
    mas executa com a velocidade e precisão que só a tecnologia permite.
    """)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# CTA FINAL
# ------------------------------------------------------------
st.markdown("""
<div style='text-align:center; margin:2rem 0 3rem 0;'>
    <a href="https://wa.me/351915323219" target="_blank"
       style="
           display:inline-block;
           background:linear-gradient(90deg, #00ff9a, #ff7a1a);
           padding:1rem 2.8rem;
           border-radius:999px;
           color:#050608 !important;
           font-weight:700;
           font-size:1.1rem;
           text-decoration:none;
           box-shadow:0 0 18px rgba(0,255,154,0.45);
       ">
        🔥 Quero entender meu ROI com o Phoenix Strategy
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha main-block
