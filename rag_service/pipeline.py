from config import client,CHAT_MODEL
from retrieval import retrieve
from prompts import *
import json

def chat(prompt):
    response=client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role":"user","content":prompt}]

    )
    return response.choices[0].message.content.strip()

def classify(question):
    return chat(CLASSIFY_PROMPT.format(question=question))

def rewrite(question):
    return chat(REWRITE_PROMPT.format(question=question))

def expand(question,classification):
    if classification=="cross-domain":
        response=chat(EXPAND_PROMPT.format(question=question))
        
        try:
            return eval(response)
        
        except:
            return [question]
    return [question]


def rerank(question,docs):
    scored=[]
    for doc in docs:
        score=chat(RERANK_PROMPT.format(
            question=question,
            document=doc.page_content
        ))
        
        try:
            scored.append((doc,int(score)))
        except:
            scored.append((doc,5))
        
        
    scored.sort(key=lambda x:x[1],reverse=True)
    return [doc for doc,_ in scored]


def generate_answer(question, docs):
    context = "\n\n".join([d.page_content for d in docs[:5]])

    prompt = f"""
You are an enterprise knowledge analyst.

Return ONLY valid JSON.
Do NOT wrap in markdown.
Do NOT use backticks.

JSON format:
{{
    "answer": "",
    "key_points": [],
    "risk_flags": [],
    "contradictions": [],
    "confidence_score": 0.0
}}

Context:
{context}

Question:
{question}
"""

    response = chat(prompt)

    cleaned = response.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]

    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except:
        return {
            "answer": cleaned,
            "confidence_score": 0.5
        }


 
def process_query(question):
    classification=classify(question)
    rewritten=rewrite(question)
    subqueries=expand(rewritten,classification)
    
    all_docs=[]
    
    for q in subqueries:
        results=retrieve(q,k=10)
        all_docs.extend(results)
        
    reranked=rerank(question,all_docs)
    answer=generate_answer(question,reranked)
    
    return answer
    