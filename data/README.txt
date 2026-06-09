ARQUIVO: campanhas_limpo.pkl
FORMATO: Pickle (Python native)
ORIGEM: CampanhasAds - Arquivo Oficial.xlsx
DATA: 2026-06-09 20:12
PROCESSADO: Notebook 00_contexto_e_dicionario.ipynb

TRATAMENTOS:
  • Removido 1 registro (Cliques > Impressoes, 0.05% da base)
  • Timestamp -> datetime64[ns]
  • Metricas: CTR, Taxa_Conversao, CPC, CPA, CPM, Taxa_Impressao
  • Temporais: Data(date), Ano_Mes(Period[M]), Semana(int), Dia_Semana(str)
  • Flag: Conversao_Zero(bool)

DIMENSOES: 23,315 registros × 9 colunas
PERIODO: 2023-10-01 11:00:00 a 2023-12-24 23:00:00
CANAIS: 6

USO:
  df = pd.read_pickle("../data/processed/campanhas_limpo.pkl")

  # Todos os tipos são preservados automaticamente:
  # - Ano_Mes continua como Period (operações temporais funcionam)
  # - Data continua como date
  # - timestamp como datetime64[ns]
  # - Conversao_Zero como bool

ATENCAO: Pickle é específico do Python. Para compartilhar com 
         outras ferramentas (Power BI, Excel), exportar CSV 
         separadamente quando necessário.
