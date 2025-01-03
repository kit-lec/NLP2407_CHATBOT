import streamlit as st

st.set_page_config (
    page_title="ChatBot",
    page_icon="😊",
)
st.title("ChatBot")

# chat_message() : chat message container 생성
#   name= 'user', 'assistant', 'ai', 'human'
with st.chat_message(name="human"):
    st.write("Hello!")

with st.chat_message(name='ai'):
    st.write('How are you?')

# chat input 위젯
# 화면 하단에 메세지 입력 위젯 표시
st.chat_input(placeholder="AI 에 메세지를 보냅니다")

# chat status
#  시간이 오래걸리는 작업에 대해서 진행 status(상태) 표시 위젯

# expaned=True 옵션을 주면, 드롭다운을 누르지 않아도 보임
import time
with st.status("Embedding file...", expanded=True) as status:
    time.sleep(3)
    st.write("Getting the file")
    time.sleep(3)
    st.write("Embedding the file")
    time.sleep(3)
    st.write("Caching the file")

    # update 도 할수 있다.
    status.update(label="오류", state="error")













