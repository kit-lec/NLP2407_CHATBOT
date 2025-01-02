# Streamlit 에선 'data 가 변경'될때 마다 python 파일 '전체'가 다시 실행된다. (py 파일 위에서부터 아래까지 전부 다시 실행)
# 가령 사용자가 무언가를 입력하거나 slider 를 드래그 해서 data 가 변경될때마다 ..

import streamlit as st
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

st.title(today)

model = st.selectbox("Choose your model", ("GPT-3", "GPT-4"))
st.write(model)

# ★ 웹개발자들에겐 미리 말하지만, 
# 이건 React.js 나 flutter 의 동작과는 다릅니다 <- 이들은 화면의 일부분을 업데이트 하는 동작이다.
# streamlit 은 전체 페이지가 refresh 된다.

# -------------------------------------
# 입력

name = st.text_input("What is your name")
st.write(name)

# 여기서 'refresh' 된다는 것은 브라우저 좌상단의 reload 의 의미는 아니다.
# refresh 는 py 파일 전체가 위에서부터 아래까지 다시 실행된다는 뜻이다.


# slider
value = st.slider(label="temperature", min_value=0.1, max_value=1.)

# 특정값에 따라 보여지거나, 보여지지 않거나 지정 가능

if model == "GPT-3":
    st.write("cheap")
else:
    st.write("expensive")

if model == "GPT-3":
    st.write("값싼 모델")
else:
    st.write("비싼 모델")
    country = st.text_input("What is your country?")
    st.write(country)





