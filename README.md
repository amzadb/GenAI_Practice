# GenAI Practice Workspace

This repository contains quickstart scripts, prompt examples, and interactive Streamlit applications for working with popular Generative AI APIs, including OpenAI, Gemini, and Anthropic. It demonstrates both native SDK usage and LangChain integration patterns for text generation, model exploration, and prompt engineering.

## Contents

### Streamlit Applications (Interactive)
- `ai_doubt_solver_client.py` — Multi-provider doubt solver using native SDKs
- `ai_doubt_solver_chat.py` — Multi-provider doubt solver using LangChain wrappers

### Quickstart Scripts
- `openai_quickstart.py` — Quickstart for OpenAI API (text generation)
- `openai_image_analyzer.py` — OpenAI image analysis example
- `openai_models_list.py` — Lists available OpenAI models
- `gemini_quickstart.py` — Quickstart for Google Gemini API
- `gemini_models_list.py` — Lists available Gemini models
- `anthropic_quickstart.py` — Quickstart for Anthropic Claude API

### Prompt Engineering Examples
- `prompt_openai.py` — LangChain-based prompt examples for OpenAI
- `prompt_gemini.py` — LangChain-based prompt examples for Gemini
- `prompt_anthropic.py` — LangChain-based prompt examples for Anthropic

### Configuration
- `requirements.txt` — Python dependencies

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd GenAI_Practice
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Create API Keys (Step-by-Step)**
   
   **A. OpenAI API Key**
   - Go to OpenAI platform: https://platform.openai.com/
   - Sign in
   - Go to API Keys section
   - Click "Create new secret key"
   - Copy and save it

   **B. Google Gemini API Key**
   - Visit Google AI Studio: https://aistudio.google.com/app/apikey
   - Login with Google account
   - Click "Create API Key"
   - Copy the key

   **C. Anthropic Claude API Key**
   - Visit Anthropic console: https://console.anthropic.com/
   - Sign up / login
   - Go to API Keys
   - Click "Create Key"

4. **Create a `.env` file**
   - In the project root, create a file named `.env`.
   - Add your API keys in the following format:
     ```env
     OPENAI_API_KEY=your_openai_key_here
     GEMINI_API_KEY=your_gemini_key_here
     ANTHROPIC_API_KEY=your_anthropic_key_here
     ```
   - Save the file. The scripts will read your API keys from this file.

## Usage

### Running Quickstart Scripts
Run any quickstart script using Python:
```sh
python openai_quickstart.py
```

### Running Interactive Streamlit Applications
To run the interactive AI doubt solver applications:
```sh
streamlit run ai_doubt_solver_client.py
```
or
```sh
streamlit run ai_doubt_solver_chat.py
```

The applications allow you to:
- Switch between OpenAI (GPT-4o-mini), Google Gemini (Flash), and Anthropic Claude
- Ask questions or topics for detailed explanations
- Receive real-life examples and quiz questions

### Running Prompt Engineering Examples
Run the prompt examples with:
```sh
python prompt_openai.py
python prompt_gemini.py
python prompt_anthropic.py
```

Modify the scripts to experiment with different prompts, models, and API features.

## License

This project is for educational and practice purposes.
