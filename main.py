from fastapi import FastAPI
from pydantic import BaseModel
from summa import summarizer

app = FastAPI()


class Info(BaseModel):
    id: int
    text: str


@app.get("/")
async def root():
    return {"message": "Software Project Component"}


@app.post("/text")
async def text(obj: Info):
    summarized_text = summarizer.summarize(
        obj.text, ratio=0.5, language="english", split=True
    )
    return {"summary": summarized_text}
