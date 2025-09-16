# Gemini Mini

Gemini Mini is a Python-based AI coding agent that leverages the Gemini API to understand and execute tasks related to file manipulation and code execution. It can list files, read and write file content, and run Python scripts based on natural language prompts.

## Features

  * **File and Directory Listing**: List the contents of any directory within the project's workspace.
  * **File Content Reading**: Read the contents of any file within the workspace.
  * **File Content Writing**: Write or overwrite the contents of any file within the workspace.
  * **Python Code Execution**: Execute Python scripts with optional arguments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

  * Python 3.12 or higher
  * An API key for the Gemini API

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/gemini-mini.git
    cd gemini-mini
    ```
2.  **Install the dependencies:**
    The project uses `uv` for package management.
    ```bash
    pip install uv
    uv sync
    ```
3.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

You can run the agent from the command line by passing a prompt as an argument. The agent will then generate a plan and execute the necessary functions to fulfill your request.

### Example

To run the calculator example and see the result of the calculation in `calculator/main.py`:

```bash
python main.py "run the calculator's main.py"
```

To see a more detailed output of the agent's execution, you can use the `--verbose` flag:

```bash
python main.py "run the calculator's main.py" --verbose
```

## Project Structure

```
.
├── calculator/
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── functions/
│   ├── call_function.py
│   ├── config.py
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file_content.py
├── .gitignore
├── available_functions.py
├── main.py
├── prompts.py
├── pyproject.toml
└── uv.lock
```

  * `main.py`: The main entry point for the AI agent.
  * `prompts.py`: Contains the system prompt that instructs the Gemini model on how to behave.
  * `available_functions.py`: Defines the functions available to the Gemini model.
  * `functions/`: Contains the implementation of the functions that the agent can call.
  * `calculator/`: An example project that the agent can interact with.
