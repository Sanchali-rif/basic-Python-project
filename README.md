# AI Agent Workspace

A monorepo containing multiple AI agent projects built with Python, LangChain, and various AI/ML tools.

## Workspace Structure

```
AI_Agent/
├── project_1/     # LangChain-based AI Agent with Gemini
├── project_2/     # Document Processing AI with Streamlit UI
├── project_3/     # Computer Vision & ML Project (in development)
└── README.md      # This file
```

## Projects

### Project 1: AI Agent
A conversational AI agent powered by **Google Gemini** using LangChain framework.

**Features:**
- Conversational interface
- Tool support (calculator, greeting, etc.)
- LangGraph integration
- Environment variable management via `.env`

**Tech Stack:** Python 3.14+, LangChain, LangGraph, Google GenAI, OpenAI

**Quick Start:**
```bash
cd project_1
python -m pip install -e .
python test.py
```

### Project 2: Document Processing AI
An AI-powered document analysis tool with a **Streamlit** web interface.

**Features:**
- Document (PDF) processing
- LangChain with Google GenAI backend
- Interactive web UI
- Streamlit-based deployment

**Tech Stack:** Python 3.14+, Streamlit, LangChain, Google GenAI, PyPDF2

**Quick Start:**
```bash
cd project_2
python -m pip install -e .
streamlit run src/project_2/__init__.py
```

### Project 3: Computer Vision & ML (In Development)
A project for computer vision and machine learning tasks.

**Planned Tech Stack:** TensorFlow, OpenCV, Python 3.14+

**Status:** Setup in progress

## Installation

Each project is a standalone Python package. Install dependencies using `uv` or `pip`:

```bash
# Install a single project
cd project_1
python -m pip install -e .

# Or using uv (faster)
uv sync
```

## Requirements

- **Python 3.14+**
- **uv** (recommended) or pip for package management
- API keys for AI services (Google Gemini, OpenAI) - store in `.env` files

## Environment Setup

Create `.env` files in the respective project directories with required API keys:

```
GOOGLE_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

## Development

Each project follows standard Python packaging conventions with:
- `pyproject.toml` for dependencies and metadata
- `src/` directory for source code
- Entry points defined via `[project.scripts]`

## Running Projects

- **Project 1:** `python project_1/test.py` or `ai-agent` (if installed)
- **Project 2:** `streamlit run ...` (after installation)
- **Project 3:** TBD

## Author

Sanchali-rif (sanchalisaha05@gmail.com)

## License

(Add your license here if applicable)
