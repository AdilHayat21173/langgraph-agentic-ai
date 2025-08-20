import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graphbuilder import GraphBuilder
from src.llms.groqllm import Groqllm
from src.states.blogstate import Blogstate
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

print(os.getenv("langsmith_API_KEY"))

os.environ["LANGSMITH_API_KEY"]=os.getenv("langsmith_API_KEY")


@app.post("/blogs")
async def create_blogs(request:Request):
    
    data=await request.json()
    topic= data.get("topic","")
    language = data.get("language", '')
    print(language)

    ## get the llm object

    groqllm=Groqllm()
    llm=groqllm.get_llm()

    ## get the graph
    graph_builder=GraphBuilder(llm)
    
    if topic and language:
        graph=graph_builder.setup_graph(usecase="language")
        state=graph.invoke({"topic":topic,"current_language":language.lower()})

    elif topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state=graph.invoke({"topic":topic})
    

    return {"data":state}

if __name__ == "__main__":
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)