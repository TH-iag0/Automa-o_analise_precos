import pandas as pd
import streamlit as st
import sqlite3

# Configuração da página para ocupar a tela inteira (wide)
st.set_page_config(page_title="Dashboard Contabilizei", page_icon="", layout="wide")

# --- BARRA LATERAL (SIDEBAR) ---
# Tudo que for "st.sidebar" vai ficar no menu lateral esquerdo (igual ao azul da sua imagem)
with st.sidebar:
    st.title(" Painel de Controle")
    st.markdown("Bem-vindo ao sistema de monitoramento.")
    st.markdown("---")
    st.markdown("**Status do Robô:** 🟢 Online")
    st.markdown("**Última atualização:** Hoje")
    st.markdown("---")
    st.markdown("*Desenvolvido por Thiago Vaz*")

# --- ÁREA PRINCIPAL ---
st.title(" Dashboard de Concorrência")
st.markdown("Acompanhamento automático dos planos da Contabilizei")

try:
    conexao = sqlite3.connect('precos_contabilizei.db')
    df = pd.read_sql_query("SELECT * FROM precos", conexao) 
    conexao.close() 

    df['preco'] = pd.to_numeric(df['preco'], errors='coerce') 

    if not df.empty:
        
        # --- LINHA 1: CARTÕES MÉTRICOS LADO A LADO ---
        # Igual à parte superior da sua imagem de referência
        st.subheader(" Visão Rápida dos Preços Atuais")
        
        preco_padrao = df[df['plano'] == 'Padrão']['preco'].values[0]
        preco_multi = df[df['plano'] == 'Multibenefícios']['preco'].values[0]
        preco_experts = df[df['plano'] == 'Experts Essencial']['preco'].values[0]

        # 3 colunas para os 3 cartões menores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.metric(label="Plano Padrão", value=f"R$ {preco_padrao:.2f}")
        with col2:
            with st.container(border=True):
                st.metric(label="Multibenefícios", value=f"R$ {preco_multi:.2f}")
        with col3:
            with st.container(border=True):
                st.metric(label="Experts Essencial", value=f"R$ {preco_experts:.2f}")

        st.markdown("<br>", unsafe_allow_html=True) # Dá um pequeno espaço visual

        # --- LINHA 2: GRÁFICOS GRANDES LADO A LADO ---
        # Cria duas colunas grandes para os gráficos
        grafico_esq, grafico_dir = st.columns(2)
        
        with grafico_esq:
            with st.container(border=True):
                st.subheader(" Comparação Atual")
                st.bar_chart(df, x='plano', y='preco', color='plano')

        with grafico_dir:
            with st.container(border=True):
                st.subheader(" Evolução Histórica")
                st.line_chart(df, x='horario', y='preco', color='plano')

        st.markdown("<br>", unsafe_allow_html=True)

        # --- LINHA 3: TABELA LARGONA EMBAIXO ---
        with st.container(border=True):
            st.subheader(" Base de Dados Coletados")
            st.dataframe(df, use_container_width=True)
            
    else:
        st.warning("O banco de dados está aguardando os primeiros dados.")

except Exception as e:
    st.error(f"Erro ao carregar dados do banco: {e}")