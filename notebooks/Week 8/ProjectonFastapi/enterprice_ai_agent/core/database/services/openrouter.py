import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# ----------------- LLM & Clients Setup -----------------
llm_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OpenRouterAPI"),
)

MODEL = "openai/gpt-oss-120b"
EMBEDDING_MODEL = "nvidia/nemotron-3.5-embed-8b:free"