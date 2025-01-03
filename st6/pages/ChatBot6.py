import streamlit as st
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI()  # API KEY 필요!

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state['messages'] = []

message = st.chat_input(placeholder="AI 에 메세지를 보냅니다")

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state['messages'].append({"message": message, "role": role})
    
for msg in st.session_state['messages']:
    send_message(msg['message'], msg['role'], save=False)

if message:
    send_message(message, "human")
    result = chat.predict(message)
    send_message(result, "ai")

    # session_state 에 저장된 내용 보고싶다면.
    # sidebar 에 그려보기
    # with st.sidebar:
    #     st.write(st.session_state)
