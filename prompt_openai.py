# Using LangChain OpenAI wrapper
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms for a beginner student."
)

# Create the LLM instance
llm = ChatOpenAI(model="gpt-4o-mini")

# Create an LLMChain with the LLM and the prompt
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with an example input
topic = input("Enter a topic to explain: ")
response = chain.invoke({"topic": topic})

print(response)
