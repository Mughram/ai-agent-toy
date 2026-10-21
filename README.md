# AI Agent Toy

A simple AI coding agent built with Python as part of the [Build an AI Agent](https://www.boot.dev/courses/build-ai-agent-python) course on Boot.dev.

The project explores how AI coding agents work using LLM APIs, function calling, and an agent loop. It can inspect files, read and write code, and execute Python programs within a configured working directory.

## Features

- **File Listing** — List files and directories
- **File Reading** — Read file contents
- **File Writing** — Create or overwrite files
- **Code Execution** — Run Python files with optional arguments
- **Function Calling** — Allow the LLM to select and execute tools
- **Agent Loop** — Process tool results and continue until a final response is generated
- **Verbose Mode** — Display tool calls and token usage

## Tech Stack

- Python 3.13+
- OpenAI Python SDK
- OpenRouter API
- uv
- python-dotenv

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mughram/ai-agent-toy.git
cd ai-agent-toy
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get an API key from [OpenRouter](https://openrouter.ai/).

### 4. Run the agent

```bash
uv run main.py "List the files in the calculator directory"
```

To see tool calls and token usage:

```bash
uv run main.py "Run main.py and show me the output" --verbose
```

## How It Works

1. The user provides a prompt through the CLI.
2. The prompt and available tools are sent to the LLM through OpenRouter.
3. The model decides whether to respond directly or call a tool.
4. Requested tools are executed locally, and their results are added to the conversation.
5. The process repeats until the model returns a final response or reaches the 20-iteration limit.

## Project Structure

```text
ai-agent-toy/
├── calculator/          # Working directory
├── functions/           # File operations and Python execution
├── main.py              # CLI entry point and agent loop
├── call_function.py     # Tool registration and execution
├── prompts.py           # Agent system prompt
├── config.py            # Working directory and configuration
└── pyproject.toml       # Project dependencies
```

## Limitations

- This is a learning project, not a production-ready coding agent.
- The agent currently uses a configured OpenRouter model.
- The agent loop is limited to 20 iterations.
- File operations are intended to stay within the configured working directory.
- Python execution can run potentially unsafe code. Use only in a trusted, isolated environment.

## Acknowledgments

Built as part of the [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python) course by [Boot.dev](https://www.boot.dev/).

## Author

[Mughram Ayashi](https://github.com/Mughram)
