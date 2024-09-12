import streamlit as st
from pydantic import ValidationError
from datetime import datetime, time
from contratopydantic import Vendas
from database import salvar_no_postgres

def main():

    st.title("Sistema de CRM Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data=  st.date_input("Campo para selecionar a data em que a venda foi realizada.", datetime.now())
    hora= st.time_input("Hora em que a venda foi realizada.", value=time(9,0))
    valor=st.number_input("valor monetário da venda realizada.", min_value=0.0, format="%.2f")
    quantidade=st.number_input("Quantidade de produtos vendidos.", min_value=1, step=1)
    produto=st.selectbox("Campo de seleção para escolher o produto vendido.", ["ZapFlow com Llama3.0", "ZapFlow com chatGPT", "ZapFlow com Gemini"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)

            # Validando os dados com Pydantic
            # venda é a instancia da minha classe Vendas
            venda = Vendas(
                    email=email,
                    data=data_hora,
                    valor=valor,
                    quantidade=quantidade,
                    produto=produto
                )       
            st.write(venda)
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(f"Erro na validação dos dados: {e}")


if __name__ =="__main__":
    main()