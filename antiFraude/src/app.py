import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card
blobUrl = ""

def show_image_and_validation(credit_card,url=blobUrl):
    st.image(url,caption="imagem enviada",use_column_width=True)
    st.write("Resultado da validação:")
    st.write("informaços do cartão de credito encontradas")
    if credit_card and credit_card["card_name"]:
        st.write("Cartão valido")
        st.write(f"Nome do titular {credit_card["card_name"]}")
    else:
        st.write("Esse não e um cartão valido")

def configure_interface():
    st.set_page_config(page_title=" Dio projeto anti fraude")
    uploaded_file = st.file_uploader('escolha um arquivo',type=["png","pdf","jpg","jpeg"])
    if uploaded_file is not None:
        fileName = uploaded_file.name
 
    blobUrl = upload_blob(uploaded_file,fileName)
    if blobUrl:
        st.write(f"Arquivo {fileName} enviado com sucesso")
        credit_card_info = analize_credit_card(blobUrl)
        show_image_and_validation(credit_card_info)
    else:
        st.write(f"Erro ao enviar o arquivo {fileName} para o Blob Storage")
    


if __name__ == "__main__":
    configure_interface()