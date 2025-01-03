import streamlit as st
import time

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")
# refresh 되더라도 상태값을 기억하도록
# streamlit 에서는 session state 제공. 
#   => 여러번 refresh 되어도 data 가 보존.

# 'messages' 라는 key 값으로 session_state 에 담을거다.

# ↓ messages 초기화.  
# 주의: refresh 될때마다 이 코드가 실행될거다.  
# 초기화는 최초에 단 한번만 이루어져야 한다
if "messages" not in st.session_state:
    st.session_state['messages'] = []

st.write(st.session_state['messages'])  # 확인용

message = st.chat_input(placeholder="AI 에 메세지를 보냅니다")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)
        # session_state
        st.session_state['messages'].append({"messsage": message, "role": role})
    
        

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f'You said: {message}', "ai")
