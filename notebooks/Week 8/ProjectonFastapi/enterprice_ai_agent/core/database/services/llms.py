from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path, override=True)

LLMs ={
    "grok":{
        "baseUrl":"https://api.groq.com/openai/v1",
        "apikey":"os.getenv('groq')",
        "model":"openai/gpt-oss-120b"
    },
    "ollama":{
        "baseUrl":"https://api.groq.com/openai/v1",
        "apikey":"",
        "model":""
    }
}