import streamlit as st
import pymysql
import requests
from PIL import Image
import io
import pymysql.cursors

# DB 연결 함수
def get_conn():
    conn= pymysql.connect(
        host='172.31.41.140',  # 데이터베이스 서버 주소
        user='nagazo',          # 데이터베이스 사용자 이름
        password='4444',        # 데이터베이스 비밀번호
        database='nagazodb',
        port = 53306,
        cursorclass=pymysql.cursors.DictCursor
        )
    return conn


# 이미지 가져오기 함수
def fetch_image(url):
    #url='http://13.125.248.110:8044/uploadfile/'
    #url='http://13.125.248.110:8044/uploadfile/'
    #response = requests.get(url)
    #if response.status_code == 200:
    #image = Image.open(io.BytesIO(response.content))
    image = Image.open(io.BytesIO(url))
    return image
    #else:
        #st.error("Failed to fetch image from URL")
        #return None

# 메인 애플리케이션
st.title("Image Processing Manager Page")

# DB에서 이미지 목록 가져오기
conn = get_conn()
with conn:
    with conn.cursor() as cursor:
        sql = "SELECT num, file_path FROM dog_class WHERE label IS NULL ORDER BY num"
        cursor.execute(sql)
        results = cursor.fetchall()

# 각 이미지에 대해 라벨링 처리
for row in results:
    num = row['num']
    file_path = row['file_path']
    print(file_path)

    # 이미지를 가져와서 Streamlit에 표시
    st.write(f"Image Number: {num}")
    image = fetch_image(file_path)

    if image:
        st.image(image, caption=f"Image {num}", use_column_width=True)

        # 라벨 입력 필드 및 제출 버튼 생성
        label = st.text_input(f"Enter label for image {num}", key=num)  # 각 이미지에 대해 다른 키 값 부여

        if st.button(f"Submit Label for Image {num}", key=f"submit_{num}"):
            if label:  # 라벨이 입력된 경우에만 처리
                with conn.cursor() as cursor:
                    update_sql = "UPDATE dog_class SET label = %s WHERE num = %s"
                    cursor.execute(update_sql, (label, num))
                    conn.commit()
                    st.success(f"Label for image {num} updated successfully.")
            else:
                st.warning("Please enter a label before submitting.")
