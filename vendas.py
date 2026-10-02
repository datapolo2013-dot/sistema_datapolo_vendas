# 1 passo titulo sistema de vendas



# 2 passo seção cadastrar vendas
# campo data
# vendedor
# produto
# qtde
# valor
# botão # quando clicar botão adiciona venda
# secçao vendas cadastradas
 # tabela com as vendas    

# secao dashboard
    # metrica faturamento total
    # grafico coluna venda por vendedor
    # grafico pizza venda por produto

    # streamlit
    # pandas
    # plotly

import streamlit as st
import pandas as pd
import plotly.express as px
# streamlit run vendas.py

dadosped = pd.read_csv("vendas.csv")

st.write("# SISTEMAS DE VENDAS")

# SEÇAO CADASTRO
# sidebar coloca ao lado sem formulario na tela
st.sidebar.write("## CADASTRAR VENDAS")
#st.write("## CADASTRAR VENDAS")

data = st.sidebar.date_input("Data", "today")
vendedor = st.sidebar.selectbox("Vendedor", [ "Ana", "Jose", "Antonio"])
produto = st.sidebar.selectbox("Produto", [ "notebook", "celular", "fone"])
qtde =  st.sidebar.number_input("Qtde", step=1)
valor = st.sidebar.number_input("Valor")
botao = st.sidebar.button("Gravar")

if botao:
#    if valor <= 0 or produto == 0:
#       st.warning("preencha valor")
     dadospedn = [str(data), vendedor, produto, quantidade, valor]
     ultima_vendas = len(dadosped)
     dadosped.loc[ultima_vendas] = dadospedn
     dadosped.to_csv("vendas.csv", index=False)

  

# print(dadospedn)  somente termianl
     st.success("Pedido incluido com Sucesso")
    
st.write("## VENDAS CADASTRADAS")

# visualizar vendas

st.dataframe(dadosped)
# dashboard

st.write("## DASHBOARD")

  # metrica faturamento total
  
total = dadosped["valor"].sum
st.metric("faturamento total", f"R$ {total}")

  
    # grafico coluna venda por vendedor
grafico1 = px.bar(dadosped, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)
    # grafico pizza venda por produto
grafico2 = px.pie(dadosped, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)



