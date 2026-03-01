# GenAI Practice Workspace

This repository contains quickstart scripts, prompt examples, and interactive Streamlit applications for working with popular Generative AI APIs, including OpenAI, Gemini, and Anthropic. It demonstrates both native SDK usage and LangChain integration patterns for text generation, model exploration, and prompt engineering.

## ✨ Key Features

- **Multiple LLM Providers**: Support for OpenAI, Google Gemini, and Anthropic Claude
- **Two Implementation Approaches**: Compare LangChain wrappers vs native SDK clients
- **Production-Ready Code**: Comprehensive error handling, input validation, and user feedback
- **Well-Documented**: Module-level docstrings and inline documentation throughout
- **Clean Architecture**: Constants extraction, organized structure, and maintainable code
- **Interactive UI**: User-friendly Streamlit applications with helpful guidance

## Contents

### Streamlit Applications (Interactive)
- **`ai_doubt_solver_chat.py`** — Multi-provider doubt solver using **LangChain wrappers**
  - Unified interface across different LLM providers
  - Simplified API calls with consistent patterns
  - Ideal for rapid prototyping and provider-agnostic code

- **`ai_doubt_solver_client.py`** — Multi-provider doubt solver using **native SDKs**
  - Direct access to provider-specific features
  - Demonstrates each provider's unique API patterns
  - More control over API parameters and configurations

**Both applications include:**
- ✅ Comprehensive error handling and graceful failure recovery
- ✅ Input validation with minimum length requirements
- ✅ User-friendly error messages and warnings
- ✅ Sidebar information explaining implementation approach
- ✅ Full module and inline documentation

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

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd GenAI_Practice
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   
   **Note:** This project uses the latest `google-genai` package. The deprecated `google-generativeai` package is no longer supported.

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

4. **Configure Environment Variables**
   - In the project root, create a file named `.env`
   - Add your API keys in the following format:
     ```env
     OPENAI_API_KEY=your_openai_key_here
     GOOGLE_API_KEY=your_gemini_key_here
     ANTHROPIC_API_KEY=your_anthropic_key_here
     ```
   - Save the file. The scripts will automatically load these keys using `python-dotenv`
   - ⚠️ **Security Note**: Never commit your `.env` file to version control

## Usage

### Running Interactive Streamlit Applications

To run the AI doubt solver applications:

**LangChain Implementation:**
```sh
streamlit run ai_doubt_solver_chat.py
```

**Native SDK Implementation:**
```sh
streamlit run ai_doubt_solver_client.py
```

**Features Available:**
- 🔄 Switch between OpenAI (GPT-4o-mini), Google Gemini (Flash), and Anthropic Claude
- 💬 Ask questions or topics for detailed explanations
- 📚 Receive simple explanations with real-life examples
- 🎯 Get 3 quiz questions with answers for learning reinforcement
- ⚠️ Input validation ensures quality user input
- 🛡️ Robust error handling for API failures

**Sidebar Information:**
- Each application displays its implementation approach
- LangChain app shows unified wrapper usage
- Native SDK app shows provider-specific patterns

### Running Quickstart Scripts

Run any quickstart script using Python:
```sh
python openai_quickstart.py
python gemini_quickstart.py
python anthropic_quickstart.py
```

**Model Listing:**
```sh
python openai_models_list.py
python gemini_models_list.py
```

### Running Prompt Engineering Examples

Run the prompt examples with:
```sh
python prompt_openai.py
python prompt_gemini.py
python prompt_anthropic.py
```

Modify the scripts to experiment with different prompts, models, and API features.

## 📊 Code Quality

This project emphasizes production-ready code with the following quality features:

### Recent Improvements
- ✅ **Constants Extraction**: All magic strings moved to configuration constants
- ✅ **Error Handling**: Comprehensive try/catch blocks with user-friendly error messages
- ✅ **Input Validation**: Minimum length requirements and empty input checks
- ✅ **Documentation**: Module-level docstrings and inline comments throughout
- ✅ **Modern APIs**: Updated to use `google-genai` (replaced deprecated `google-generativeai`)
- ✅ **Code Organization**: Clear section headers and logical grouping of constants
- ✅ **User Experience**: Helpful sidebar information and validation warnings

### Code Quality Score
Both `ai_doubt_solver_*.py` applications: **7.5/10**

**Strengths:**
- Clean, maintainable code structure
- Proper error handling and validation
- Well-documented with docstrings
- Constants-based configuration

**Future Enhancements:**
- Add type hints for better IDE support
- Implement more specific exception handling
- Add logging for production debugging
- Extract repeated code into helper functions

## 📦 Dependencies

Core dependencies (see `requirements.txt`):
- `streamlit` — Web application framework
- `langchain` — LLM integration framework
- `langchain-openai` — OpenAI LangChain wrapper
- `langchain-google-genai` — Google Gemini LangChain wrapper
- `langchain-anthropic` — Anthropic LangChain wrapper
- `openai` — OpenAI native SDK
- `google-genai` — Google Gemini native SDK (replaced `google-generativeai`)
- `anthropic` — Anthropic native SDK
- `python-dotenv` — Environment variable management

## 🔧 Troubleshooting

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'google.generativeai'`**
- **Solution**: Update your dependencies. The old package has been replaced.
  ```sh
  pip uninstall google-generativeai
  pip install google-genai
  ```

**Issue: API Key Errors**
- **Solution**: Ensure your `.env` file is in the project root with correct key names:
  - `OPENAI_API_KEY` (not `OPENAI_KEY`)
  - `GOOGLE_API_KEY` (not `GEMINI_API_KEY`)
  - `ANTHROPIC_API_KEY` (not `CLAUDE_API_KEY`)

**Issue: Input Validation Warning**
- **Solution**: Enter at least 3 characters in the topic field

**Issue: Streamlit App Not Loading**
- **Solution**: Make sure you're in the correct directory and Streamlit is installed:
  ```sh
  pip install streamlit
  streamlit --version
  ```

## License

This project is for educational and practice purposes.
