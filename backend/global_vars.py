from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv

llm, embedding_function, retriever = None, None, None
def init():
    load_dotenv()
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.7, )
    persist_dir = "chromadb"
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    newdb = Chroma(persist_directory=persist_dir, embedding_function=embedding_function)
    retriever = newdb.as_retriever()
    return llm, embedding_function, retriever

