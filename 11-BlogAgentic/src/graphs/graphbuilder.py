from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import Groqllm
from src.states.blogstate import Blogstate
from src.nodes.blognode import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(Blogstate)
        self.blog_node_obj = BlogNode(llm)

    def build_topic_graph(self):
        """
        Build a graph to generate a blog based on topic
        """
        
        ## nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        ##Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph

    def build_language_graph(self):
        """
        Build a graph for blog generation with inputs topic and language
        """
        self.blog_node_obj = BlogNode(self.llm)
        print(self.llm)
        
        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        # Fixed: Remove lambda functions that cause mapping issues
        self.graph.add_node("hindi_translation", self.blog_node_obj.translation)
        self.graph.add_node("french_translation", self.blog_node_obj.translation)
        self.graph.add_node("thai_translation", self.blog_node_obj.translation)
        self.graph.add_node("german_translation", self.blog_node_obj.translation)
        self.graph.add_node("italian_translation", self.blog_node_obj.translation)
        self.graph.add_node("portuguese_translation", self.blog_node_obj.translation)
        self.graph.add_node("spanish_translation", self.blog_node_obj.translation)

        self.graph.add_node("route", self.blog_node_obj.route)

        ## edges and conditional edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        ## conditional edge
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation",
                "thai": "thai_translation",
                "german": "german_translation",
                "italian": "italian_translation",
                "portuguese": "portuguese_translation",
                "spanish": "spanish_translation"
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        self.graph.add_edge("thai_translation", END)
        self.graph.add_edge("german_translation", END)
        self.graph.add_edge("italian_translation", END)
        self.graph.add_edge("portuguese_translation", END)
        self.graph.add_edge("spanish_translation", END)
        
        return self.graph

    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()

        if usecase == "language":
            self.build_language_graph()

        return self.graph.compile()


## Below code is for the langsmith langgraph studio
llm = Groqllm().get_llm()

## get the graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_topic_graph().compile()