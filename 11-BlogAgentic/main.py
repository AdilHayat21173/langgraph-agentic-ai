from src.graphs.graphbuilder import GraphBuilder
from src.llms.groqllm import Groqllm
from dotenv import load_dotenv

load_dotenv()

def test_blog_generator(topic: str):
    groqllm = Groqllm()
    llm = groqllm.get_llm()

    graph_builder = GraphBuilder(llm)
    graph = graph_builder.setup_graph(usecase="topic")

    state = graph.invoke({
        "topic": topic,
        "current_language": "English",
        "blog": {"title": "", "content": ""}   # ✅ pass Blog dict
    })

    return state


if __name__ == "__main__":
    topic = input("Enter a topic: ")
    result = test_blog_generator(topic)
    print("\nGenerated Blog State:\n")
    print(result)
