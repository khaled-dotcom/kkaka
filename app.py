import streamlit as st
from groq import Groq

st.title("Groq Chatbot with Your API Key")

# Your API key (not secure for public repos!)
API_KEY = "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"

client = Groq(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

def send_message(user_message):
    st.session_state.messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=st.session_state.messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    assistant_reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

user_input = st.text_input("Ask me anything:")

if user_input:
    send_message(user_input)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Assistant:** {msg['content']}")
