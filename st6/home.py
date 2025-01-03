import streamlit as st

st.set_page_config(
    page_title="GPT Home",
    page_icon="👀",
)
st.title("GPT Home")

# 마크다운 위젯으로 링크
st.markdown(
    """
### GPT 홈페이지!
- [ ] [ChatBot1](/ChatBot1)
- [ ] [ChatBot2](/ChatBot2)
- [ ] [ChatBot3](/ChatBot3)
- [ ] [ChatBot4](/ChatBot4)
- [ ] [ChatBot5](/ChatBot5)
- [ ] [ChatBot6](/ChatBot6)
"""
)