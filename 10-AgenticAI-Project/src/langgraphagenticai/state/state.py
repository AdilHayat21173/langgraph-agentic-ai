from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated, Optional


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List, add_messages]
    
    # Additional fields for AI News functionality
    news_data: Optional[List[dict]]  # For storing fetched news articles
    user_query: Optional[str]        # For storing the user's query
    summary: Optional[str]           # For storing the generated summary
    error: Optional[str]             # For storing any error messages
    
    # Additional field for Consultant Bot functionality
    consultation: Optional[str]      # For storing consultation responses