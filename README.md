# 🌊 Social Wave — Otimização de Campanhas de Marketing Digital

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-red)](https://matplotlib.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.11+-lightblue)](https://scipy.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)]()

---

## 📖 Sobre o Projeto

Este projeto analisa dados de campanhas de marketing digital da **Social Wave** para responder a uma pergunta crítica de negócio:

> **"Como aumentar o orçamento de marketing sem disparar o CPA (Custo Por Aquisição)?"**

Em 2024, a empresa aumentou o orçamento em 20% dividindo igualmente entre canais — o resultado foi um **CPA global elevado**. Este projeto usa dados de Outubro-Dezembro de 2023 para construir um **modelo de otimização de alocação de orçamento** que minimiza o CPA global.

---

## 🎯 Problema de Negócio

| Situação | Detalhe |
|----------|---------|
| **Empresa** | Social Wave (agência de marketing digital) |
| **Problema** | CPA disparou após aumento igualitário de verba |
| **Objetivo** | Aumentar investimento mantendo/reduzindo CPA global |
| **KPI Principal** | CPA (Gasto ÷ Conversões) |
| **Período dos Dados** | Outubro a Dezembro de 2023 |
| **Canais** | Meta Ads, Google Search, YouTube Ads, Twitter Ads, TikTok, LinkedIn Ads |

---

## 🏗️ Estrutura do Projeto

```
social-wave-campaign-optimization/
├── 📂 data/
│   ├── raw/                    # Dados originais (não versionar)
│   └── processed/              # Dados tratados (.pkl + .csv)
├── 📂 notebooks/
│   ├── 00_contexto_e_dicionario.ipynb   # Contexto e validação
│   ├── 01_exploratory_analysis.ipynb    # Análise exploratória
│   ├── 02_cpa_analysis.ipynb            # Decomposição do CPA
│   ├── 03_budget_optimization.ipynb     # Modelo de otimização
│   └── 04_executive_summary.ipynb       # Resumo executivo
├── 📂 reports/
│   ├── figures/                # 12 visualizações geradas
│   └── *.txt                   # Resumos de texto
├── 📂 src/                     # Scripts reutilizáveis
├── 📂 docs/                    # Documentação
├── 📄 requirements.txt         # Dependências
├── 📄 README.md                # Este arquivo
└── 📄 LICENSE                  # Licença MIT
```

---

## 📊 Resultados Principais

### 🎯 Diagnóstico

| Canal | CPA | Status |
|-------|-----|--------|
| **Meta Ads** | $[valor] | 🏆 Mais eficiente |
| **Google Search** | $[valor] | ✅ Eficiente |
| **YouTube Ads** | $[valor] | ✅ Eficiente |
| **TikTok** | $[valor] | ⚠️ Médio |
| **Twitter Ads** | $[valor] | ⚠️ Médio |
| **LinkedIn Ads** | $[valor] | 🔴 Menos eficiente |

**Problema identificado:** Desbalanceamento crítico entre share de gasto e share de conversões. Canais ineficientes consomem mais verba do que retornam.

### 📈 Recomendação

| Cenário | CPA Global | Conversões |
|---------|-----------|------------|
| **Atual** | $[valor] | [valor] |
| **Otimizado** | $[valor] | [valor] |
| **Ganho** | **[x]% ↓** | **[x]% ↑** |

**Alocação recomendada:** Reduzir verba em canais sobre-investidos, aumentar em canais sub-investidos, mantendo presença mínima de 5%.

---

## 🛠️ Stack Tecnológico

| Ferramenta | Uso |
|------------|-----|
| **Python 3.11** | Linguagem principal |
| **Pandas** | Manipulação de dados |
| **NumPy** | Cálculos numéricos |
| **Matplotlib** | Visualizações estáticas |
| **Seaborn** | Estilização de gráficos |
| **SciPy** | Otimização não-linear (SLSQP) |
| **Jupyter Notebook** | Ambiente de desenvolvimento |
| **Git/GitHub** | Versionamento |

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/ricardo-paganini/social-wave-campaign-optimization.git
cd social-wave-campaign-optimization
```

### 2. Criar ambiente virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar notebooks

```bash
jupyter notebook
# Navegar até notebooks/ e executar em ordem (00 → 01 → 02 → 03 → 04)
```

---

## 📓 Notebooks

| # | Arquivo | Conteúdo | Status |
|---|---------|----------|--------|
| 00 | `00_contexto_e_dicionario.ipynb` | Contexto, dicionário, validação de dados | ✅ |
| 01 | `01_exploratory_analysis.ipynb` | EDA: CPA, CTR, shares, correlações, 6 visualizações | ✅ |
| 02 | `02_cpa_analysis.ipynb` | Decomposição do CPA em CPM/CTR/Conversão, sensibilidade | ✅ |
| 03 | `03_budget_optimization.ipynb` | Modelo de alocação ótima, trade-off, simulações | ✅ |
| 04 | `04_executive_summary.ipynb` | Storytelling executivo, dashboard de KPIs | ✅ |

---

## 📊 Visualizações Geradas

| # | Figura | Descrição |
|---|--------|-----------|
| 01 | `01_cpa_por_canal.png` | CPA por canal (barras horizontais) |
| 02 | `02_share_gasto_vs_conversao.png` | Desbalanceamento gasto vs. conversão |
| 03 | `03_gasto_vs_cpa_scatter.png` | Dispersão: gasto vs. CPA (retornos decrescentes) |
| 04 | `04_evolucao_cpa_temporal.png` | Evolução do CPA ao longo do tempo |
| 05 | `05_ctr_vs_taxa_conversao.png` | CTR vs. Taxa de Conversão (funil) |
| 06 | `06_matriz_correlacao.png` | Heatmap de correlações |
| 07 | `07_decomposicao_cpa.png` | Decomposição do CPA em componentes |
| 08 | `08_tornado_sensibilidade.png` | Tornado chart: impacto de melhorias |
| 09 | `09_alocacao_atual_vs_otima.png` | Alocação atual vs. ótima |
| 10 | `10_tradeoff_custo_volume.png` | Trade-off: custo vs. volume |
| 11 | `11_simulacao_aumento_20pct.png` | Simulação de +20% orçamento |
| 12 | `12_dashboard_executivo.png` | Dashboard executivo (4 KPIs) |

---

## 🎯 Metodologia

### Fórmula do CPA

```
CPA = (CPM × 10) / (CTR × Taxa de Conversão)
```

Onde:
- **CPM** = Custo por Mil Impressões ($)
- **CTR** = Click-Through Rate (%)
- **Taxa de Conversão** = Conversões / Cliques (%)

### Modelo de Otimização

```
Minimizar: CPA_global = Σ(Gasto_i) / Σ(Conversões_i)
Sujeito a:
  - Σ(Share_i) = 100%
  - 5% ≤ Share_i ≤ 50% (presença mínima, não concentrar)
  - CPA_i = CPA_base_i × (1 + 0.3 × ln(Share_i / Share_base_i))
```

Método: **SLSQP** (Sequential Least Squares Programming) via SciPy.

---

## 📚 Aprendizados

| Aprendizado | Aplicação |
|-------------|-----------|
| **Retornos decrescentes** | Aumentar gasto em canal saturado eleva CPA |
| **Decomposição de KPIs** | CPA = f(CPM, CTR, Conversão) — identificar qual componente falha |
| **Otimização com restrições** | Presença mínima de 5% em cada canal |
| **Storytelling com dados** | Narrativa: problema → diagnóstico → análise → recomendação |

---

## 🤝 Contribuição

Este projeto foi desenvolvido como case de portfolio. Sugestões e melhorias são bem-vindas!

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👤 Autor

**Ricardo Paganini**  
Data Analyst | Marketing Analytics  
[LinkedIn](https://www.linkedin.com/in/ricardo-paganini/) | [GitHub](https://github.com/ricardo-paganini) | [Medium](https://medium.com/@ricardo.paganini)

---

> *"Dados ruins = insights ruins. Dados bem tratados = decisões certeiras."*
