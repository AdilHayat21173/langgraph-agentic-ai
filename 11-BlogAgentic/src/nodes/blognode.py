# # from src.states.blogstate import Blogstate, Blog
# # from langchain_core.messages import SystemMessage, HumanMessage

# # class BlogNode:
# #     """
# #     A class representing a node in the blog generation graph.
# #     """
    
# #     def __init__(self, llm):
# #         self.llm = llm
    
# #     def title_creation(self, state: Blogstate):
# #         """
# #         create the title for the blog
# #         """
# #         if "topic" in state and state["topic"]:
# #             prompt = """
# #                    You are an expert blog content writer. Use Markdown formatting. Generate
# #                    a blog title for the {topic}. This title should be creative and SEO friendly
# #                    """
            
# #             system_message = prompt.format(topic=state["topic"])
# #             print(system_message)
# #             response = self.llm.invoke(system_message)
# #             print(response)
# #             return {"blog": Blog(title=response.content, content="")}
    
# #     def content_generation(self, state: Blogstate):
# #         if "topic" in state and state["topic"]:
# #             system_prompt = """You are expert blog writer. Use Markdown formatting.
# #             Generate a detailed blog content with detailed breakdown for the {topic}"""
# #             system_message = system_prompt.format(topic=state["topic"])
# #             response = self.llm.invoke(system_message)
# #             return {"blog": Blog(title=state["blog"].title, content=response.content)}
    
# #     def translation(self, state: Blogstate):
# #         """
# #         Translate the content to the specified language.
# #         """
# #         translation_prompt = """
# #         Translate the following content into {current_language}.
# #         - Maintain the original tone, style, and formatting.
# #         - Adapt cultural references and idioms to be appropriate for {current_language}.

# #         ORIGINAL CONTENT:
# #         {blog_content}

# #         """
# #         print(state["current_language"])
# #         blog_content = state["blog"].content
# #         messages = [
# #             HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))
# #         ]
# #         translation_content = self.llm.with_structured_output(Blog).invoke(messages)
# #         return {"blog": translation_content}
    
# #     def route(self, state: Blogstate):
# #         return {"current_language": state["current_language"]}
    
# #     def route_decision(self, state: Blogstate):
# #         """
# #         Route the content to the respective translation function.
# #         """
# #         language = state["current_language"].lower()
        
# #         if language == "hindi":
# #             return "hindi"
# #         elif language == "french":
# #             return "french"
# #         elif language == "thai":
# #             return "thai"
# #         elif language == "german":
# #             return "german"
# #         elif language == "italian":
# #             return "italian"
# #         elif language == "portuguese":
# #             return "portuguese"
# #         elif language == "spanish":
# #             return "spanish"
# #         else:
# #             return language

# from src.states.blogstate import Blogstate, Blog
# from langchain_core.messages import SystemMessage, HumanMessage

# class BlogNode:
#     """
#     A class representing a node in the blog generation graph.
#     """
    
#     def __init__(self, llm):
#         self.llm = llm
    
#     def title_creation(self, state: Blogstate):
#         """
#         create the title for the blog
#         """
#         if "topic" in state and state["topic"]:
#             prompt = """
#                    You are an expert blog content writer. Use Markdown formatting. Generate
#                    a blog title for the {topic}. This title should be creative and SEO friendly
#                    """
            
#             system_message = prompt.format(topic=state["topic"])
#             print(system_message)
#             response = self.llm.invoke(system_message)
#             print(response)
#             return {"blog": Blog(title=response.content, content="")}
    
#     def content_generation(self, state: Blogstate):
#         if "topic" in state and state["topic"]:
#             system_prompt = """You are expert blog writer. Use Markdown formatting.
#             Generate a detailed blog content with detailed breakdown for the {topic}"""
#             system_message = system_prompt.format(topic=state["topic"])
#             response = self.llm.invoke(system_message)
#             return {"blog": Blog(title=state["blog"].title, content=response.content)}
    
#     def translation(self, state: Blogstate):
#         """
#         Translate the content to the specified language.
#         """
#         translation_prompt = """
#         Translate the following content into {current_language}.
#         - Maintain the original tone, style, and formatting.
#         - Adapt cultural references and idioms to be appropriate for {current_language}.
#         - Return ONLY the translated content without any additional explanations.

#         ORIGINAL CONTENT:
#         {blog_content}

#         """
#         print(state["current_language"])
#         blog_content = state["blog"].content
#         messages = [
#             HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))
#         ]
#         # Removed structured output since llama3-70b-8192 doesn't support it
#         response = self.llm.invoke(messages)
#         # Create Blog object manually with original title and translated content
#         translated_blog = Blog(title=state["blog"].title, content=response.content)
#         return {"blog": translated_blog}
    
#     def route(self, state: Blogstate):
#         return {"current_language": state["current_language"]}
    
#     def route_decision(self, state: Blogstate):
#         """
#         Route the content to the respective translation function.
#         """
#         language = state["current_language"].lower()
        
#         if language == "hindi":
#             return "hindi"
#         elif language == "french":
#             return "french"
#         elif language == "thai":
#             return "thai"
#         elif language == "german":
#             return "german"
#         elif language == "italian":
#             return "italian"
#         elif language == "portuguese":
#             return "portuguese"
#         elif language == "spanish":
#             return "spanish"
#         else:
#             return language

from src.states.blogstate import Blogstate, Blog
from langchain_core.messages import SystemMessage, HumanMessage

class BlogNode:
    """
    A class representing a node in the blog generation graph.
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def title_creation(self, state: Blogstate):
        """
        create the title for the blog
        """
        if "topic" in state and state["topic"]:
            prompt = """
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly
                   """
            
            system_message = prompt.format(topic=state["topic"])
            print(system_message)
            response = self.llm.invoke(system_message)
            print(response)
            return {"blog": Blog(title=response.content, content="")}
    
    def content_generation(self, state: Blogstate):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": Blog(title=state["blog"].title, content=response.content)}
    
    def translation(self, state: Blogstate):
        """
        Translate the content to the specified language.
        """
        # First translate the title
        title_translation_prompt = """
        Translate the following title into {current_language}.
        - Maintain the original meaning and SEO-friendly nature.
        - Return ONLY the translated title without any additional text.

        TITLE TO TRANSLATE:
        {blog_title}
        """
        
        title_messages = [
            HumanMessage(title_translation_prompt.format(
                current_language=state["current_language"], 
                blog_title=state["blog"].title
            ))
        ]
        translated_title_response = self.llm.invoke(title_messages)
        
        # Then translate the content
        content_translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.
        - Return ONLY the translated content without any additional explanations.

        ORIGINAL CONTENT:
        {blog_content}
        """
        
        print(state["current_language"])
        blog_content = state["blog"].content
        content_messages = [
            HumanMessage(content_translation_prompt.format(
                current_language=state["current_language"], 
                blog_content=blog_content
            ))
        ]
        translated_content_response = self.llm.invoke(content_messages)
        
        # Create Blog object with both translated title and content
        translated_blog = Blog(
            title=translated_title_response.content.strip(),
            content=translated_content_response.content.strip()
        )
        return {"blog": translated_blog}
    
    def route(self, state: Blogstate):
        return {"current_language": state["current_language"]}
    
    def route_decision(self, state: Blogstate):
        """
        Route the content to the respective translation function.
        """
        language = state["current_language"].lower()
        
        if language == "hindi":
            return "hindi"
        elif language == "french":
            return "french"
        elif language == "thai":
            return "thai"
        elif language == "german":
            return "german"
        elif language == "italian":
            return "italian"
        elif language == "portuguese":
            return "portuguese"
        elif language == "spanish":
            return "spanish"
        else:
            return language