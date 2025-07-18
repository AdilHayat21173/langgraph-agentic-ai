from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END, START, add_messages
from langgraph.graph.state import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

def initialize_agentic_graph():
    """Initialize the LangGraph agentic workflow and return the compiled graph."""

    load_dotenv()

    # Set environment variables for Groq and LangSmith
    os.environ["GROQ_API_KEY"] = os.getenv("Groq_API_KEY")
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LangSmith_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "agenticlanggraph"

    # Initialize the LLM
    llm = ChatGroq(model="deepseek-r1-distill-llama-70b")

    # Define the conversation state
    class State(TypedDict):
        messages: Annotated[list[BaseMessage], add_messages]

    # Define your tools
    @tool
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    tools = [add]
    llm_with_tools = llm.bind_tools(tools)

    # Define tool-calling logic
    def tool_calling_llm(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Build the workflow graph
    graph = StateGraph(State)
    graph.add_node("tool_calling_llm", tool_calling_llm)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge(START, "tool_calling_llm")
    graph.add_conditional_edges("tool_calling_llm", tools_condition)
    graph.add_edge("tools", END)

    # Compile and return the graph
    graphbuilder = graph.compile()
    return graphbuilder



graphbuilder = initialize_agentic_graph()
