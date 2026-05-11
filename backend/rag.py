from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# Load Chroma DB
db = Chroma(
    persist_directory="rag_db",
    embedding_function=embeddings
)


def get_rag(query):
    return db