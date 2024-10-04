import streamlit as st
import requests
from PIL import Image
import io

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

    .big-font {
        font-size: 50px !important;
        color: #303030;  /* 글자 색상 */
        font-family: 'Roboto', sans-serif;  /* 글꼴 설정 */
    }

    .reportview-container {
        background: #666666;  /* 연한 회색 */
    }

    .stApp {
        background-color: #666666; /* 앱 배경색을 연한 회색으로 설정 */
        color: black;  /* 기본 글자색을 검은색으로 설정 */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Dog Classifier 🐶</p>', unsafe_allow_html=True)

def upload_file():
    url='http://13.125.248.110:8044/uploadfile/'
    file=st.file_uploader('궁금한 강아지 사진을 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
    if file is not None:
        files={"file": (file.name, file.getvalue(), file.type)}
        response=requests.post(url, files=files)
        if response.status_code==200:
            st.success("이미지 업로드 성공!")
            st.write(response.json())
        else:
            st.error(f"이미지 업로드 실패... {response.status_code}")
            st.write(response.text)
    else:
        st.warning("파일을 업로드 해라")

upload_file()

