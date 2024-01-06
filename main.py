import os
from pprint import pprint as pp

from dotenv import load_dotenv

# from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI

# from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise Exception("OPENAI_API_KEY not found in .env file")

# parser = argparse.ArgumentParser()
# parser.add_argument("--task", default="return a list of numbers")
# parser.add_argument("--language", default="python")
# args = parser.parse_args()

llm = OpenAI(api_key=api_key)


result = llm("Write a very very short poem")
pp(result)
