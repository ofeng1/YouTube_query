import os
from typing import List

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI(os.environ.get("OPENAI_API_KEY"))


def get_embeddings(text: List[str], model: str = "text-embedding-3-small"):
    response = openai_client.embeddings.create(input=text, model=model)

    return [entry.embedding for entry in response.data]
