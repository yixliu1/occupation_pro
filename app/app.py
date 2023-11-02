from fastapi import FastAPI, HTTPException, Query
from main import query
from env import chain


app = FastAPI()

@app.post("/process_resume")
async def process_resume(resume: str):
    # Simulate processing the resume string
    res = chain({"query": query(resume)})
    return res['result']
