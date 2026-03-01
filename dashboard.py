import pandas as pd
import streamlit as st
import sqlite3

# Configuração da página para ocupar a tela inteira (wide)
st.set_page_config(page_title="Dashboard Contabilizei", page_icon="", layout="wide")
st.title(" Dashboard de Concorrência")
st.write("Acompanhamento automático dos planos da Contabilizei")

try:
    conexao = sqlite3.connect('precos_contabilizei.db')

    # Lê os dados do banco
    df = pd.read_sql_query("SELECT * FROM precos", conexao) 
    conexao.close() 

    # Converte para numérico
    df['preco'] = pd.to_numeric(df['preco'], errors='coerce') 

    # --- CONCEITO 1: CARTÕES MÉTRICOS (Visão Executiva) ---
    st.markdown("---")
    st.subheader(" Visão Rápida dos Preços Atuais")
    
    # Verifica se o banco de dados não está vazio antes de tentar puxar os preços
    if not df.empty:
        # Pega o valor exato de cada plano
        preco_padrao = df[df['plano'] == 'Padrão']['preco'].values[0]
        preco_multi = df[df['plano'] == 'Multibenefícios']['preco'].values[0]
        preco_experts = df[df['plano'] == 'Experts Essencial']['preco'].values[0]

        # Divide a tela em 3 colunas para os cartões
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Plano Padrão", value=f"R$ {preco_padrao:.2f}")
        col2.metric(label="Multibenefícios", value=f"R$ {preco_multi:.2f}")
        col3.metric(label="Experts Essencial", value=f"R$ {preco_experts:.2f}")
    
    st.markdown("---")

    # --- TABELA DE DADOS ---
    st.subheader(" Base de Dados Coletados")
    st.dataframe(df, use_container_width=True)

    # --- GRÁFICOS ---
    st.subheader(" Comparação Atual de Preços")
    st.bar_chart(df, x='plano', y='preco', color='plano')

    st.subheader(" Evolução Histórica (Linha do Tempo)")
    st.line_chart(df, x='horario', y='preco', color='plano')

except Exception as e:
    st.error(f"Erro ao carregar dados do banco: {e}")