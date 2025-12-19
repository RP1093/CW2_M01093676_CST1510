import streamlit as st

from openai import OpenAI
client = OpenAI(api_key="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")

st.title("Chat with GPT")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    st.chat_message(messages["role"]).write(message["content"])


prompt = st.chat_input("Enter your messages:")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    completion = client.chat.completion.create(
        model="gpt-5.2",
        messages= st.session_state.messages
    )

reply = st.chat_message('user').markdown(prompt)
st.session_state.messages.append({"role": "assisstant", "content": reply})
st.chat_message("assistant").write(reply)
