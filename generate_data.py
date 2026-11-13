"""
Gera as bases fictícias do projeto Social Wave: Otimização de Campanhas de Marketing.

Arquivos gerados (na mesma pasta do script):
- channels.csv: cadastro dos 6 canais de mídia
- campaigns.csv: cadastro das 12 campanhas (2 por canal)
- daily_performance.csv: resultado diário de cada campanha em 2024 e 2025
- ab_test.csv: resultado de cada pessoa no teste A/B do Meta Ads (novembro de 2025)

A semente é fixa, então qualquer pessoa que rodar o script gera exatamente os mesmos dados.
"""

import random

import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

# ---------------------------------------------------------------
# 1. Canais
# Cada canal tem uma curva de saturação: conversões por dia = a * (1 - exp(-investimento / b)).
# 'a' é o teto de vendas por dia e 'b' diz quão rápido o canal chega perto do teto.
# ---------------------------------------------------------------
channels = pd.DataFrame({
    'channel_id': ['CH01', 'CH02', 'CH03', 'CH04', 'CH05', 'CH06'],
    'channel_name': ['Google Search', 'Google Display', 'Meta Ads', 'TikTok Ads', 'YouTube Ads', 'Pinterest Ads'],
    'channel_type': ['Busca', 'Display', 'Rede social', 'Rede social', 'Vídeo', 'Rede social'],
})

params = {
    'CH01': {'a': 60, 'b': 900, 'cpm': 40, 'ctr': 0.040, 'ticket': 210},
    'CH02': {'a': 20, 'b': 600, 'cpm': 8, 'ctr': 0.004, 'ticket': 170},
    'CH03': {'a': 80, 'b': 1500, 'cpm': 20, 'ctr': 0.012, 'ticket': 180},
    'CH04': {'a': 55, 'b': 1600, 'cpm': 12, 'ctr': 0.009, 'ticket': 140},
    'CH05': {'a': 25, 'b': 1200, 'cpm': 15, 'ctr': 0.005, 'ticket': 190},
    'CH06': {'a': 30, 'b': 1000, 'cpm': 14, 'ctr': 0.008, 'ticket': 200},
}

# ---------------------------------------------------------------
# 2. Campanhas: uma de prospecção (gente nova) e uma de remarketing (quem já visitou o site)
# ---------------------------------------------------------------
campaign_rows = []
number = 1
for _, channel in channels.iterrows():
    for campaign_type in ['Prospecção', 'Remarketing']:
        campaign_rows.append({
            'campaign_id': f'CP{number:02d}',
            'channel_id': channel['channel_id'],
            'campaign_name': f"{channel['channel_name']} - {campaign_type}",
            'campaign_type': campaign_type,
            'start_date': '2024-01-01',
        })
        number += 1
campaigns = pd.DataFrame(campaign_rows)

# ---------------------------------------------------------------
# 3. Desempenho diário
# A verba diária de cada canal parte de uma base (maior em 2025), muda de mês a mês
# ("no feeling") e sobe na Black Friday e no Natal.
# ---------------------------------------------------------------
dates = pd.date_range('2024-01-01', '2025-12-31', freq='D')
months = sorted(set(dates.to_period('M')))

spend_month_factor = {
    (channel_id, month): np.random.uniform(0.4, 1.8)
    for channel_id in channels['channel_id'] for month in months
}
season_spend = {11: 1.5, 12: 1.2}

perf_rows = []
for date in dates:
    base_spend = 650 if date.year == 2024 else 850
    month = date.to_period('M')
    for channel_id in channels['channel_id']:
        p = params[channel_id]
        spend = (base_spend * spend_month_factor[(channel_id, month)]
                 * season_spend.get(date.month, 1) * np.random.uniform(0.9, 1.1))
        expected_conv = p['a'] * (1 - np.exp(-spend / p['b']))
        conversions = np.random.poisson(expected_conv)

        # Divide o canal entre prospecção (70% da verba) e remarketing (30%).
        # O remarketing converte melhor, então leva uma fatia maior das vendas.
        share_spend = np.clip(np.random.normal(0.70, 0.03), 0.6, 0.8)
        share_conv = share_spend * 1.0 / (share_spend * 1.0 + (1 - share_spend) * 1.6)
        conv_split = np.random.binomial(conversions, share_conv)

        channel_campaigns = campaigns[campaigns['channel_id'] == channel_id]['campaign_id'].tolist()
        for campaign_id, s, conv in zip(channel_campaigns,
                                        [share_spend, 1 - share_spend],
                                        [conv_split, conversions - conv_split]):
            camp_spend = spend * s
            impressions = int(camp_spend / p['cpm'] * 1000 * np.random.uniform(0.85, 1.15))
            clicks = int(np.random.binomial(impressions, p['ctr']))
            conv = min(conv, clicks)
            revenue = sum(np.random.normal(p['ticket'], 35, conv)) if conv > 0 else 0
            perf_rows.append({
                'date': date.strftime('%Y-%m-%d'),
                'campaign_id': campaign_id,
                'spend': round(camp_spend, 2),
                'impressions': impressions,
                'clicks': clicks,
                'conversions': float(conv),
                'revenue': round(max(revenue, 0), 2),
            })

performance = pd.DataFrame(perf_rows)

# ---------------------------------------------------------------
# 4. Problemas reais nos dados
# ---------------------------------------------------------------
# 4.1 Exportação do TikTok falhou de 10 a 16 de junho de 2025 (os dias somem)
tiktok_ids = campaigns[campaigns['channel_id'] == 'CH04']['campaign_id'].tolist()
gap = (performance['campaign_id'].isin(tiktok_ids)
       & performance['date'].between('2025-06-10', '2025-06-16'))
performance = performance[~gap].reset_index(drop=True)

# 4.2 Algumas linhas soltas que não vieram na exportação
performance = performance.drop(performance.sample(40, random_state=42).index).reset_index(drop=True)

# 4.3 Gasto negativo (estornos lançados como linha de gasto)
idx = performance.sample(35, random_state=1).index
performance.loc[idx, 'spend'] = -performance.loc[idx, 'spend']

# 4.4 Impressões e cliques trocados de coluna (cliques maiores que impressões)
idx = performance.sample(25, random_state=2).index
performance.loc[idx, ['impressions', 'clicks']] = performance.loc[idx, ['clicks', 'impressions']].values

# 4.5 Conversões vazias
idx = performance.sample(60, random_state=3).index
performance.loc[idx, 'conversions'] = np.nan

# 4.6 Código da campanha escrito de jeitos diferentes
idx = performance.sample(450, random_state=4).index
variants = [lambda c: c.lower(), lambda c: c.replace('CP', 'CP-'), lambda c: f' {c} ']
performance.loc[idx, 'campaign_id'] = [random.choice(variants)(c) for c in performance.loc[idx, 'campaign_id']]

# 4.7 Linhas duplicadas (exportação rodou duas vezes em alguns dias)
duplicates = performance.sample(150, random_state=5)
performance = pd.concat([performance, duplicates]).sort_values(['date', 'campaign_id']).reset_index(drop=True)

# ---------------------------------------------------------------
# 5. Teste A/B no Meta Ads (3 a 30 de novembro de 2025)
# A: foto do produto (controle) | B: vídeo com cliente (teste)
# ---------------------------------------------------------------
n_users = 40000
test_days = pd.date_range('2025-11-03', '2025-11-30', freq='D')
groups = np.random.choice(['A', 'B'], n_users)
click_rate = np.where(groups == 'A', 0.110, 0.118)
buy_given_click = np.where(groups == 'A', 0.185, 0.205)
clicked = np.random.binomial(1, click_rate)
converted = clicked * np.random.binomial(1, buy_given_click)

ab_test = pd.DataFrame({
    'user_id': [f'U{n:05d}' for n in range(1, n_users + 1)],
    'group': groups,
    'exposure_date': np.random.choice(test_days, n_users),
    'clicked': clicked,
    'converted': converted,
})
ab_test['exposure_date'] = pd.to_datetime(ab_test['exposure_date']).dt.strftime('%Y-%m-%d')

# Problemas: pessoas que caíram nos dois grupos e linhas duplicadas
both = ab_test.sample(120, random_state=6).copy()
both['group'] = np.where(both['group'] == 'A', 'B', 'A')
ab_dup = ab_test.sample(80, random_state=7)
ab_test = pd.concat([ab_test, both, ab_dup]).sample(frac=1, random_state=8).reset_index(drop=True)

# ---------------------------------------------------------------
# 6. Salvando
# ---------------------------------------------------------------
channels.to_csv('channels.csv', index=False)
campaigns.to_csv('campaigns.csv', index=False)
performance.to_csv('daily_performance.csv', index=False)
ab_test.to_csv('ab_test.csv', index=False)

print('Bases geradas:')
print(f'channels.csv: {len(channels)} linhas')
print(f'campaigns.csv: {len(campaigns)} linhas')
print(f'daily_performance.csv: {len(performance)} linhas')
print(f'ab_test.csv: {len(ab_test)} linhas')
