from fastapi import FastAPI
from main import query
from env import chain
from pydantic import BaseModel
from result_process import process_result
import re


app = FastAPI()


class Input(BaseModel):
    personal_information: str


@app.post("/task1")
async def process_resume(input: Input):
    # Simulate processing the resume string
    for i in range(3):
        res = chain({"query": query(input.personal_information)})
        chunks = re.split(r'(\d+\.\s*Occupation:)', res['result'], flags=re.IGNORECASE)
        if len(chunks) > 1:
            break
    if len(chunks) > 1:
        output = process_result(chunks)
    else:
        output = res['result']

    return output
