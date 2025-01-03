import streamlit as st
import time

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")
# message 들을 저장하는 logic

messages = []  # list 를 만들어서 message 들을 쌓아가면 안되나?

message = st.chat_input(placeholder="AI 에 메세지를 보냅니다")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)
        messages.append({"messsage": message, "role": role})
    st.write(messages)  # 확인용) list 에 잘 쌓이는지 확인

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f'You said: {message}', "ai")

# message 를 입력하면, 추가되는 것이 아니다, update 가 된다? 왜?

# refresh 될때마다 코드의 처음부터 끝까지 재실행.
# messages = [] <- 다시 빈 리스트부터 실행되기 때문.

# refresh 되더라도 상태값을 기억하도록
# streamlit 에서는 session state 제공. 
#   => 여러번 refresh 되어도 data 가 보존.