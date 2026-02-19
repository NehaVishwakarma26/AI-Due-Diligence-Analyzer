CLASSIFY_PROMPT="""
Classify the query into one of:
company,products,employees,contracts,cross-domain.
Return only the label.

Query: {question}
"""

REWRITE_PROMPT="""
Rewrite this query to improve document retrieval precision:

{question}
"""

EXPAND_PROMPT="""
Break this into 3 focused subqueries if cross-domain.
Return as Python list.

Query: {question}

"""

RERANK_PROMPT="""
Score relevance (1-10) of this document to the query.

Query: {question}
Document: {document}
Return only the number.
"""
