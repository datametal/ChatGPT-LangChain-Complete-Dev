import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise Exception("OPENAI_API_KEY not found in .env file")


llm = OpenAI(api_key=api_key)

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"],
)

code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({"language": "python", "task": "return a list of numbers"})

print(result["text"])
