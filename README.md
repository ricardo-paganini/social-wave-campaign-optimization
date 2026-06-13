# 🌊 Social Wave — Otimização de Campanhas de Marketing Digital

[!\[Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[!\[Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[!\[Pandas](https://img.shields.io/badge/Pandas-2.0+-green)](https://pandas.pydata.org/)
[!\[Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-red)](https://matplotlib.org/)
[!\[SciPy](https://img.shields.io/badge/SciPy-1.11+-lightblue)](https://scipy.org/)
\[!\[Status](https://img.shields.io/badge/Status-Concluído-brightgreen)]()

\---

## 📖 Sobre o Projeto

Este projeto analisa dados de campanhas de marketing digital da **Social Wave** para responder a uma pergunta crítica de negócio:

> \*\*"Como aumentar o orçamento de marketing sem disparar o CPA (Custo Por Aquisição)?"\*\*

Em 2024, a empresa aumentou o orçamento em 20% dividindo igualmente entre canais — o resultado foi um **CPA global elevado**. Este projeto usa dados de Outubro-Dezembro de 2023 para construir um **modelo de otimização de alocação de orçamento** que minimiza o CPA global.

\---

## 🎯 Problema de Negócio

|Situação|Detalhe|
|-|-|
|**Empresa**|Social Wave (agência de marketing digital)|
|**Problema**|CPA disparou após aumento igualitário de verba|
|**Objetivo**|Aumentar investimento mantendo/reduzindo CPA global|
|**KPI Principal**|CPA (Gasto ÷ Conversões)|
|**Período dos Dados**|Outubro a Dezembro de 2023|
|**Canais**|Meta Ads, Google Search, YouTube Ads, Twitter Ads, TikTok, LinkedIn Ads|

\---

## 🏗️ Estrutura do Projeto

```
social-wave-campaign-optimization/
├── 📂 data/
│   ├── raw/                    # Dados originais (não versionar)
│   └── processed/              # Dados tratados (.pkl + .csv)
├── 📂 notebooks/
│   ├── notebook\_00\_contexto\_dicionario\_e\_tratamento.ipynb   # Contexto e validação
│   ├── notebook\_01\_analise\_exploratoria.ipynb    # Análise exploratória
│   ├── notebook\_02\_analise\_do\_cpa.ipynb            # Decomposição do CPA
│   ├── notebook\_03\_otimizacao\_de\_orcamento.ipynb     # Modelo de otimização
│   └── notebook\_04\_resumo\_executivo.ipynb       # Resumo executivo
├── 📂 reports/
│   ├── images/                # 12 visualizações geradas
│   └── \*.txt                   # Resumos de texto
├── 📄 requirements.txt         # Dependências
├── 📄 README.md                # Este arquivo
└── 📄 LICENSE                  # Licença MIT
```

\---

## 📊 Resultados Principais

### 🎯 Diagnóstico

|Canal|CPA|Status|
|-|-|-|
|**Meta Ads**|$\[3.88]|🏆 Mais eficiente|
|**Google Search**|$\[40.76]|✅ Eficiente|
|**YouTube Ads**|$\[27.22]|✅ Eficiente|
|**TikTok**|$\[15.35]|⚠️ Médio|
|**Twitter Ads**|$\[4.86]|⚠️ Médio|
|**LinkedIn Ads**|$\[47.47]|🔴 Menos eficiente|

**Problema identificado:** Desbalanceamento crítico entre share de gasto e share de conversões. Canais ineficientes consomem mais verba do que retornam.

### 📈 Recomendação

|Cenário|CPA Global|Conversões|
|-|-|-|
|**Atual**|$\[11.51]|\[5,711,699]|
|**Otimizado**|$\[6.65]|\[9,873,729]|
|**Ganho**|**\[42.2]% ↓**|**\[72.9]% ↑**|

**Alocação recomendada:** Reduzir verba em canais sobre-investidos, aumentar em canais sub-investidos, mantendo presença mínima de 5%.

\---

## 🛠️ Stack Tecnológico

|Ferramenta|Uso|
|-|-|
|**Python 3.14.5**|Linguagem principal|
|**Pandas**|Manipulação de dados|
|**NumPy**|Cálculos numéricos|
|**Matplotlib**|Visualizações estáticas|
|**Seaborn**|Estilização de gráficos|
|**SciPy**|Otimização não-linear (SLSQP)|
|**Jupyter Notebook**|Ambiente de desenvolvimento|
|**Git/GitHub**|Versionamento|

\---

## 🚀 Como Executar

### 1\. Clonar o repositório

```bash
git clone https://github.com/ricardo-paganini/social-wave-campaign-optimization.git
cd social-wave-campaign-optimization
```

### 2\. Criar ambiente virtual

```bash
# Windows
python -m venv .venv
.venv\\Scripts\\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3\. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4\. Executar notebooks

```bash
jupyter notebook
# Navegar até notebooks/ e executar em ordem (00 → 01 → 02 → 03 → 04)
```

\---

## 📓 Notebooks

|#|Arquivo|Conteúdo|Status|
|-|-|-|-|
|00|`notebook\_00\_contexto\_dicionario\_e\_tratamento.ipynb`|Contexto, dicionário, validação de dados|✅|
|01|`notebook\_01\_analise\_exploratoria.ipynb`|EDA: CPA, CTR, shares, correlações, 6 visualizações|✅|
|02|`notebook\_02\_analise\_do\_cpa.ipynb`|Decomposição do CPA em CPM/CTR/Conversão, sensibilidade|✅|
|03|`notebook\_03\_otimizacao\_de\_orcamento.ipynb`|Modelo de alocação ótima, trade-off, simulações|✅|
|04|`notebook\_04\_resumo\_executivo.ipynb`|Storytelling executivo, dashboard de KPIs|✅|

\---

## 📊 Visualizações Geradas

|#|Figura|Descrição|
|-|-|-|
|01|`01\_cpa\_por\_canal.png`|CPA por canal (barras horizontais)|
|02|`02\_share\_gasto\_vs\_conversao.png`|Desbalanceamento gasto vs. conversão|
|03|`03\_gasto\_vs\_cpa\_scatter.png`|Dispersão: gasto vs. CPA (retornos decrescentes)|
|04|`04\_evolucao\_cpa\_temporal.png`|Evolução do CPA ao longo do tempo|
|05|`05\_ctr\_vs\_taxa\_conversao.png`|CTR vs. Taxa de Conversão (funil)|
|06|`06\_matriz\_correlacao.png`|Heatmap de correlações|
|07|`07\_decomposicao\_cpa.png`|Decomposição do CPA em componentes|
|08|`08\_tornado\_sensibilidade.png`|Tornado chart: impacto de melhorias|
|09|`09\_alocacao\_atual\_vs\_otima.png`|Alocação atual vs. ótima|
|10|`10\_tradeoff\_custo\_volume.png`|Trade-off: custo vs. volume|
|11|`11\_simulacao\_aumento\_20pct.png`|Simulação de +20% orçamento|
|12|`12\_dashboard\_executivo.png`|Dashboard executivo (4 KPIs)|

\---

## 🎯 Metodologia

### Fórmula do CPA

```
CPA = (CPM × 10) / (CTR × Taxa de Conversão)
```

Onde:

* **CPM** = Custo por Mil Impressões ($)
* **CTR** = Click-Through Rate (%)
* **Taxa de Conversão** = Conversões / Cliques (%)

### Modelo de Otimização

```
Minimizar: CPA\_global = Σ(Gasto\_i) / Σ(Conversões\_i)
Sujeito a:
  - Σ(Share\_i) = 100%
  - 5% ≤ Share\_i ≤ 50% (presença mínima, não concentrar)
  - CPA\_i = CPA\_base\_i × (1 + 0.3 × ln(Share\_i / Share\_base\_i))
```

Método: **SLSQP** (Sequential Least Squares Programming) via SciPy.

\---

## 📚 Aprendizados

|Aprendizado|Aplicação|
|-|-|
|**Retornos decrescentes**|Aumentar gasto em canal saturado eleva CPA|
|**Decomposição de KPIs**|CPA = f(CPM, CTR, Conversão) — identificar qual componente falha|
|**Otimização com restrições**|Presença mínima de 5% em cada canal|
|**Storytelling com dados**|Narrativa: problema → diagnóstico → análise → recomendação|

\---

## 🤝 Contribuição

Este projeto foi desenvolvido como case de portfolio. Sugestões e melhorias são bem-vindas!

\---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

\---

## 👤 Autor

**Ricardo Paganini**  
Data Analyst | Marketing Analytics  
[LinkedIn](https://www.linkedin.com/in/ricardo-paganini/) | [GitHub](https://github.com/ricardo-paganini) | [Medium](https://medium.com/@ricardo.paganini)

\---

> \*"Dados ruins = insights ruins. Dados bem tratados = decisões certeiras."\*

