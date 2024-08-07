import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This application is demo of implemenation of **HyDe** and **Decomposition** techniques used in RAG applications.
    The chatbot uses chromaDB vector store which has document embeddings of Kubernetes. 
    You can ask various questions related to kubernetes such as - 'What is Kuberntes?', 'What are volumes in Kubernetes?', 'Give example code of creating Volumes in K8s.' etc
    
    Choose **HyDe** from sidebar for getting response via HyDE approach that also gives sources of docs
    Choose **Decomposition** from sidebar that uses it's API to give response.
    
    Make sure that backend is running if you run this locally and test it with postman before connecting it to this streamlit app
"""
)