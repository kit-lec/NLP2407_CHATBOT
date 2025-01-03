import streamlit as st
import time

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")

# sesstion_state['messages'] 내용을 그리자.


if "messages" not in st.session_state:
    st.session_state['messages'] = []

message = st.chat_input(placeholder="AI 에 메세지를 보냅니다")

# 
def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state['messages'].append({"message": message, "role": role})
    
# session_state 에 'messages' 가 있다면  send_message() 호출
# 화면에 그릴때는 session 에 저장하면 안되기에 save=False 로 지정
for msg in st.session_state['messages']:
    send_message(msg['message'], msg['role'], save=False)

if message:
    send_message(message, "human")  # save=True  session 에 저장
    time.sleep(2)
    send_message(f'You said: {message}', "ai")

    # session_state 에 저장된 내용 보고싶다면.
    # sidebar 에 그려보기
    with st.sidebar:
        st.write(st.session_state)
