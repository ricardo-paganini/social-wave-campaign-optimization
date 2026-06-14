ARQUIVO: campanhas_base_processada.pkl
FORMATO: Pickle (Python native)
ORIGEM: CampanhasAds - Arquivo Oficial.xlsx
DATA: 2026-06-14 14:09
PROCESSADO: notebook_00_contexto_dicionario_e_tratamento.ipynb

TRATAMENTOS:
  • Removido 1 registro (Cliques > Impressoes, 0.05% da base)
  • Timestamp -> datetime64[ns]

DIMENSOES: 23,315 registros × 9 colunas
PERIODO: 2023-10-01 11:00:00 a 2023-12-24 23:00:00
CANAIS: 6

USO:
  df = pd.read_pickle(r'../../data/processed/campanhas_base_processada.pkl').resolve()

ATENCAO: Pickle é específico do Python. Para compartilhar com 
         outras ferramentas (Power BI, Excel), exportar CSV 
         separadamente quando necessário.
