import streamlit as st
import time

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")
# message 들을 저장하는 logic

message = st.chat_input(placeholder="AI 에 메세지를 보냅니다")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f'You said: {message}', "ai")


# message 를 입력할때마다. 페이지의 파이썬 코드가 재실행.
# 그래서 message 에 대한 history 가 없는 상태다.

# message 를 보관하는 (refresh 되어도) 시스템 필요.
# To next page...