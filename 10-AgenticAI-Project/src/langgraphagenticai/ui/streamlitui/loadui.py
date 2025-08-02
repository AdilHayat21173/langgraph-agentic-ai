import streamlit as st
import os

from langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Initialize GROQ API key session state
                if "GROQ_API_KEY" not in st.session_state:
                    st.session_state["GROQ_API_KEY"] = ""
                
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                
                # GROQ API Key input
                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "GROQ API Key", 
                    type="password",
                    value=st.session_state.get("GROQ_API_KEY", ""),
                    key="groq_api_input"
                )
                st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]
                
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer: https://console.groq.com/keys")
            
            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Cases", usecase_options)

            # Show TAVILY API key input for both Chatbot With Web and AI News
            if self.user_controls["selected_usecase"] == "Chatbot With Web" or self.user_controls["selected_usecase"] == "AI News":
                # Initialize TAVILY API key session state
                if "TAVILY_API_KEY" not in st.session_state:
                    st.session_state["TAVILY_API_KEY"] = ""
                
                # TAVILY API Key input
                tavily_key = st.text_input(
                    "TAVILY API KEY", 
                    type="password",
                    value=st.session_state.get("TAVILY_API_KEY", ""),
                    key="tavily_api_input",
                    help="Required for web search functionality"
                )
                
                # Update session state and user controls
                st.session_state["TAVILY_API_KEY"] = tavily_key
                self.user_controls["TAVILY_API_KEY"] = tavily_key
                
                # Set environment variable
                if tavily_key:
                    os.environ["TAVILY_API_KEY"] = tavily_key

                # Validate API key
                if not tavily_key:
                    st.warning("⚠️ Please enter your TAVILY API KEY to proceed. Don't have? refer: https://app.tavily.com/home")
                else:
                    st.success("✅ TAVILY API Key provided")

            # Add helpful information for AI News use case
            if self.user_controls["selected_usecase"] == "AI News":
                st.info("💡 **AI News Tips:**\n"
                        "- Ask: 'latest OpenAI news'\n"
                        "- Query: 'AI breakthroughs this week'\n"
                        "- Search: 'Google AI updates'\n"
                        "- General: 'artificial intelligence news'")

            # Add helpful information for Consultant Bot use case
            if self.user_controls["selected_usecase"] == "Consultant Bot":
                st.info("🎯 **Consultant Bot - Expert Advice:**\n"
                        "• **Business Strategy**: 'How to scale my startup?'\n"
                        "• **Technology**: 'Best practices for AI implementation'\n"
                        "• **Finance**: 'Investment strategy for small business'\n"
                        "• **Marketing**: 'Digital marketing plan for B2B'\n"
                        "• **Operations**: 'How to optimize supply chain?'\n"
                        "• **HR**: 'Building a remote team culture'\n\n"
                        "💡 **Tip**: Be specific about your industry, company size, and goals for better advice!")

        return self.user_controls
