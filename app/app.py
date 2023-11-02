from fastapi import FastAPI, HTTPException, Query
from main import query
from env import chain
from pydantic import BaseModel


app = FastAPI()


class Input(BaseModel):
    personal_information: str


@app.post("/task1")
async def process_resume(input: Input):
    # Simulate processing the resume string
    print(query(input.personal_information))
    res = chain({"query": query(input.personal_information)})
    return res
