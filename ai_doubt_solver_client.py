from dotenv import load_dotenv
load_dotenv()

# Using native SDK clients (not LangChain wrappers)
import streamlit as st
from langchain.prompts import PromptTemplate
from openai import OpenAI
from google import genai
import anthropic

st.title("🎓 AI Student Doubt Solver")

# LLM Provider Selection
st.sidebar.header("LLM Configuration")
llm_choice = st.sidebar.radio(
    "Choose LLM Provider:",
    ["OpenAI (GPT-4o-mini)", "Gemini (Flash)", "Claude (Sonnet)"]
)

# Initialize LLM based on selection
if llm_choice == "OpenAI (GPT-4o-mini)":
    llm = OpenAI()
elif llm_choice == "Gemini (Flash)":
    llm = genai.Client()
else:  # Claude
    llm = anthropic.Anthropic()

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
    
    if llm_choice == "OpenAI (GPT-4o-mini)":
        response = llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": formatted_prompt}]
        )
        model_name = "GPT-4o-mini"
        result = response.choices[0].message.content
    elif llm_choice == "Gemini (Flash)":
        response = llm.models.generate_content(
            model="gemini-3-flash-preview",
            contents=formatted_prompt
        )
        model_name = "Gemini (Flash)"
        result = response.text
    else:  # Claude
        response = llm.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": formatted_prompt}]
        )
        model_name = "Claude (Sonnet)"
        result = response.content[0].text
    
    st.subheader(f"📙 Response from {model_name}")
    st.write(result)
