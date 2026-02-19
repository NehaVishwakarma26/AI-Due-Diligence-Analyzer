from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from urllib3.util.request import ChunksAndContentLength
from embeddings import embedding_model

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

def ingest_document(text,metadata):
    chunks=text_splitter.split_text(text)
    
    vectordb=Chroma(
        collection_name="knowledge_base",
        embedding_function=embedding_model,
        persist_directory="./chroma_db"
    )
    
    vectordb.add_texts(
        texts=chunks,
        metadatas=[metadata for _ in chunks]
    )
    
    vectordb.persist()
    
    return len(chunks)
