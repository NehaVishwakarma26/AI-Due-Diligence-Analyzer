from langchain_community.vectorstores import Chroma
from embeddings import embedding_model

def retrieve(query,k=10,filters=None):
    vectordb=Chroma(
        collection_name="knowledge_base",
        embedding_function=embedding_model,
        persist_directory="./chroma_db"
    )
    # find similar 10 documents that are the answer to the query nearest 10 vectors
    results=vectordb.similarity_search(
        query,
        k=k,
        filter=filters
    )
    
    return results