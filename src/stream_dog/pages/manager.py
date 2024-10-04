import streamlit as st
import pymysql
import requests
from PIL import Image
import io
import pymysql.cursors

# DB 연결 함수
def get_conn():
    conn= pymysql.connect(
        host='13.125.248.110',  # 데이터베이스 서버 주소
        user='nagazo',          # 데이터베이스 사용자 이름
        password='4444',        # 데이터베이스 비밀번호
        database='nagazodb',
        port = 53306,
        cursorclass=pymysql.cursors.DictCursor
        )
    return conn


# 이미지 가져오기 함수
def fetch_image(url):
    url='http://13.125.248.110:8044/uploadfile/'
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        st.error("Failed to fetch image from URL")
        return None

# 메인 애플리케이션
st.title("Image Processing Manager Page")

# DB에서 이미지 목록 가져오기
conn = get_conn()
with conn:
    with conn.cursor() as cursor:
        sql = "SELECT num, file_path FROM dog_class WHERE label IS NULL ORDER BY num"
        cursor.execute(sql)
        results = cursor.fetchall()

labels = st.text_input("정답을 입력하세요")

def labeling(num):
    from stream_dog.db import dml
    sql="update dog_class set label=%s where num=%s"
    dml(sql, labels, num)
