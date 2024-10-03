from openai import OpenAI

def setup_openai_client(server_type: str, api_key: str="unused") -> OpenAI:
    assert server_type in ["ollama", "vllm"]
    match server_type:
        case "ollama":
            base_llm_server_url = "http://llm_server:11434/v1"
        case _:
            base_llm_server_url = "http://llm_server:8000/v1"

    client = OpenAI(
        base_url=base_llm_server_url,
        api_key=api_key,
    )
    return client