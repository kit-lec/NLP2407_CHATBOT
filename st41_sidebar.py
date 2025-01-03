import streamlit as st

st.title("PageTitle")

# st.sidebar.text_input("xxx")

# sidebar
with st.sidebar:
    # with 안에서는 굳이 st.sidebar 를 명시할 필요 없다.
    st.title("sidebar title")
    st.text_input("name")
    "Hello Everyone"

# Tab 추가
# 선택한 tab 값을 받아올수 있다.
# 이를 사용해서 tab 화면을 그릴수도 있다.
tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one:  # "A" 탭 화면 그리기
    st.write("aaa")

with tab_two:
    st.write("bbb")

with tab_three:
    st.write("ccc")


