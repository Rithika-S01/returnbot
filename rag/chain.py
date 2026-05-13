from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

def get_chain():
    print("🔗 Loading database...")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="data/chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 4})

    print("🤖 Loading AI model...")
    llm = Ollama(model="tinyllama")

    return retriever, llm