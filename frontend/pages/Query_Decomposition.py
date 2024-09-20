import streamlit as st
import requests

st.title("Kubernetes Documentation Bot🤖")


st.subheader("Decomposition")
st.markdown("This techniques breaks complex query to smaller sub-queries and gives answer for each. Then these answers are combined as context to question and answer generated")

    
# Initialize chat history
if "decomposition_messages" not in st.session_state:
    st.session_state.decomposition_messages = []

# Display chat messages from history on app rerun
for message in st.session_state.decomposition_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.decomposition_messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if len(st.session_state.decomposition_messages):
            answer = requests.post("http://127.0.0.1:5000/decomposition/generate", json={"question": st.session_state.decomposition_messages[-1]["content"]})
            answer = answer.json()
            api_type = "Decomposition"
            resp_string =  f"{api_type} response\n\n" + answer['response']
            response = st.markdown(resp_string)
    st.session_state.decomposition_messages.append({"role": "assistant", "content": resp_string})
