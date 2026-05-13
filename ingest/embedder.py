from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
import os

def embed_policies():
    documents = []
    metadatas = []

    folder = os.path.join(os.path.dirname(__file__), "../data/raw_policies")
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(f"{folder}/{filename}", "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
                documents.append(text)
                metadatas.append({"source": filename.replace(".txt", "")})
                print(f"📄 Loaded: {filename}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents(documents, metadatas=metadatas)
    print(f"✂️ Total chunks created: {len(chunks)}")

    print("⏳ Creating embeddings... (takes 1-2 mins first time)")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory="data/chroma_db")
    db.persist()
    print("✅ Done! Database saved in data/chroma_db")

if __name__ == "__main__":
    embed_policies()