from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    base_url="http://vllm_server:8000/v1",
    api_key="dummy-token",
)

@app.get("/test")
def test_endpoint():
    return {"response": "Up"}

@app.get("/")
def read_root():
    completion = client.chat.completions.create(
        model="/mnt/model",
        messages=[
            {"role": "user", "content": "Give me one iconic sentence about Thailand."}
        ]
    )
    return {"response": completion.choices[0].message.content}