# GenAI Practice Workspace

This repository contains quickstart scripts and prompt examples for working with popular Generative AI APIs, including OpenAI, Gemini, and Anthropic. It is designed to help you get started quickly with text and image generation, model exploration, and prompt engineering.

## Contents

- `openai_quickstart.py` — Quickstart for OpenAI API (text generation)
- `openai_image_analyzer.py` — OpenAI image analysis example
- `openai_models_list.py` — Lists available OpenAI models
- `prompt_openai.py` — Prompt engineering examples for OpenAI
- `gemini_quickstart.py` — Quickstart for Gemini API
- `gemini_models_list.py` — Lists available Gemini models
- `prompt_gemini.py` — Prompt engineering examples for Gemini
- `anthropic_quickstart.py` — Quickstart for Anthropic API
- `prompt_anthropic.py` — Prompt engineering examples for Anthropic
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

Run any script using Python:
```sh
python openai_quickstart.py
```

Modify the scripts to experiment with different prompts, models, and API features.

## License

This project is for educational and practice purposes.
