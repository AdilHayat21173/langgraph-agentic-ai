# LangGraph with Tools: Quantum Computing & Machine Learning Workflow

This project demonstrates how to build a workflow using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain) tools to query research papers, Wikipedia, and Tavily search, and integrate them with an LLM (Groq) for advanced question answering.

---

## Features

- **Arxiv Search**: Query latest research papers from arxiv.org.
- **Wikipedia Search**: Fetch summaries and articles from Wikipedia.
- **Tavily Search**: Use Tavily for web search integration.
- **Groq LLM**: Bind all tools to a Groq LLM for multi-tool reasoning.
- **LangGraph Workflow**: Visualize and execute a stateful workflow using LangGraph.
- **Jupyter Notebook**: Interactive exploration and step-by-step execution.

---

## Requirements

- Python 3.11+
- [langchain](https://pypi.org/project/langchain/)
- [langgraph](https://pypi.org/project/langgraph/)
- [langchain-tavily](https://pypi.org/project/langchain-tavily/)
- [langchain-groq](https://pypi.org/project/langchain-groq/)
- [arxiv](https://pypi.org/project/arxiv/)
- [wikipedia](https://pypi.org/project/wikipedia/)
- [jupyter](https://pypi.org/project/jupyter/)
- [ipython](https://pypi.org/project/ipython/)
- [graphviz](https://graphviz.gitlab.io/download/)
- [pygraphviz](https://pypi.org/project/pygraphviz/) (optional, for advanced visualization)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for API key management)

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## Setup

1. **Clone this repository** and open the notebook `1-langgrapheithtools.ipynb` in Jupyter.

2. **Set your API keys**  
   Create a `.env` file in the project root with:
   ```
   Groq_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

3. **Install Graphviz (Windows users):**
   - Download and install from [Graphviz Downloads](https://graphviz.gitlab.io/download/).
   - Add Graphviz to your system PATH.

4. **(Optional) Install pygraphviz for advanced graph visualization:**
   - On Windows, use a pre-built wheel from [Gohlke's Unofficial Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz).

---

## Usage

- **Run the notebook cells step by step.**
- Query Arxiv, Wikipedia, and Tavily directly.
- Bind all tools to the Groq LLM and invoke complex queries.
- Visualize the workflow graph using Mermaid diagrams (if supported).
- See example queries at the end of the notebook.

---

## Example Queries

- "What is the latest research on quantum computing?"
- "What is the latest research on quantum computing and what is Machine learning?"
- "My name is Adil Hayat and give me the research on machine learning?"

---

## Troubleshooting

- **Graphviz/pygraphviz errors:**  
  Ensure Graphviz is installed and added to your PATH. Use pre-built wheels for pygraphviz if pip install fails.
- **API errors:**  
  Double-check your `.env` file and API key validity.
- **Deprecation warnings:**  
  Use `langchain_tavily` instead of deprecated `TavilySearchResults`.

---

## Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Groq](https://groq.com/)
- [Tavily](https://www.tavily.com/)
- [arxiv](https://arxiv.org/)
- [Wikipedia](https://wikipedia.org/)

---

## License

MIT