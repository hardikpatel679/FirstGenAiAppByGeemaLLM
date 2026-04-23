# FirstGenAiAppByGeemaLLM

A comprehensive AI application demonstrating integration with both online and offline large language models. This project showcases the use of Groq's cloud-based LLMs and Ollama's local Gemma model, built with Streamlit for interactive interfaces and LangChain for prompt management.

## Features

- **Online AI Integration**: Streamlit app using Groq API for fast, cloud-based LLM responses.
- **Offline AI Support**: Local Streamlit app with Ollama and Gemma 2B model for privacy-focused interactions.
- **LangChain Integration**: Utilizes LangChain for prompt templating, output parsing, and embeddings.
- **Python Basics Notebook**: Jupyter notebook covering Python fundamentals, data manipulation (Pandas, NumPy), and AI examples.
- **Environment Management**: Uses uv for dependency management and virtual environments.

## Installation

### Prerequisites

- Python 3.14 or higher
- Ollama installed (for offline model): [Install Ollama](https://ollama.ai/)
- API keys for Groq and LangSmith (optional for tracing)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FirstGenAiAppByGeemaLLM.git
   cd FirstGenAiAppByGeemaLLM
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirement.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   LANGSMITH_TRACING=true
   LANGCHAIN_PROJECT=your_project_name
   ```

4. For offline model, pull the Gemma model:
   ```bash
   ollama pull gemma:2b
   ```

## Usage

### Running the Online Groq App

```bash
uv run streamlit run groq_integration.py
```

Open http://localhost:8501 in your browser.

### Running the Offline Ollama App

```bash
uv run streamlit run Demo/app.py
```

Open http://localhost:8502 in your browser.

### Exploring Python Basics

Open `basics.ipynb` in Jupyter Notebook or VS Code to explore Python examples, including:
- Basic Python syntax
- Data structures (lists, sets, tuples, dictionaries)
- Pandas and NumPy for data manipulation
- LangChain with Ollama embeddings
- AI prompt examples

## Project Structure

```
FirstGenAiAppByGeemaLLM/
├── basics.ipynb              # Jupyter notebook with Python basics and AI examples
├── groq_integration.py       # Streamlit app for Groq LLM integration
├── main.py                   # Simple entry point script
├── pyproject.toml            # Project configuration and dependencies
├── requirement.txt           # Alternative requirements file
├── README.md                 # This file
├── example.txt               # Sample text file
└── Demo/
    └── app.py                # Streamlit app for local Ollama integration
```

## Dependencies

Key libraries used:
- `streamlit`: Web app framework
- `langchain`: LLM framework
- `langchain-groq`: Groq integration
- `langchain-community`: Community integrations (Ollama)
- `python-dotenv`: Environment variable management
- `pandas`, `numpy`: Data manipulation
- `ipykernel`: Jupyter support

See `pyproject.toml` for full dependency list.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- Groq for providing fast LLM APIs
- Ollama for local model hosting
- LangChain for simplifying LLM integrations
- Streamlit for easy web app development
