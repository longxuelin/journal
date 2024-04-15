import streamlit as st
import pandas as pd
import time


st.set_page_config(page_title='Электронные журналы', page_icon=None, layout="wide", menu_items=None,initial_sidebar_state="expanded", )


#nav_bar





def data ():
    db = pd.read_csv("test.csv", names=["Регистрационный номер",
                                           "Дата регистрации",
                                           "Дата утверждения",
                                           "Наименование документа",
                                           "Кем утвержден (должность)",
                                           "Кол-во листов",
                                           "Разработчик",
                                           "Место хранения",
                                           "Примечание",



                                          ],encoding='windows-1251')
    return db

last_num = data()['Регистрационный номер'].values[len(data())-1 if len(data()) > 0  else 1]

st.markdown("<h1 style='text-align: center; color: white;'>Журнал регистрации технической документации ОИТПЭ</h1>", unsafe_allow_html=True)

st.metric(label=f'Последний зарегистрированный номер:', value=f'{last_num}')

# Регистрация номера
def check_empty():
    if data().empty == True:
        number = 1
    else:
        last_num = data()['Регистрационный номер'].values[len(data())-1 if len(data()) > 0  else 1]
        w = last_num.find('-ОИТПЭ-24')
        number = int(last_num[:w])+1
    return number
number = check_empty()


# Боковое МЕНЮ

with st.sidebar:
    st.markdown("ОИТПЭ")


    def form_callback(data1, data2, data3, data4, data5, data6, data7, data8, data9):
        with open('test.csv', 'a+') as f:
            f.write(f"{data1},{data2},{data3}, {data4}, {data5}, {data6}, {data7}, {data8}, {data9}\n")


    with st.form(key="my_form", clear_on_submit=True, ):
        st.write("Введите данные:")

        # Ввод данных
        number = f'{number}-ОИТПЭ-24'
        name = st.text_input(':red[Наименование документа*]', placeholder="Акт обследования вентсистем", key='name')
        developer = st.text_input(':red[Разработчик*]', placeholder="Петров А.А.", key='developer')
        job_title = st.selectbox('Кем утвержден (должность)',
                                 ("ГИ", "ЗГИ ИП", "НОИТПЭ", "И.о. ГИ", "И.о. ЗГИ ИП", "И.о. НОИТПЭ"))
        pages = st.number_input('Кол-во листов', min_value=1)
        place = st.selectbox('Место хранения', (
        "зд.445 п.334", "зд.445 п.312", "зд. 401 УПАК п.402/2", "зд. 401 УПАК п.402/1", "зд.401 п.919/1",
        "зд.601 п.314", "зд.609 п.115", "зд.601 п.521", "зд.609 п.206", "зд. 00UYB п.04R113"))
        date_reg = st.date_input('Дата регистрации', format="DD.MM.YYYY")
        date_accept = st.date_input('Дата утверждения', format="DD.MM.YYYY")
        notes = st.text_input('Примечания', key='notes', placeholder="")

        submitted = st.form_submit_button("Ввод",type="primary")

        if submitted and number == '' or name == '' or job_title == '' or developer == '':
            error = st.error('Заполните поля')

        else:
            form_callback(number, date_reg, date_accept, name, job_title, pages, developer, place, notes)
            with st.spinner('Подождите...'):
                time.sleep(1)
            st.toast(f"{number} {name}")
            time.sleep(.8)



    st.divider()

    st.write("<h1 style='text-align: right; color: grey;font-size:14px'>V 0.0.1</h1>", unsafe_allow_html=True)

    st.write('<a href="mailto:oitp-sjs@ln.rosenergoatom.ru">Есть предложение? Нашел баг?</a>', unsafe_allow_html=True)




    # таблица с данными

st.dataframe((data()), height=490, width=1400, hide_index=True)

















