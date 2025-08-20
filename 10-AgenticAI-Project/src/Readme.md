# AgenticLangGraph: AgenticAI Project

A modular, agentic AI application built with [LangChain](https://github.com/langchain-ai/langchain), [LangGraph](https://github.com/langchain-ai/langgraph), and [Streamlit](https://streamlit.io/). This project enables users to interact with LLMs (Large Language Models) for various use cases through a Streamlit-based UI.

---

## Features

- **Streamlit UI** for easy interaction
- **Configurable LLM backends** (e.g., Groq)
- **Graph-based agentic workflows** using LangGraph
- **Extensible use case selection**
- **Modular codebase** for easy customization

---

## Use Cases

- **Basic Chatbot:**  
  Ask any general question. The bot responds using only its built-in LLM knowledge (no web search).

- **Chatbot With Web:**  
  Ask questions and get answers that combine the LLM’s knowledge with up-to-date information from the web (e.g., Google search).

- **AI News:**  
  Search for the latest news about topics like LangChain, LangGraph, etc., using the Tavily API for real-time updates.

- **Consultant Bot:**  
  Ask for expert advice on any topic. The bot responds as a professional consultant, providing detailed and expert-level answers.

---

## Project Structure

```
10-AgenticAI-Project/
│
├── src/
│   ├── app.py
│   └── langgraphagenticai/
│       ├── main.py
│       ├── LLMS/
│       │   └── groqllm.py
│       ├── graph/
│       │   └── graph_builder.py
│       └── ui/
│           ├── uiconfigfile.py
│           └── streamlitui/
│               ├── loadui.py
│               └── display_result.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd 10-AgenticAI-Project
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application:**
    ```sh
    streamlit run src/app.py
    ```

---

## Configuration

- Edit `src/langgraphagenticai/ui/uiconfigfile.ini` to set LLM options, use cases, and page title.
- The UI and LLM behavior can be customized by modifying the files in `src/langgraphagenticai/ui/` and `src/langgraphagenticai/LLMS/`.

---

## Troubleshooting

- If you get `ModuleNotFoundError: No module named 'src'`, always run Streamlit from the project root directory.
- Ensure your virtual environment is activated before running any commands.
- For API-based features (like Tavily), ensure you have valid API keys set up as required.

---

## License

This project is for educational and research