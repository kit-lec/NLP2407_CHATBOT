import streamlit as st

# set_page_config() 페이지 설정
st.set_page_config(
    page_title= "Welcome Home",   # 페이지 탭에 표시
    page_icon="🐹",   # 페이지 탭에 표시되는 아이콘.
)
st.title("GPT Home")

# ./pages 라는 폴더를 생성.
#   정확히 이 이름으로 만들어야 함.  <- streamlit 은 위 이름의 폴더를 찾습니다.
#   여기에 page 파일들(*.py) 를 만들면 자동으로 sidebar 와 메뉴들이 그려짐.