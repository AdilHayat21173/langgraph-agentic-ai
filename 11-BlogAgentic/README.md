# Blog Agentic LangGraph

A FastAPI-based agentic blog generation system using LangGraph, Pydantic, and LLMs. This project demonstrates how to build a modular, extensible pipeline for generating, translating, and routing blog content using a graph-based workflow.

## Features
- **Blog Title and Content Generation**: Uses an LLM to generate creative, SEO-friendly blog titles and detailed content based on a user-provided topic.
- **Multi-language Translation**: Supports translation of blog content into multiple languages (Hindi, French, Thai, German, Italian, Portuguese, Spanish, etc.).
- **Graph-based Workflow**: Modular nodes for each step (title creation, content generation, translation, routing) managed by LangGraph.
- **API Endpoint**: Exposes a `/generate_blog` POST endpoint for easy integration.
- **Extensible Design**: Easily add new nodes or languages by extending the graph and node classes.

## Project Structure
```
├── app.py                        # FastAPI app entry point
├── requirements.txt              # Python dependencies
└── src/
    ├── graphs/
    │   └── graphbuilder.py       # GraphBuilder: builds and compiles the LangGraph workflow
    ├── llms/
    │   └── groqllm.py           # LLM wrapper (e.g., for Groq or OpenAI)
    ├── nodes/
    │   └── blognode.py          # BlogNode: all node logic (title, content, translation, routing)
    └── states/
        └── blogstate.py         # Pydantic models for state and blog
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd 11-BlogAgentic
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
# Or
source .venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the root directory and add your API keys (e.g., for LangSmith, Groq, or OpenAI):
```
langsmith_API_KEY=your_langsmith_api_key
# Add other keys as needed
```

### 5. Run the FastAPI Server
```sh
python app.py
```
The server will start at `http://127.0.0.1:8000`.

## API Usage

### POST `/generate_blog`
Generate a blog post for a given topic.

**Request Body (JSON):**
```
{
  "topic": "Your blog topic here"
}
```

**Response (JSON):**
```
{
  "data": {
    "topic": "...",
    "current_language": "english",
    "blog": {
      "title": "...",
      "content": "..."
    }
  }
}
```

## Customization
- **Add More Languages**: Extend the `route_decision` and `translation` methods in `BlogNode`.
- **Change LLM Provider**: Modify `src/llms/groqllm.py` to use your preferred LLM.
- **Add More Steps**: Add new nodes and edges in `GraphBuilder`.

## File Descriptions
- `app.py`: FastAPI app, loads environment, sets up API endpoint, builds and runs the graph.
- `src/graphs/graphbuilder.py`: Defines the graph structure and compiles it for execution.
- `src/nodes/blognode.py`: Contains all node logic for title creation, content generation, translation, and routing.
- `src/states/blogstate.py`: Pydantic models for the state and blog objects.
- `src/llms/groqllm.py`: LLM wrapper for invoking language models.

## Example Request (Python)
```python
import requests

url = "http://127.0.0.1:8000/generate_blog"
data = {"topic": "The future of AI in education"}
response = requests.post(url, json=data)
print(response.json())
```

## License
MIT License

## Credits
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Pydantic](https://docs.pydantic.dev/)
- [Your LLM Provider]
