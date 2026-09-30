"""Точка входа приложения MusicGuide.

На КТ-1 — прототип на Streamlit.
На следующих этапах — подключение BM25 и LLM.
"""

import streamlit as st

st.set_page_config(page_title="MusicGuide", page_icon="🎵", layout="centered")

st.title("🎵 MusicGuide")
st.caption("Поиск по музыкальной базе знаний (BM25 + LLM)")

query = st.text_input(
    "Ваш вопрос о музыке:",
    placeholder="Например: чем отличается джаз от блюза?",
)

if st.button("Найти ответ") and query:
    st.subheader("Найденные документы")
    st.info("Здесь появятся топ-5 фрагментов (BM25). [заглушка КТ-1]")

    st.subheader("Ответ")
    st.success("Здесь будет ответ LLM с источниками. [заглушка КТ-1]")

st.divider()
st.caption("КТ-1: прототип интерфейса. BM25 и LLM будут подключены на следующих этапах.")
