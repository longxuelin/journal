import streamlit as st
import pandas as pd
import time




st.set_page_config(page_title='Журналы', page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)


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
                                            "Документ"


                                          ],encoding='windows-1251')
    return db

last_num = data()['Регистрационный номер'].values[len(data())-1 if len(data()) > 0  else 1]

st.markdown("<h1 style='text-align: center; color: white;'>Журнал регистрации технической документации ОИТПЭ</h1>", unsafe_allow_html=True)

st.markdown(f'Последний зарегистрированный номер: {last_num}')

# Регистрация номера
def check_empty():
    if data().empty == True:
        number = 1
    else:
        last_num = data()['Регистрационный номер'].values[len(data()) - 1 if len(data()) > 0 else 1]
        w = last_num.find('-ОИТПЭ-24')
        number = int(last_num[:w]) + 1
    return number
number = check_empty()



# Первая колонка
col3, col4, col5 = st.columns([1,3,1])

with col3:
    with st.container(border=False):
        st.write('')
        st.write('')

#data3, data4, data5, data6, data7, data8, data9

with col4:
    # Форма
    with st.container(border=False):
        def form_callback(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10):
            with open('test.csv', 'a+') as f:
                f.write(f"{data1},{data2},{data3}, {data4}, {data5}, {data6}, {data7}, {data8}, {data9}, {data10}\n")


        with st.form(key="my_form", clear_on_submit=True, ):
            st.write("Введите данные:")

            # Ввод данных
            number = f'ОИТПЭ-{number}-24'
            name = st.text_input('Наименование документа*', key='name')
            developer = st.text_input('Разработчик*', key='developer')
            job_title = st.selectbox('Кем утвержден (должность)',("ГИ","ЗГИ ИП","НОИТПЭ","И.о. ГИ","И.о. ЗГИ ИП","И.о. НОИТПЭ"))
            pages = st.number_input('Кол-во листов', min_value=1)
            place = st.selectbox('Место хранения',("зд.445 п.334", "зд.445 п.312", "зд. 401 УПАК п.402/2", "зд. 401 УПАК п.402/1", "зд.401 п.919/1", "зд.601 п.314",  "зд.609 п.115", "зд.601 п.521", "зд.609 п.206", "зд. 00UYB п.04R113"))
            date_reg = st.date_input('Дата регистрации', format="DD.MM.YYYY")
            date_accept = st.date_input('Дата утверждения', format="DD.MM.YYYY")
            notes = st.text_input('Примечания', key='notes', placeholder="")
            upload = st.file_uploader('Загрузите документ')
            link = ""

            submitted = st.form_submit_button("Ввод")

            if submitted and number == '' or name == '' or job_title == '' or developer == '':
                error = st.error('Заполните поля')

            else:
                form_callback(number, date_reg, date_accept, name, job_title, pages, developer, place, notes, link)
                with st.spinner('Подождите...'):
                    time.sleep(0)
                success = st.success(
                    f"Данные добавлены: Регистрационный номер {number}, Наименование документа {name}, ")
                time.sleep(1)
                success.empty()

with col5:
    with st.container(border=False):
        st.write('')






# Вторая колонка
col3, col4, col5 = st.columns([1,5,1])

with col3:
    with st.container(border=False):
        st.write('')
        st.write('')


with col4:
    # таблица с данными
    with st.container(border=False):
        st.dataframe((data()), height=400, width=1400, hide_index=True)

with col5:
    with st.container(border=False):
        st.write('')













