from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# Load Chroma DB
db = Chroma(
    persist_directory="rag_db",
    embedding_function=embeddings
)


def get_rag(query):
    return db