import streamlit as st

st.set_page_config(
    page_title="Planos – Phoenix Strategy",
    page_icon="🔥",
    layout="wide"
)

st.markdown("""
<style>
    .wrapper {
        max-width: 1100px;
        margin: 0 auto;
        margin-top: 2rem;
    }

    .title {
        color: #00ff9a;
        text-align: center;
        font-size: 2rem;
        margin-bottom: 0.3rem;
        font-weight:700;
    }

    .subtitle {
        text-align: center;
        font-size: 1rem;
        color: #d7d7d7;
        margin-bottom: 2.2rem;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
    }

    @media(max-width: 1000px) {
        .grid {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    .plan-card-wrapper {
        background: rgba(255,255,255,0.03);
        border-radius: 20px;
        padding: 1.8rem 1.7rem;
        border: 1px solid rgba(0,255,154,0.28);
        box-shadow: 0 0 18px rgba(0,255,154,0.28);
        transition: 0.25s;
    }

    .plan-card-wrapper:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 30px rgba(0,255,154,0.55);
    }

    .badge {
        background: #ff7a1a;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        color: #000;
    }

    .badge-green {
        background: #00ff9a;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        color: #000;
    }

    .plan-title {
        margin-top: 1rem;
        margin-bottom: 0.4rem;
        color: #ffffff;
        font-size: 1.4rem;
        font-weight:700;
    }

    .plan-desc {
        font-size: 0.95rem;
        color: #d7d7d7;
        margin-bottom: 1rem;
    }

    .price-highlight {
        font-size: 1.1rem;
        color: #00ff9a;
        margin-bottom: 0.6rem;
        font-weight: 600;
    }

    .price-table {
        font-size: 0.9rem;
        color: #d7d7d7;
        margin-top: 0.4rem;
        margin-bottom: 0.6rem;
    }

    .price-table span.label {
        color: #aaaaaa;
    }

    .cta-btn {
        margin-top: 0.8rem;
        text-align:center;
    }

    .cta-btn a {
        background: transparent;
        border: 2px solid #00ff9a;
        color: #00ff9a !important;
        padding: 0.55rem 2.0rem;
        border-radius: 50px;
        font-weight: 700;
        font-size:0.95rem;
        text-decoration: none;
        transition: 0.25s;
        display:inline-block;
    }

    .cta-btn a:hover {
        background: #00ff9a;
        color: #000 !important;
        box-shadow: 0 0 18px rgba(0,255,154,0.45);
    }

    .footnote {
        text-align:center;
        color:#888;
        font-size:0.8rem;
        margin-top:2rem;
        max-width:800px;
        margin-left:auto;
        margin-right:auto;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='wrapper'>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Planos Phoenix Strategy</h1>", unsafe_allow_html=True)
st.markdown("""
<p class='subtitle'>
Escolha o plano que mais se conecta com a forma como você opera.  
Quanto maior o período, menor o custo mensal e mais rápido o payback da sua assinatura.
</p>
""", unsafe_allow_html=True)

st.markdown("<div class='grid'>", unsafe_allow_html=True)

# ---------------------- PHOENIX EQUITY ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge'>Mais Vendido</span>
    <h2 class='plan-title'>Phoenix Equity</h2>
    <p class='plan-desc'>
        Combina <strong>IBOV + Small Caps + BDR</strong> em uma única assinatura.
        Ideal para quem quer operar ações com diversificação e filtros algorítmicos.
    </p>
    <p class='price-highlight'>
        A partir de <strong>R$ 247/mês</strong> no plano anual.
    </p>
    <div class='price-table'>
        <div><span class='label'>Plano Mensal:</span> R$ 309/mês</div>
        <div><span class='label'>Plano Trimestral:</span> R$ 272/mês</div>
        <div><span class='label'>Plano Anual:</span> equivalente a R$ 247/mês</div>
    </div>
    <div class='cta-btn'>
        <a href='https://wa.me/351915323219?text=Quero%20assinar%20o%20Phoenix%20Equity' target='_blank'>
            Assinar Phoenix Equity
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- PHOENIX FULL ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge-green'>Recomendado</span>
    <h2 class='plan-title'>Phoenix Full</h2>
    <p class='plan-desc'>
        Todas as carteiras em um único plano:
        <strong>IBOV, Small Caps, BDR e Opções</strong>.  
        Para quem quer aproveitar tanto movimentos em ações quanto assimetrias em derivativos.
    </p>
    <p class='price-highlight'>
        A partir de <strong>R$ 397/mês</strong> no plano anual.
    </p>
    <div class='price-table'>
        <div><span class='label'>Plano Mensal:</span> R$ 496/mês</div>
        <div><span class='label'>Plano Trimestral:</span> R$ 437/mês</div>
        <div><span class='label'>Plano Anual:</span> equivalente a R$ 397/mês</div>
    </div>
    <div class='cta-btn'>
        <a href='https://wa.me/351915323219?text=Quero%20assinar%20o%20Phoenix%20Full' target='_blank'>
            Assinar Phoenix Full
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- PHOENIX SCANNER PRO ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge-green'>Linha PRO</span>
    <h2 class='plan-title'>Phoenix Scanner PRO</h2>
    <p class='plan-desc'>
        Scanner profissional de <strong>Ações + Opções</strong>, focado em leitura de volatilidade,
        fluxo e assimetrias. Ideal para traders avançados, analistas e gestores.
    </p>
    <p class='price-highlight'>
        A partir de <strong>R$ 597/mês</strong> no plano anual.
    </p>
    <div class='price-table'>
        <div><span class='label'>Plano Mensal:</span> R$ 746/mês</div>
        <div><span class='label'>Plano Trimestral:</span> R$ 657/mês</div>
        <div><span class='label'>Plano Anual:</span> equivalente a R$ 597/mês</div>
    </div>
    <div class='cta-btn'>
        <a href='https://wa.me/351915323219?text=Quero%20assinar%20o%20Phoenix%20Scanner%20PRO' target='_blank'>
            Assinar Scanner PRO
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha grid

st.markdown("""
<p class='footnote'>
Os valores acima são referências de tabela e podem ser ajustados em campanhas específicas, combos ou upgrades.
Considere sempre o seu perfil de risco, horizonte de tempo e objetivo financeiro antes de contratar qualquer plano.
</p>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha wrapper
