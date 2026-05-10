import os

from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_rag():

    folder_path = "../data"

    documents = []

    # Read all txt files
    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            with open(
                os.path.join(folder_path, file),
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

                documents.append(
                    Document(page_content=text)
                )

    print(f"Loaded {len(documents)} documents")

    # Embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Chroma DB
    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="rag_db"
    )

    db.persist()

    print("✅ RAG database built successfully!")


if __name__ == "__main__":
    build_rag()