import streamlit as st
from agent import chat 

st.set_page_config(
    page_title="YouTube Bot",
    page_icon="🎥",
    layout="wide",
)
st.title("YouTube Bot 🎥")
st.subheader("Ask questions about any YouTube video!")

with st.sidebar:
    st.header("📺 load a YouTube video")
    url=st.text_input("Enter YouTube URL", "https://youtu.be/7NMYz-kRtdM")
    if st.button("Load Video"):
        with st.spinner("loading transcript...."):
            response=chat({url})
            st.success(response)

#chat

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("Ask a question about the video..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(prompt)
            st.write(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )