from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from openai import OpenAI
import os
from ingestion import ingest_document
from pipeline import process_query


app=FastAPI()
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

class QueryRequest(BaseModel):
    question:str
    
class IngestRequest(BaseModel):
    text:str
    metadata:dict
    
@app.post("/ingest")
def ingest(data:IngestRequest):
    chunks=ingest_document(data.text,data.metadata)
    return {"chunks_ingested":chunks}

@app.post("/query")
def query(data:QueryRequest):
    result=process_query(data.question)
    return result