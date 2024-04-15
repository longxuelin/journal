import streamlit as st
import pandas as pd
import time


st.set_page_config(page_title='Электронные журналы', page_icon=None, layout="wide", menu_items=None,initial_sidebar_state="expanded", )




def data ():
    db = pd.read_csv("PTO.csv", names=["Подразделение",
                                        "Разработчик",
                                           "Дата поступления (ГУТД)",
                                           "Дата проверки (ГУТД)",
                                           "Дата поступления (ГППТД)",
                                           "Дата проверки (ГППТД)",
                                           "Наименование документа",
                                           "Кто проверил (ГППТД)",
                                           "Кто проверил (ГУТД)",
                                           "Дата визирования (ГППТД)",
                                           "Дата визирования (ГУТД)",
                                           "Кем утвержден",
                                           "Примечание"



                                          ],encoding='windows-1251')
    return db


st.markdown("<h1 style='text-align: center; color: white;'>Журнал нормконтроля перечней ТД в ПТО</h1>", unsafe_allow_html=True)



# Боковое МЕНЮ

with st.sidebar:
    st.markdown("ПТО")


    def form_callback(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13):
        with open('PTO.csv', 'a+') as f:
            f.write(f"{data1},{data2},{data3}, {data4}, {data5}, {data6}, {data7}, {data8}, {data9}, {data10}, {data11}, {data12}, {data13}\n")


    with st.form(key="my_form", clear_on_submit=True, ):
        st.write("Введите данные:")

        # Ввод данных
        sub = st.selectbox('Подразделение',
                                 ("АХО", "ОИТПЭ", "ЦВт", "РЦ-1", "РЦ-2", "ЦТАИ"))

        developer = st.text_input(':red[Разработчик*]', placeholder="Ф.И.О.", key='developer')

        date_r = st.date_input('Дата поступления (ГУТД)', format="DD.MM.YYYY", key='date_r')

        date_a = st.date_input('Дата проверки (ГУТД)', format="DD.MM.YYYY", key='date_a')

        date_rr = st.date_input('Дата проверки (ГППТД)', format="DD.MM.YYYY", key='date_rr')

        date_aa = st.date_input('Дата проверки (ГППТД)', format="DD.MM.YYYY", key='date_aa')

        name = st.text_input(':red[Наименование документа*]', placeholder="Ф.И.О.", key='name')

        check_GPPTD = st.selectbox('Кто проверил (ГППТД)',
                                   ("Соенко",),  key='check_GPPTD')

        check_GUTD = st.selectbox('Кто проверил (ГУТД)',
                           ("Трудовая",), key='check_GUTD')

        date_viz_GPPTD = st.date_input('Дата визирования (ГППТД)', format="DD.MM.YYYY", key='date_viz_GPPTD')

        date_viz_GUTD = st.date_input('Дата визирования (ГУТД)', format="DD.MM.YYYY", key='date_viz_GUTD')

        apr = st.selectbox('Кем утвержден',
                   ("ЗДОВ",), key='apr')

        notes = st.text_input('Примечания', key='notes', placeholder="")



        submitted = st.form_submit_button("Ввод", type="primary")

        if submitted:

            form_callback(sub, developer, date_r, date_a, date_rr, date_aa, name, check_GPPTD, check_GUTD, date_viz_GPPTD, date_viz_GUTD, apr, notes)
            with st.spinner('Подождите...'):
                time.sleep(1)
            st.toast(f"ЗБС")
            time.sleep(.8)



    st.divider()

    st.write("<h1 style='text-align: right; color: grey;font-size:14px'>V 0.0.1</h1>", unsafe_allow_html=True)

    st.write('<a href="mailto:oitp-sjs@ln.rosenergoatom.ru">Есть предложение? Нашел баг?</a>', unsafe_allow_html=True)




    # таблица с данными

st.dataframe((data()), height=490,  hide_index=True)













