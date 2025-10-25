import streamlit as st
import requests
import os


API_BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

API_URL_TEXT = f"{API_BASE_URL}/analyze_text/"
API_URL_IMAGE = f"{API_BASE_URL}/analyze_image/"

st.title("SafeNet AI Dashboard")
st.write("Модуль анализа текста и изображений для выявления признаков кибер-шума и интернет-травли")

st.header("Анализ текста")
text_input = st.text_area("Введите текст для анализа:")
if st.button("Анализировать текст"):
    try:
        response = requests.post(API_URL_TEXT, data={"text": text_input})
        st.json(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка соединения с API: {e}")

st.header("Анализ изображения")
uploaded_file = st.file_uploader("Загрузите изображение", type=["png", "jpg", "jpeg"])
if st.button("Анализировать изображение") and uploaded_file:
    try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL_IMAGE, files=files)
        st.json(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка соединения с API: {e}")
