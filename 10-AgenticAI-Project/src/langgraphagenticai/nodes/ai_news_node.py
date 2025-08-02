# from tavily import TavilyClient
# from langchain_core.prompts import ChatPromptTemplate

# class AINewsNode:
#     def __init__(self,llm):
#         """
#         Initialize the AINewsNode with API keys for Tavily and GROQ.
#         """
#         self.tavily = TavilyClient()
#         self.llm = llm
#         self.state = {}

#     def fetch_news(self, state: dict) -> dict:
#         """
#         Fetch AI news based on the user's query.
        
#         Args:
#             state (dict): The state dictionary containing 'messages' with user query.
        
#         Returns:
#             dict: Updated state with 'news_data' key containing fetched news.
#         """
#         user_query = state['messages'][0].content
#         self.state['query'] = user_query
        
#         response = self.tavily.search(
#             query=user_query,
#             topic="news",
#             include_answer="advanced",
#             max_results=20,
#             # You can adjust these parameters as needed
#         )

#         state['news_data'] = response.get('results', [])
#         self.state['news_data'] = state['news_data']
#         return state
    
#     def summarize_news(self, state: dict) -> dict:
#         """
#         Summarize the fetched news using an LLM.
#         """
#         news_items = self.state['news_data']
#         user_query = self.state['query']

#         prompt_template = ChatPromptTemplate.from_messages([
#             ("system", f"""Summarize news articles about '{user_query}' into markdown format. For each item include:
#             - Date in **YYYY-MM-DD** format in IST timezone
#             - Concise sentences summary from latest news
#             - Sort news by date wise (latest first)
#             - Source URL as link
#             Use format:
#             ### [Date]
#             - [Summary](URL)"""),
#             ("user", "Articles:\n{articles}")
#         ])

#         articles_str = "\n\n".join([
#             f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
#             for item in news_items
#         ])

#         response = self.llm.invoke(prompt_template.format(articles=articles_str))
#         state['summary'] = response.content
#         self.state['summary'] = state['summary']
#         return state
    

from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self, llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ.
        """
        self.tavily = TavilyClient()
        self.llm = llm

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the user's query.
        
        Args:
            state (dict): The state dictionary containing 'messages' with user query.
        
        Returns:
            dict: Updated state with 'news_data' key containing fetched news.
        """
        try:
            # Extract user query from messages
            if isinstance(state['messages'][0], str):
                user_query = state['messages'][0]
            else:
                user_query = state['messages'][0].content
            
            print(f"Fetching news for query: {user_query}")
            
            # Enhanced query for better AI news results
            enhanced_query = f"AI artificial intelligence {user_query} news technology"
            
            response = self.tavily.search(
                query=enhanced_query,
                topic="news",
                include_answer="advanced",
                max_results=15,
                days=7,  # Last 7 days for recent news
                include_domains=None  # Let Tavily choose the best sources
            )

            news_results = response.get('results', [])
            print(f"Found {len(news_results)} news articles")
            
            # Store both in state for the next node
            state['news_data'] = news_results
            state['user_query'] = user_query
            
            return state
            
        except Exception as e:
            print(f"Error in fetch_news: {e}")
            state['news_data'] = []
            state['user_query'] = user_query if 'user_query' in locals() else "AI news"
            state['error'] = f"Failed to fetch news: {str(e)}"
            return state
    
    def summarize_news(self, state: dict) -> dict:
        """
        Summarize the fetched news using an LLM.
        
        Args:
            state (dict): The state dictionary containing 'news_data' and 'user_query'.
        
        Returns:
            dict: Updated state with 'summary' key containing the summarized news.
        """
        try:
            news_items = state.get('news_data', [])
            user_query = state.get('user_query', 'AI news')
            
            # Check if there was an error in fetching
            if 'error' in state:
                state['summary'] = f"❌ {state['error']}\n\nPlease check your TAVILY API key and try again."
                return state
            
            # Check if we have news items
            if not news_items:
                state['summary'] = f"🔍 No recent news found for: **{user_query}**\n\n" \
                                 f"Try these suggestions:\n" \
                                 f"• Use more specific terms (e.g., 'OpenAI GPT news')\n" \
                                 f"• Try broader terms (e.g., 'AI technology news')\n" \
                                 f"• Check for recent developments in the last week"
                return state

            print(f"Summarizing {len(news_items)} news articles")

            # Create a comprehensive prompt for better summarization
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", f"""You are an expert AI news summarizer. Create a comprehensive summary of news articles about '{user_query}' in markdown format.

                Structure your response as follows:
                
                # 🤖 AI News Summary: {user_query}
                
                ## 📋 Overview
                [Brief 2-3 sentence overview of the main themes and developments]
                
                ## 🔥 Key Highlights
                [List 5-7 most important points with bullet points. Include dates when available]
                
                ## 📰 Recent Articles
                [For each major article, provide:
                - **[Article Title]** - [Date if available]
                  - Brief summary (2-3 sentences)
                  - [Link to article](URL)
                ]
                
                ## 🎯 Key Takeaways
                [2-3 main insights or implications]
                
                Guidelines:
                - Use engaging emojis for section headers
                - Include dates in DD/MM/YYYY format when available
                - Focus on the most recent and relevant information
                - Make links clickable with proper markdown formatting
                - Keep summaries concise but informative
                """),
                ("user", "News articles to summarize:\n\n{articles}")
            ])

            # Format articles for the prompt
            articles_str = ""
            for i, item in enumerate(news_items[:10], 1):  # Limit to top 10 articles
                title = item.get('title', 'No title')
                content = item.get('content', 'No content')[:500]  # Limit content length
                url = item.get('url', 'No URL')
                date = item.get('published_date', 'No date')
                score = item.get('score', 0)
                
                articles_str += f"Article {i}:\n"
                articles_str += f"Title: {title}\n"
                articles_str += f"Content: {content}\n"
                articles_str += f"URL: {url}\n"
                articles_str += f"Date: {date}\n"
                articles_str += f"Relevance Score: {score}\n\n"

            # Generate summary
            response = self.llm.invoke(prompt_template.format(articles=articles_str))
            
            if response and response.content:
                state['summary'] = response.content
                print("Summary generated successfully")
            else:
                state['summary'] = f"⚠️ Failed to generate summary for: **{user_query}**\n\n" \
                                 f"Found {len(news_items)} articles but couldn't process them. " \
                                 f"Please try a different query or check back later."
            
            return state
            
        except Exception as e:
            print(f"Error in summarize_news: {e}")
            state['summary'] = f"❌ Error generating summary: {str(e)}\n\n" \
                             f"Please try again or contact support if the issue persists."
            return state