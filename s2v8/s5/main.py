import argparse

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()


llm = OpenAI(openai_api_key=api_key)

code_prompt = PromptTemplate(
    input_variables=["task", "language"],
    template="Write a very short {language} function that will {task}",
)

code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({"language": args.language, "task": args.task})

print(result["text"])
