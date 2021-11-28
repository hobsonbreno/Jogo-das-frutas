import streamlit as st;

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Digite o valor do seu Deposito")
    input_frutas = st.selectbox("Selecione a sua Fruta",["Morango","Maçã","Banana","Abacaxi","Acerola","Caja","Caju","laranja"])
    input_button_submit = st.form_submit_button("Enviar") 
    