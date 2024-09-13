import streamlit as st
import time

from supabase import create_client


SUPABASE_URL = "https://vejfdkjsmivwndahxwhx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZlamZka2pzbWl2d25kYWh4d2h4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYxNjE1ODIsImV4cCI6MjA0MTczNzU4Mn0.S-dIvRc50gd2WBhiEvap7flCVdufDzMXU-YW-WZhUsI"


url = SUPABASE_URL
key = SUPABASE_KEY
supabase = create_client(url, key)


data = supabase.table("set").select("*").execute()





st.set_page_config(page_title='', page_icon=None, layout="centered", menu_items=None, initial_sidebar_state="expanded", )


st.markdown("<h1 style='text-align: center; color: white;'>Создание чат-бота RAG</h1>", unsafe_allow_html=True)



form = st.form("my_form")
form.write("Введите данные:")
token = form.text_input("Токен телеграм бота")
api_model = form.text_input("API вашей модели")
api_vb = form.text_input("API векторной базы")



supabase.table("set").insert({"API Ollama":f"{token}"}).execute()




accept = form.form_submit_button("Submit", type="primary")

if accept:
    st.session_state.token = token
    st.session_state.api_model = api_model
    st.session_state.api_vb = api_vb
    with st.spinner('Создаю...'):
        time.sleep(2)
        st.success('Бот создан', icon="✅")



st.write(st.session_state["api_model"])





# uploaded_files = st.file_uploader(
#     "Загрузите документы", accept_multiple_files=True
# )

