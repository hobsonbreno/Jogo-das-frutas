import streamlit as st;

st.title("Jogo das Frutas")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_deposito= st.number_input(label="Digite o Valor que Deseja Depositar:",format="%d",step=1)
    input_aposta= st.number_input(label="Digite o Valor da sua Aposta:",format="%d",step=1)
    input_button_submit = st.form_submit_button("Enviar") 
    
    if input_button_submit:
        
        st.write(f'Seu nome é :{input_name}')
        st.write(f'Seu deposito foi:{input_deposito}','reais')
        st.write(f'Sua aposta foi:{input_aposta}','reais')
        st.write(f'A soma foi :{input_aposta + input_deposito }')
        st.write(f'A subtração foi :{input_aposta - input_deposito }')
        st.write(f'A multiplicação foi :{input_aposta * input_deposito }')
        st.write(f'A divisão foi :{input_aposta / input_deposito }')
        st.write(f'O resto foi: {input_aposta % input_deposito }')
        