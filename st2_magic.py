import streamlit as st

st.write("Hello streamlit")
st.write([1, 2, 3, 4])
st.write({"x": 100, "y": 3.14})

from langchain.prompts import PromptTemplate
st.write(PromptTemplate)

p = PromptTemplate.from_template("xxxxx")
st.write(p)

# 걍 아래처럼 값을 표시해도, 웹 화면에 그려준다! --> magic!
# write() 없이도 표현 가능하나 (비추함.)
p 

10 + 200

[10, 20, 30, 40]

# streamlit 의 공식 api-reference
# https://docs.streamlit.io/develop/api-reference
# ↑ 함 보자. 많은 widget 들이 제공된다.

st.selectbox("Choose yoru model", ("GPT-3", "GPT-4"))