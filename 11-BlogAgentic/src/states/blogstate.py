from typing import TypedDict, Optional
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(..., title="The title of the blog post")
    content: str = Field(..., title="The content of the blog post")

# Use TypedDict instead of BaseModel for state to allow mapping operations
class Blogstate(TypedDict):
    topic: str
    current_language: str
    blog: Optional[Blog]