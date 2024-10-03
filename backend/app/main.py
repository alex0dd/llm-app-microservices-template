from fastapi import FastAPI

import os

from app.utils import setup_openai_client

app = FastAPI()

server_type = os.environ.get("LLM_SERVER_TYPE", "vllm")
openai_client = setup_openai_client(server_type=server_type)

@app.get("/test")
def test_endpoint():
    return {"response": "Up"}

@app.get("/")
def get_sentence(about: str = "Thailand"):
    about = about.capitalize()
    completion = openai_client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "user", "content": f"Give me one iconic sentence about {about}."}
        ]
    )
    return {"response": completion.choices[0].message.content, "about": about}