import os

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise Exception("OPENAI_API_KEY not found in .env file")

# chat = ChatOpenAI(api_key=api_key, verbose=True)
loader = TextLoader("facts.txt")
docs = loader.load()

print(docs)
