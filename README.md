# AI Agent

A small Python project demonstrating a LangChain-based AI agent using Google Gemini.

## Overview

This project includes a simple conversational agent with a few tools such as calculator and greeting support.

## Requirements

- Python 3.14+
- `langchain`, `langchain-google-genai`, `langchain-openai`, `langgraph`, `python-dotenv`
- A `.env` file for any required API keys

## Install

From the repository root:

```bash
python -m pip install -e project_1
```

Or install requirements directly from `project_1/pyproject.toml`.

## Run

To start the example agent:

```bash
python project_1/test.py
```

If the package is installed, you can also run:

```bash
ai-agent
```

## Notes

- The example loads environment variables with `python-dotenv`.
- Customize or extend tools in `project_1/test.py`.
