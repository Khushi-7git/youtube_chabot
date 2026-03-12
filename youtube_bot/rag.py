from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

vectordb=None

def store_transcript(text):
    global vectordb
    # Split the transcript into chunks
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks=text_splitter.split_text(text)
    embeddings=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectordb=FAISS.from_texts(chunks,embeddings)
    return len(chunks)

def search_transcript(query):
    global vectordb
    if vectordb is None:
        return "❌ No transcript loaded!"
    docs=vectordb.similarity_search(query,k=3)
    return "\n".join([doc.page_content for doc in docs])
