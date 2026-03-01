"""AI Student Doubt Solver - Native SDK Implementation.

This Streamlit application provides an interactive educational tool that uses
native SDK clients to communicate directly with multiple LLM providers (OpenAI,
Google Gemini, and Anthropic Claude). Users can ask questions or request explanations
on topics, and the AI teacher provides simple explanations, real-life examples, and
quiz questions.

Implementation:
    - Uses native SDK clients directly from each provider
    - Demonstrates provider-specific API patterns
    - Includes error handling and input validation

Requirements:
    - streamlit
    - openai
    - google-genai
    - anthropic
    - python-dotenv

Environment Variables:
    - OPENAI_API_KEY: API key for OpenAI
    - GOOGLE_API_KEY: API key for Google Gemini
    - ANTHROPIC_API_KEY: API key for Anthropic Claude

Usage:
    streamlit run ai_doubt_solver_client.py
"""

from dotenv import load_dotenv
load_dotenv()

# Using native SDK clients (not LangChain wrappers)
import streamlit as st
from langchain.prompts import PromptTemplate
from openai import OpenAI
from google import genai
import anthropic

# ============================================================================
# CONFIGURATION CONSTANTS
# ============================================================================
APP_TITLE = "🎓 AI Student Doubt Solver"
SIDEBAR_HEADER = "LLM Configuration"
LLM_PROVIDERS = ["OpenAI (GPT-4o-mini)", "Gemini (Flash)", "Claude (Sonnet)"]
OPENAI_MODEL = "gpt-4o-mini"
OPENAI_ROLE = "user"
GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL_NAME = "Gemini (Flash)"
CLAUDE_MODEL = "claude-sonnet-4-20250514"
CLAUDE_MODEL_NAME = "Claude (Sonnet)"
CLAUDE_MAX_TOKENS = 1024
INPUT_PLACEHOLDER = "Enter your question or topic:"
BUTTON_LABEL = "Explain"
RESPONSE_HEADER = "📙 Response from"
ERROR_EMPTY_TOPIC = "⚠️ Please enter a topic or question."
ERROR_API = "❌ An error occurred while processing your request:"
MIN_TOPIC_LENGTH = 3

# Prompt template for the AI teacher
# This structured template ensures consistent, educational responses
PROMPT_TEMPLATE = """
You are a friendly teacher.

Explain the topic: {topic}

1. Give a simple explanation
2. Give a real-life example
3. Provide 3 quiz questions
4. Provide answers
"""

# ============================================================================
# STREAMLIT UI SETUP
# ============================================================================

st.title(APP_TITLE)

# LLM Provider Selection
st.sidebar.header(SIDEBAR_HEADER)
llm_choice = st.sidebar.radio("Choose LLM Provider:", LLM_PROVIDERS)
st.sidebar.info("🔧 **Implementation:** Uses native SDK clients directly from each provider (OpenAI, Google Generative AI, Anthropic).")

# Initialize native SDK client based on user selection
# Each provider has its own client class and API patterns
try:
    if llm_choice == LLM_PROVIDERS[0]:  # OpenAI
        llm = OpenAI()
    elif llm_choice == LLM_PROVIDERS[1]:  # Gemini
        llm = genai.Client()
    else:  # Claude
        llm = anthropic.Anthropic()
except Exception as e:
    # Display error and stop execution if client initialization fails
    st.error(f"{ERROR_API} {str(e)}")
    st.stop()

topic = st.text_input(INPUT_PLACEHOLDER)

prompt = PromptTemplate(input_variables=["topic"], template=PROMPT_TEMPLATE)

if st.button(BUTTON_LABEL):
    # Input validation: ensure topic is not empty and meets minimum length
    if not topic or len(topic.strip()) < MIN_TOPIC_LENGTH:
        st.warning(ERROR_EMPTY_TOPIC)
    else:
        try:
            # Format the prompt with user's topic
            formatted_prompt = prompt.format(topic=topic.strip())
            
            # Call the appropriate API based on selected provider
            # Each provider has a different API structure
            
            if llm_choice == LLM_PROVIDERS[0]:  # OpenAI
                # OpenAI uses chat.completions.create with messages array
                response = llm.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[{"role": OPENAI_ROLE, "content": formatted_prompt}]
                )
                model_name = OPENAI_MODEL
                result = response.choices[0].message.content
                
            elif llm_choice == LLM_PROVIDERS[1]:  # Gemini
                # Gemini uses models.generate_content with contents parameter
                response = llm.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=formatted_prompt
                )
                model_name = GEMINI_MODEL_NAME
                result = response.text
                
            else:  # Claude
                # Claude uses messages.create with max_tokens and messages array
                response = llm.messages.create(
                    model=CLAUDE_MODEL,
                    max_tokens=CLAUDE_MAX_TOKENS,
                    messages=[{"role": OPENAI_ROLE, "content": formatted_prompt}]
                )
                model_name = CLAUDE_MODEL_NAME
                result = response.content[0].text
            
            # Display the response to the user
            st.subheader(f"{RESPONSE_HEADER} {model_name}")
            st.write(result)
        except Exception as e:
            # Handle any API errors gracefully with user-friendly message
            st.error(f"{ERROR_API} {str(e)}")
