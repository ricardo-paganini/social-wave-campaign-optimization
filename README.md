# 📣 Social Wave: Otimização de Campanhas de Marketing

## Sobre o projeto

A **Social Wave** é uma marca brasileira (fictícia) de roupas casuais que vende só pela internet e investe em 6 canais de mídia paga: Google Search, Google Display, Meta Ads, TikTok Ads, YouTube Ads e Pinterest Ads.

Em 2024 e 2025 a verba foi dividida quase igual entre os canais e o **CPA (custo por venda) subiu 10%**. Para 2026 o orçamento continua o mesmo, e a diretoria quer saber: **dá para vender mais com o mesmo dinheiro?**

Além disso, o time testou um criativo novo no Meta Ads (vídeo com cliente x foto do produto) e precisava saber se a diferença de vendas era real ou sorte.

O projeto segue a metodologia **CRISP-DM**: entendimento do negócio, descrição e limpeza dos dados, análise exploratória com SQL, curvas de saturação, otimização do orçamento e teste A/B.

## Perguntas de negócio

1. Quanto investimos e quanto retornou em cada canal (CPA e ROAS)?
2. Em que etapa do funil cada canal perde mais gente (CTR e taxa de conversão)?
3. Como investimento, conversões e CPA mudaram ao longo de 2024 e 2025?
4. A partir de que investimento cada canal começa a saturar?
5. Como redistribuir o mesmo orçamento para ter o máximo de vendas, e quanto o CPA cai com isso?
6. No teste A/B do Meta Ads, o criativo novo converte mais que o atual de verdade?

## Principais resultados

- **Mesmo orçamento, 9% mais vendas:** redistribuindo a verba (Meta +87%, Google Search +59%, YouTube e Display −50%, Pinterest −42%), as vendas estimadas sobem **9,0%** (cerca de **4.865 vendas a mais por ano**) e o CPA cai **8,2%** (de R\$ 38,81 para R\$ 35,61), sem gastar nenhum real a mais.
- **Os canais saturam em pontos diferentes:** no investimento atual, a próxima venda custa **R\$ 35 no Meta** e **R\$ 37 no Search**, contra **R\$ 117 no YouTube** e **R\$ 134 no Display**.
- **CPA por canal:** Google Search (R\$ 23,44) e Meta (R\$ 25,39) são os mais eficientes. YouTube (R\$ 72,41) e Display (R\$ 60,31) custam mais que o dobro por venda.
- **A alta do CPA em 2025 é saturação:** o investimento subiu 29,7% e as vendas só 17,5%. A correlação entre investimento do mês e CPA é de 0,83, com picos de R\$ 48 nas Black Fridays.
- **Teste A/B:** o vídeo com cliente converteu **2,57%** contra **2,19%** da foto (**+17,6%**), com p-valor de **0,013**. A diferença é real.

## Ferramentas

- **Python:** pandas, numpy, matplotlib, seaborn
- **SciPy:** `curve_fit` (curvas de saturação), `minimize` (otimização com restrição) e `chi2_contingency` (teste A/B)
- **SQL:** SQLite em memória
- **Jupyter Notebook**, **Git** e **GitHub**

## Como reproduzir

Pré-requisitos: Python 3 e Jupyter Notebook instalados.

```bash
git clone https://github.com/ricardo-paganini/social-wave-campaign-optimization.git
cd social-wave-campaign-optimization
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name=social-wave-venv --display-name="Python (social-wave)"
jupyter notebook
```

No Linux ou Mac, ative o ambiente com `source venv/bin/activate`.

Abra o `social_wave_campaign_optimization.ipynb`, escolha o kernel **Python (social-wave)** e rode **Kernel > Restart & Run All**.

Os arquivos `.csv` já estão no repositório. Para gerá-los de novo (o resultado é idêntico, porque a semente é fixa):

```bash
python generate_data.py
```

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `social_wave_campaign_optimization.ipynb` | Notebook com todo o estudo de caso |
| `generate_data.py` | Script que gera as bases fictícias (semente fixa) |
| `channels.csv` | Cadastro dos 6 canais de mídia |
| `campaigns.csv` | Cadastro das 12 campanhas (prospecção e remarketing de cada canal) |
| `daily_performance.csv` | Resultado diário de cada campanha em 2024 e 2025 (investimento, impressões, cliques, conversões e receita) |
| `ab_test.csv` | Resultado de cada pessoa no teste A/B do Meta Ads (grupo, clicou, comprou) |
| `requirements.txt` | Bibliotecas e versões usadas |

## Observação sobre os dados

Todos os dados são **fictícios** e foram gerados pelo script `generate_data.py` para este estudo de caso. As bases incluem de propósito problemas comuns em dados reais: linhas duplicadas, códigos escritos de jeitos diferentes, gastos negativos, colunas invertidas, valores vazios e dias faltando. Todos são tratados no notebook. Os números ilustram o método de análise e não representam um mercado real.
