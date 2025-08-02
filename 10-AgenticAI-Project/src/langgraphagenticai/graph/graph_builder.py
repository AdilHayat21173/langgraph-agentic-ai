
from langgraph.graph import StateGraph
from langgraphagenticai.state.state import State
from langgraph.graph import START,END
from langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode
from langgraphagenticai.nodes.ai_news_node import AINewsNode
from langgraphagenticai.nodes.consultant_bot_node import ConsultantBotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node=BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)

        ## Define the LLM
        llm=self.llm

        ## Define the chatbot node

        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        ## Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
    
    

    def ai_news_builder_graph(self):

        ai_news_node=AINewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)

        #added the edges

        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news", END)

    
    
    def consultant_bot_build_graph(self):
        """
        Builds a consultant bot graph for providing expert advice.
        This method creates a single-node graph that provides comprehensive
        consultation responses across various business and technical domains.
        """
        consultant_node = ConsultantBotNode(self.llm)
    
        # Add the consultation node
        self.graph_builder.add_node("consultant", consultant_node.provide_consultation)
    
        # Add edges
        self.graph_builder.add_edge(START, "consultant")
        self.graph_builder.add_edge("consultant", END)


  


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()
        elif usecase == "AI News":
            self.ai_news_builder_graph()
        
        elif usecase == "Consultant Bot":
            self.consultant_bot_build_graph()

        return self.graph_builder.compile()