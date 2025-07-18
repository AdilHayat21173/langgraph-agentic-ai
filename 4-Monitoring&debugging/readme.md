# LangGraph Agentic Workflow

A **Python project** demonstrating intelligent agentic workflows using **LangGraph**, with tool calling, Groq integration, and LangSmith monitoring for debugging.

## 🚀 Overview

This project creates an **agent** that:

* Processes user messages
* Calls external tools (web search, calculations, etc.)
* Handles tool responses
* Maintains conversation state
* Tracks executions in **LangSmith Dashboard**

## ✨ Features

* **Tool Integration**: Add tools with LLM binding
* **State Management**: Type-safe conversation state
* **Conditional Routing**: Decide when to call tools vs. LLM
* **Graph Visualization**: See workflows visually
* **Groq Integration**: Fast inference
* **LangSmith Monitoring**: Track and debug executions

## ⚙️ Installation

### 1️⃣ Clone the repository:

```bash
git clone <your-repo-url>
cd AGENTICLANGGRAPH
```

### 2️⃣ Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_key

# Optional LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=LangGraph-Agentic-Workflow
```

## 🚀 Quick Start

### Method 1: LangGraph Dev Server

```bash
cd "Monitoring&debugging"
langgraph dev
```

* **API**: http://127.0.0.1:2024
* **Studio UI**: [LangSmith Studio](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)
* **Docs**: http://127.0.0.1:2024/docs

### Method 2: Jupyter Notebook

```bash
jupyter notebook
# Open and run Monitoring&debugging/debugging.ipynb
```

## 📁 Project Structure

```
AGENTICLANGGRAPH/
├── .env
├── requirements.txt
├── main.py
├── Monitoring&debugging/
│   ├── agent_execution.py
│   ├── langgraph.json
│   ├── debugging.ipynb
```

## 🔧 Configuration

`Monitoring&debugging/langgraph.json`:

```json
{
  "dependencies": ["."],
  "graphs": {
    "graphbuilder": "agent_execution.py:initialize_agentic_graph"
  },
  "env": "../.env"
}
```

## 🩺 Monitoring and Debugging

Enable **LangSmith** for:

* Tracing executions
* Monitoring latency, token usage, and tool calls
* Debugging errors step-by-step

## 🆘 Troubleshooting

### ✅ **Module not found**:
* Ensure you are in the project root
* Check that paths in `langgraph.json` match the folder structure

### ✅ **Dev server issues**:
* Validate `.env` variables
* Confirm your Groq and LangSmith keys

### ✅ **Tool call issues**:
* Check if tool functions are properly registered in `agent_execution.py`

## 🎯 Next Steps

* Add more tools and memory
* Expand tests
* Deploy to production