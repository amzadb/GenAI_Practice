"""AI Student Doubt Solver - LangChain Implementation.

This Streamlit application provides an interactive educational tool that uses
LangChain wrappers to communicate with multiple LLM providers (OpenAI, Google Gemini,
and Anthropic Claude). Users can ask questions or request explanations on topics,
and the AI teacher provides simple explanations, real-life examples, and quiz questions.

Implementation:
    - Uses LangChain wrappers for unified interface across different LLM providers
    - Provides consistent API for OpenAI, Google Gemini, and Anthropic Claude
    - Includes error handling and input validation

Requirements:
    - streamlit
    - langchain
    - langchain-openai
    - langchain-google-genai
    - langchain-anthropic
    - python-dotenv

Environment Variables:
    - OPENAI_API_KEY: API key for OpenAI
    - GOOGLE_API_KEY: API key for Google Gemini
    - ANTHROPIC_API_KEY: API key for Anthropic Claude

Usage:
    streamlit run ai_doubt_solver_chat.py
"""

from dotenv import load_dotenv
load_dotenv()

# Using LangChain wrappers for LLM providers
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

# ============================================================================
# CONFIGURATION CONSTANTS
# ============================================================================

# UI Text Constants
APP_TITLE = "🎓 AI Student Doubt Solver"
SIDEBAR_HEADER = "LLM Configuration"
LLM_PROVIDERS = ["OpenAI (GPT-4o-mini)", "Gemini (Flash)", "Claude (Sonnet)"]
INPUT_PLACEHOLDER = "Enter your question or topic:"
BUTTON_LABEL = "Explain"
RESPONSE_HEADER = "📙 Response from"

# Model Configuration
OPENAI_MODEL = "gpt-4o-mini"
GEMINI_MODEL = "gemini-3-flash-preview"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

# Error Messages
ERROR_EMPTY_TOPIC = "⚠️ Please enter a topic or question."
ERROR_API = "❌ An error occurred while processing your request:"
ERROR_UNKNOWN_MODEL = "Unknown Model"

# Validation
MIN_TOPIC_LENGTH = 3  # Minimum characters required for a valid topic input

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
st.sidebar.info("📚 **Implementation:** Uses LangChain wrappers for unified LLM interface across different providers.")

# Initialize LLM based on user selection
# LangChain wrappers provide a unified interface across different providers
try:
    if llm_choice == LLM_PROVIDERS[0]:  # OpenAI
        llm = ChatOpenAI(model=OPENAI_MODEL)
    elif llm_choice == LLM_PROVIDERS[1]:  # Gemini
        llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
    else:  # Claude
        llm = ChatAnthropic(model=CLAUDE_MODEL)
except Exception as e:
    # Display error and stop execution if LLM initialization fails
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
            # Format the prompt with user's topic and invoke the LLM
            formatted_prompt = prompt.format(topic=topic.strip())
            response = llm.invoke(formatted_prompt)
            
            # Extract model name from LLM instance for display
            # Different LangChain wrappers use different attribute names
            if hasattr(llm, 'model_name'):
                model_name = llm.model_name
            elif hasattr(llm, 'model'):
                model_name = llm.model
            else:
                model_name = ERROR_UNKNOWN_MODEL
            
            # Display the response to the user
            st.subheader(f"{RESPONSE_HEADER} {model_name}")
            st.write(response.content)
        except Exception as e:
            # Handle any API errors gracefully with user-friendly message
            st.error(f"{ERROR_API} {str(e)}")
