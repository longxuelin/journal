import streamlit as st
import pandas as pd


st.set_page_config(page_title='AI', page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)


st.sidebar.page_link("app2.py", label="Chat")


# Первая колонка (ПОИСК)
col3, col4, col5 = st.columns([1,3,1])

with col3:
    with st.container(border=False):
        st.write('')
        st.write('')
        st.write('AI Generator')

with col4:
    with st.container(border=False):
        st.text_input("", placeholder='Поиск')

with col5:
    with st.container(border=False):
        st.write('')


# Вторая колонка (САМАРИ, ИСТОЧНИКИ, РЕЗУЛЬТАТЫ, ЧАТ)
col1, col2 = st.columns([3,1])

# САМАРИ
with col1:
    with st.container(border=True, height=700):
        st.markdown("AI Summary")
        st.write('something something something something something something something something something something something something something something something something')

        st.divider()
        st.markdown("Источники:")


        st.divider()
        st.markdown("Результаты:")

        data_df = pd.DataFrame((
            {
                "category": [
                    " Data Exploration",
                    " Data Visualization",
                    " LLM",
                    " Data Exploration",
                ],
            }
        ))

        st.data_editor(
            data_df,
            column_config={
                "category": st.column_config.SelectboxColumn(disabled=True,required=True, width= 1250)
            },
            hide_index=True,
        )



# ЧАТ
with col2:
    with st.container(border=True,height=700):
        st.header("Chat")
        prompt = st.chat_input("Напиши")
        if prompt:
             st.write(f"User: {prompt}")















st.write(
    """
       
       <style>
   
   
           section[data-testid="stSidebar"] {
               width: 10px !important; # Set the width to your desired value
           }
       </style>
       """,
    unsafe_allow_html=True,
)import streamlit as st
import pandas as pd


st.set_page_config(page_title='AI', page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)


st.sidebar.page_link("app2.py", label="Chat")


# Первая колонка (ПОИСК)
col3, col4, col5 = st.columns([1,3,1])

with col3:
    with st.container(border=False):
        st.write('')
        st.write('')
        st.write('AI Generator')

with col4:
    with st.container(border=False):
        st.text_input("", placeholder='Поиск')

with col5:
    with st.container(border=False):
        st.write('')


# Вторая колонка (САМАРИ, ИСТОЧНИКИ, РЕЗУЛЬТАТЫ, ЧАТ)
col1, col2 = st.columns([3,1])

# САМАРИ
with col1:
    with st.container(border=True, height=700):
        st.markdown("AI Summary")
        st.write('something something something something something something something something something something something something something something something something')

        st.divider()
        st.markdown("Источники:")


        st.divider()
        st.markdown("Результаты:")

        data_df = pd.DataFrame((
            {
                "category": [
                    " Data Exploration",
                    " Data Visualization",
                    " LLM",
                    " Data Exploration",
                ],
            }
        ))

        st.data_editor(
            data_df,
            column_config={
                "category": st.column_config.SelectboxColumn(disabled=True,required=True, width= 1250)
            },
            hide_index=True,
        )



# ЧАТ
with col2:
    with st.container(border=True,height=700):
        st.header("Chat")
        prompt = st.chat_input("Напиши")
        if prompt:
             st.write(f"User: {prompt}")















st.write(
    """
       
       <style>
   
   
           section[data-testid="stSidebar"] {
               width: 10px !important; # Set the width to your desired value
           }
       </style>
       """,
    unsafe_allow_html=True,
)
