# import os
from pprint import pprint as pp

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# if api_key is None:
#     raise Exception("OPENAI_API_KEY not found in .env file")

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(text_splitter=text_splitter)

for doc in docs:
    pp(doc.page_content)
    pp("\n")
