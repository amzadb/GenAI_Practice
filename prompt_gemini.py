# Using LangChain Google Generative AI wrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give 5 bullet points to explain {topic} for beginners."
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = input("Enter a topic to explain: ")
print(chain.invoke({"topic": topic}))
