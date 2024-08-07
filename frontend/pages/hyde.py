import streamlit as st
import requests

st.title("Kubernetes Documentation Bot🤖")


st.subheader("HyDe")
st.markdown("Retrieves multiple docs via web search to get closer to embeddings improving response")

    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if len(st.session_state.messages):
            answer = requests.post("http://127.0.0.1:5000/hyde/generate", json={"question": st.session_state.messages[-1]["content"]})
            answer = answer.json()
            api_type = "HyDe"
            # st.text(st.session_state.messages[-1])
            resp_string =  f"{api_type} response\n\n" + answer['response'] + "\n" + f"sources: {answer['sources']}"
            response = st.markdown(resp_string)
    st.session_state.messages.append({"role": "assistant", "content": resp_string})
