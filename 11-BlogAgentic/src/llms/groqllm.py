# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# class Groqllm:
#     def __init__(self):
#         load_dotenv()
    
#     def get_llm(self):
#         try:
#             os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
#             llm = ChatGroq(api_key=self.groq_api_key,model="deepseek-r1-distill-llama-70b")
#             return llm

#         except Exception as e:
#             raise ValueError(f"Error occurred with exception :{e}")


from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class Groqllm:
    def __init__(self):
        load_dotenv()
        # Initialize groq_api_key in __init__
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        
    def get_llm(self):
        try:
            if not self.groq_api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")
            
            os.environ["GROQ_API_KEY"] = self.groq_api_key
            # Return the LLM client
            return ChatGroq(api_key=self.groq_api_key, model="llama3-70b-8192")
        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")


