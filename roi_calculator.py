import streamlit as st
from textwrap import dedent
import streamlit.components.v1 as components

def render_roi_calculator():
    """
    Renderiza a calculadora de ROI + Payback em HTML dentro do Streamlit.
    Usa os valores MENSAIS dos planos (modelo 1: mensal = +25% sobre o anual).
    Ajuste os preços conforme necessário.
    """

    calc_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
      :root {
        --bg: #050608;
        --card-bg: rgba(5,6,8,0.95);
        --neon: #00ff9a;
        --accent: #ff7a1a;
        --text: #f2f2f2;
      }

      body {
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        color: var(--text);
      }

      .calc-wrapper {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 8px;
      }

      .calc-title {
        text-align: center;
        color: var(--neon);
        font-size: 1.6rem;
        margin-bottom: 0.3rem;
        font-weight: 700;
      }

      .calc-subtitle {
        text-align: center;
        color: #d7d7d7;
        font-size: 0.9rem;
        margin-bottom: 1.2rem;
      }

      .calc-card {
        background: var(--card-bg);
        border-radius: 18px;
        border: 1px solid rgba(0,255,154,0.35);
        box-shadow: 0 0 18px rgba(0,255,154,0.28);
        padding: 16px 18px 18px 18px;
      }

      .calc-label {
        font-size: 0.85rem;
        color: #d7d7d7;
        margin-bottom: 0.25rem;
        display: block;
      }

      .calc-input,
      .calc-select {
        width: 100%;
        background: #11131a;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.12);
        padding: 0.55rem 0.9rem;
        color: var(--text);
        font-size: 0.95rem;
        outline: none;
        box-sizing: border-box;
        margin-bottom: 0.65rem;
      }

      .calc-input:focus,
      .calc-select:focus {
        border-color: var(--neon);
        box-shadow: 0 0 6px rgba(0,255,154,0.45);
      }

      .main-number {
        text-align: center;
        margin-bottom: 0.85rem;
      }

      .main-number-title {
        font-size: 0.85rem;
        color: #d7d7d7;
      }

      .main-number-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--neon);
      }

      .bar-wrapper {
        margin-bottom: 0.9rem;
      }

      .bar-label {
        font-size: 0.8rem;
        color: #d7d7d7;
        margin-bottom: 0.25rem;
      }

      .bar-bg {
        width: 100%;
        height: 12px;
        border-radius: 999px;
        background: #14171f;
        overflow: hidden;
        position: relative;
      }

      .bar-fill-conservador {
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        background: linear-gradient(90deg, #ff7a1a, #ffb347);
        border-radius: 999px;
      }

      .bar-fill-estrategia {
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        background: linear-gradient(90deg, #00ff9a, #00ffd5);
        border-radius: 999px;
        opacity: 0.7;
      }

      .result-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.86rem;
        margin-bottom: 0.25rem;
      }

      .result-row span:first-child {
        color: #d7d7d7;
      }

      .result-row span:last-child {
        font-weight: 600;
      }

      .result-row.plano span:last-child {
        color: #ffffff;
      }

      .result-row.estrategia span:last-child {
        color: var(--neon);
      }

      .result-row.payback span:last-child {
        color: #ffb446;
        text-shadow: 0 0 6px rgba(255, 180, 70, 0.55);
      }

      .calc-footnote {
        font-size: 0.75rem;
        color: #888;
        margin-top: 0.8rem;
        text-align: center;
      }

      .calc-grid {
        display: grid;
        grid-template-columns: 1.1fr 1.2fr;
        gap: 18px;
      }

      @media (max-width: 760px) {
        .calc-grid {
          grid-template-columns: 1fr;
        }
        .calc-card {
          padding: 14px 12px 16px 12px;
        }
        .calc-title {
          font-size: 1.35rem;
        }
      }
    </style>
    </head>
    <body>
      <div class="calc-wrapper">
        <h3 class="calc-title">Simule seu ROI com o Phoenix Strategy</h3>
        <p class="calc-subtitle">
          Ajuste o capital, o plano e o horizonte de tempo para visualizar, de forma educacional,
          o potencial de retorno e o tempo estimado de payback da assinatura.
          Os valores consideram o <strong>plano mensal</strong>; planos mais longos reduzem ainda mais o custo mensal.
        </p>

        <div class="calc-grid">
          <div>
            <div class="calc-card">
              <label class="calc-label" for="capital-input">
                Capital que você pretende operar (R$)
              </label>
              <input id="capital-input" class="calc-input" type="number" min="1000" step="500" value="10000">

              <label class="calc-label" for="plano-select">
                Plano / Perfil de Estratégia
              </label>
              <select id="plano-select" class="calc-select">
                <option value="equity">Phoenix Equity (Ações)</option>
                <option value="full">Phoenix Full (Ações + Opções)</option>
                <option value="scanner">Phoenix Scanner PRO</option>
              </select>

              <label class="calc-label" for="horizonte-select">
                Horizonte de simulação
              </label>
              <select id="horizonte-select" class="calc-select">
                <option value="1">1 mês</option>
                <option value="3">3 meses</option>
                <option value="6">6 meses</option>
                <option value="12">12 meses</option>
              </select>
            </div>
          </div>

          <div>
            <div class="calc-card">
              <div class="main-number">
                <div class="main-number-title">ROI estimado (Premissas da Estratégia)</div>
                <div id="main-number-value" class="main-number-value">R$ 0,00</div>
              </div>

              <div class="bar-wrapper">
                <div class="bar-label">Comparação entre cenário conservador e estratégia</div>
                <div class="bar-bg">
                  <div id="bar-conservador" class="bar-fill-conservador" style="width: 30%;"></div>
                  <div id="bar-estrategia" class="bar-fill-estrategia" style="width: 60%;"></div>
                </div>
              </div>

              <div class="result-row plano">
                <span>Valor da assinatura (plano mensal)</span>
                <span id="valor-plano">R$ 0,00</span>
              </div>
              <div class="result-row estrategia">
                <span>Total estimado da estratégia no período</span>
                <span id="valor-estrategia">R$ 0,00</span>
              </div>
              <div class="result-row payback">
                <span>Payback estimado da assinatura</span>
                <span id="valor-payback">–</span>
              </div>

              <div class="calc-footnote">
                Os valores são <strong>simulações educacionais</strong> baseadas em premissas conservadoras e na filosofia
                da estratégia. Não constituem promessa ou garantia de rentabilidade futura.
              </div>
            </div>
          </div>
        </div>
      </div>

    <script>
      const planos = {
        "equity":  { preco: 309,  pCons: 0.04,  pEst: 0.06  },  // Phoenix Equity
        "full":    { preco: 496,  pCons: 0.08,  pEst: 0.155 },  // Phoenix Full
        "scanner": { preco: 746,  pCons: 0.00,  pEst: 0.00  }   // Scanner PRO (sem ROI de trade, foco em ferramenta)
      };

      function formatCurrency(v) {
        if (!isFinite(v)) return "R$ 0,00";
        return v.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
      }

      function formatDays(d) {
        if (!isFinite(d) || d <= 0) return "–";
        const dias = Math.round(d);
        if (dias < 30) return dias + " dias";
        const meses = dias / 30;
        if (meses < 12) {
          return meses.toFixed(1).replace(".", ",") + " meses";
        }
        const anos = meses / 12;
        return anos.toFixed(1).replace(".", ",") + " anos";
      }

      function updateCalc() {
        const capitalInput = document.getElementById("capital-input");
        const planoSelect = document.getElementById("plano-select");
        const horizonteSelect = document.getElementById("horizonte-select");

        let capital = parseFloat(capitalInput.value);
        if (!isFinite(capital) || capital <= 0) capital = 0;

        const plano = planos[planoSelect.value];
        const meses = parseInt(horizonteSelect.value);

        const lucroMensalCons = capital * plano.pCons;
        const lucroMensalEst  = capital * plano.pEst;

        const totalEst  = lucroMensalEst * meses;

        document.getElementById("valor-plano").textContent = formatCurrency(plano.preco);
        document.getElementById("valor-estrategia").textContent  = formatCurrency(totalEst);
        document.getElementById("main-number-value").textContent = formatCurrency(totalEst);

        if (lucroMensalEst > 0) {
          const paybackMeses = plano.preco / lucroMensalEst;
          const paybackDias  = paybackMeses * 30.0;
          document.getElementById("valor-payback").textContent = formatDays(paybackDias);
        } else {
          document.getElementById("valor-payback").textContent = "–";
        }

        // barras – proporção entre conservador (aqui simplificado) e estratégia
        let ratio = 0.3;
        if (totalEst > 0 && lucroMensalCons > 0) {
          const totalCons = lucroMensalCons * meses;
          ratio = Math.min(1.0, totalCons / totalEst);
        }
        const widthEst = 100;
        const widthCons = Math.max(8, Math.round(widthEst * ratio));

        document.getElementById("bar-estrategia").style.width  = widthEst + "%";
        document.getElementById("bar-conservador").style.width = widthCons + "%";
      }

      document.getElementById("capital-input").addEventListener("input", updateCalc);
      document.getElementById("plano-select").addEventListener("change", updateCalc);
      document.getElementById("horizonte-select").addEventListener("change", updateCalc);

      updateCalc();
    </script>
    </body>
    </html>
    """

    components.html(calc_html, height=800, scrolling=False)

    st.markdown(dedent("""
        <p style='color:#888; font-size:0.8rem; text-align:center; margin-top:0.6rem;'>
            A simulação usa o valor do <strong>plano mensal</strong> apenas como referência de custo.
            Planos trimestrais e anuais possuem desconto progressivo, reduzindo ainda mais o payback.
        </p>
    """), unsafe_allow_html=True)
