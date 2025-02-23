import pandas as pd
import yfinance as yf

def obter_dados_brent():
    brent = yf.download('BZ=F', start="2007-01-01", end="2025-02-10")
    # Remover a linha de títulos extra, se necessário
    brent.columns = ['Close', 'High', 'Low', 'Open', 'Volume']  # Definindo as colunas corretamente
    return brent

df_brent = obter_dados_brent()

# Verificar as primeiras linhas para garantir que as colunas estão corretas
print(df_brent.head())