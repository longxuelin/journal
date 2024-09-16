import streamlit as st
from supabase import create_client, Client

# Инициализация Supabase
SUPABASE_URL = "https://vejfdkjsmivwndahxwhx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZlamZka2pzbWl2d25kYWh4d2h4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYxNjE1ODIsImV4cCI6MjA0MTczNzU4Mn0.S-dIvRc50gd2WBhiEvap7flCVdufDzMXU-YW-WZhUsI"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def save_to_supabase(data):
    try:
        response = supabase.table("set").insert(data).execute()
        return True
    except Exception as e:
        st.error(f"Ошибка при сохранении данных в Supabase: {str(e)}")
        return False


def launch_llm(llm_config, telegram_config):
    st.success("LLM запущен со следующими параметрами:")

    for config_name, config in [("LLM", llm_config), ("Telegram бот", telegram_config)]:
        with st.expander(f"Конфигурация {config_name}", expanded=True):
            for key, value in config.items():
                st.text(f"{key}: {value}")

    # Объединяем конфигурации для сохранения в Supabase
    combined_config = {**llm_config, **telegram_config}

    if save_to_supabase(combined_config):
        st.success("✅ Настройки успешно сохранены в Supabase!")
    else:
        st.error("❌ Не удалось сохранить настройки в Supabase.")


def main():
    st.set_page_config(page_title="Запуск LLM", layout="centered")

    with st.container():
        st.title("🚀 Современный запуск LLM")
        st.write("Настройте и запустите ваш LLM с легкостью!")

        with st.form("форма_запуска_llm"):
            st.header("🧠 Конфигурация LLM")
            llm_api = st.text_input("API ключ LLM:", type="password")
            llm_model = st.text_input("Название модели LLM:")

            with st.expander("🛠️ Расширенные настройки LLM"):
                system_prompt = st.text_input("Ситсемный промпт LLM:")
                prompt = st.text_input("Промпт LLM:")

                col1, col2 = st.columns(2)
                with col1:
                    temperature = st.slider("Температура:", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
                    top_k = st.slider("Top K:", min_value=1, max_value=100, value=50)
                    max_tokens = st.slider("Макс. токенов:", min_value=1, max_value=4096, value=1024)
                with col2:
                    top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)
                    frequency_penalty = st.slider("Штраф за частоту:", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
                    presence_penalty = st.slider("Штраф за присутствие:", min_value=-2.0, max_value=2.0, value=0.0,
                                                 step=0.1)

            st.header("🤖 Конфигурация Telegram бота")
            telegram_token = st.text_input("Токен Telegram бота:", type="password")
            telegram_chat_id = st.text_input("ID чата Telegram:")

            submit_button = st.form_submit_button("🚀 Запустить LLM")

        if submit_button:
            llm_config = {
                "api_key": llm_api,
                "model": llm_model,
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p,
                "max_tokens": max_tokens,
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty
            }
            telegram_config = {
                "telegram_token": telegram_token,
                "telegram_chat_id": telegram_chat_id
            }

            # if all(llm_config.values()) and all(telegram_config.values()):
            #     launch_llm(llm_config, telegram_config)
            # else:
            #     st.error("❗ Пожалуйста, заполните все поля перед запуском.")


if __name__ == "__main__":
    main()