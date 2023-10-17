from operator import contains
from typing import Container
import streamlit as st
import plotly.express as px 

class VisualizacaoSupermercado:
    def exibir_pagina(self, df_filtrado, total_do_mes, margem_de_lucro_bruta,calcular_total_cogs):
        col1, col2 = st.columns(2)
        col3 = st.columns(1)[0]
        col4, col5, col6 = st.columns(3)
        col7 = st.columns(1)[0]
        col8 = st.columns(1)[0]
        col9, col10 = st.columns(2)

    fig_data = px.bar(df_filtrado, x="Date", y="Total", color = "City", title="Faturamento por dia")
    fig_data.update_xaxes(title="Data")
    col1.plotly_chart(fig_data, use_container_width=True)

    fig_produto = px.bar(df_filtrado, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientarion="h")
    fig_produto = update_xaxes(title="Date")
    fig_produto = update_yaxes(title="Linha do produto")
    col2.plotly_chart(fig_produto, use_container_widht=True)

    fig_crescimento = px.line(df_filtrado, x='Total', y='cogs', color="Branch", symbol='Branch', title="custo dos bens vendidos")
    fig_crescimento.update_xaxes(title='Total')
    fig_crescimento.update_yaxes(title='custo dos bens vendidos')
    col3.plotly_chart(fig_crescimento, use_container_width=True)

    cidade_total = df_filtrado.groupby("City")[["Total"]].sum().reset_index()
    fig_cidade = px.bar(cidade_total, x="City", y="Total", title="Faturamento por filial")
    fig_cidade.update_xaxes(title="Cidade")
    col4.plotly_chart(fig_cidade, use_container_width=True)

    fig_tipo = px.pie(df_filtrado, x="Mes", y="gross income", color="City", title="Margem de Lucro Bruta por Mes")
    fig_margem_bruta.update_yaxes(title="Renda Bruta")
    col6.plotly_chart(fig_margem_bruta, use_container_width=True)

    st.write("Dados Analisados:")
    st.write(df.filtrado)

    st.write(f'Total do Mês: ${total_do_mes:,.2f}')

    st.write(f'Total CoG: ${calcular_total_cogs:,.2f}')

    st.write(f"Margem de Lucro Bruts Média (%) = [(Total do Mês - Total do custo das mercadorias vendidas) / Total do Mês] * 100\n\nMargem de Lucro Bruta Média:{margem_de_lucro_bruta:,.2f}%")

    fig_avaliacao_faturamento = px.scatter(df_filtrado, x="Rating", y="Total",
title="Relação entre avaliação e Faturamento")
    fig_avaliacao_faturamento.update_xaxes(title="Avaliação")
    fig_avaliacao_faturamento.update_yaxes(title="Faturamento Total")
    col7.plotly_chart(fig_avaliacao_faturamento, use_container_width=True)
