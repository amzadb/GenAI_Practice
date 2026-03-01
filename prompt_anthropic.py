# Using LangChain Anthropic wrapper
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-20250514")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Teach {topic} like I am 10 years old."
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = input("Enter a topic to explain: ")
print(chain.invoke({"topic": topic}))
