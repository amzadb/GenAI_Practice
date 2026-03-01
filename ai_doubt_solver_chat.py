from dotenv import load_dotenv
load_dotenv()

# Using LangChain wrappers for LLM providers
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

st.title("🎓 AI Student Doubt Solver")

# LLM Provider Selection
st.sidebar.header("LLM Configuration")
llm_choice = st.sidebar.radio(
    "Choose LLM Provider:",
    ["OpenAI (GPT-4o-mini)", "Gemini (Flash)", "Claude (Sonnet)"]
)

# Initialize LLM based on selection
if llm_choice == "OpenAI (GPT-4o-mini)":
    llm = ChatOpenAI(model="gpt-4o-mini")
elif llm_choice == "Gemini (Flash)":
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
else:  # Claude
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")

topic = st.text_input("Enter your question or topic:")

template = """
You are a friendly teacher.

Explain the topic: {topic}

1. Give a simple explanation
2. Give a real-life example
3. Provide 3 quiz questions
4. Provide answers
"""

prompt = PromptTemplate(input_variables=["topic"], template=template)

if st.button("Explain"):
    formatted_prompt = prompt.format(topic=topic)
    response = llm.invoke(formatted_prompt)
    
    # Get model name based on LLM type
    if hasattr(llm, 'model_name'):
        model_name = llm.model_name
    elif hasattr(llm, 'model'):
        model_name = llm.model
    else:
        model_name = "Unknown Model"
    
    st.subheader(f"📙 Response from {model_name}")
    st.write(response.content)
