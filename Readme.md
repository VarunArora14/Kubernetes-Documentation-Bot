### Kuberneted Documentation Bot🤖


This project was submitted at **Google Gemini API Developer competition 2024**.

This repo is code for GenAI chatbot made to answer user queries about documentations. It has markdown data fed to it using **chromaDB** vector store.
The data consists of **markdown files** based of kubernetes documentation stored by me as personal notes in Joplin app. It uses **sentence transformers - all-MiniLM-L6-v2** for creating embeddings.

The initial idea was making it a personal notes bot but since I had lot of code and documentation code as part of my notes, I felt like calling it Documentation bot makes more sense.
APIs for both **HyDe** and **Decomposition** techniques exist separately. Make sure to create virtual environment and try running and hitting backend APIs using postman before starting frontend on streamlit.

Please refer to the following video demo which is also hosted on youtube at - https://www.youtube.com/watch?v=jTsQqHk0E7E
