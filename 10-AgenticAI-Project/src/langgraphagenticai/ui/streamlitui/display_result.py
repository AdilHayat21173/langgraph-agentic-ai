import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages': ("user", user_message)}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

        elif usecase == "Chatbot With Web":
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)

            for message in res.get('messages', []):
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.chat_message("ai"):
                        st.write("🔧 Tool Call Start")
                        st.write(message.content)
                        st.write("🔧 Tool Call End")
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            # Display user message
            with st.chat_message("user"):
                st.write(user_message)

            with st.spinner("Fetching and summarizing news... ⏳"):
                try:
                    # Invoke the graph with proper state format
                    initial_state = {"messages": [HumanMessage(content=user_message)]}
                    result = graph.invoke(initial_state)
                    
                    # Debug: Print result structure (remove in production)
                    print(f"AI News Result Type: {type(result)}")
                    print(f"AI News Result Keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
                    
                    # Extract summary content
                    summary_content = None
                    
                    if isinstance(result, dict):
                        # First priority: Check for 'summary' key (most likely)
                        if "summary" in result and result["summary"]:
                            summary_content = result["summary"]
                            print("Found summary in 'summary' key")
                        
                        # Second priority: Check all keys for string content
                        elif not summary_content:
                            for key, value in result.items():
                                if isinstance(value, str) and len(value) > 100:
                                    summary_content = value
                                    print(f"Found summary in '{key}' key")
                                    break
                        
                        # Third priority: Check messages for AIMessage (last resort)
                        if not summary_content and "messages" in result and isinstance(result["messages"], list):
                            for msg in result["messages"]:
                                if isinstance(msg, AIMessage) and msg.content and len(msg.content) > 100:
                                    summary_content = msg.content
                                    print("Found summary in AIMessage")
                                    break
                    
                    # Display the result
                    if summary_content and summary_content.strip():
                        with st.chat_message("assistant"):
                            st.markdown(summary_content, unsafe_allow_html=True)
                    else:
                        with st.chat_message("assistant"):
                            st.warning("🔍 No news summary was generated. This could be due to:")
                            st.write("• No recent news found for your query")
                            st.write("• TAVILY API rate limits")
                            st.write("• Temporary service issues")
                            st.write("\n💡 **Try:**")
                            st.write("• A more specific query (e.g., 'OpenAI GPT-4 news')")
                            st.write("• A broader query (e.g., 'AI technology news')")
                            st.write("• Waiting a moment and trying again")
                            
                            # Show debug info for troubleshooting
                            if isinstance(result, dict):
                                st.write(f"\n🔧 **Debug Info:** Available keys: {list(result.keys())}")

                except Exception as e:
                    with st.chat_message("assistant"):
                        st.error(f"❌ **Error occurred:** {str(e)}")
                        st.write("**Troubleshooting steps:**")
                        st.write("1. Check your TAVILY API key")
                        st.write("2. Verify your internet connection")
                        st.write("3. Try a simpler query")
                        st.write("4. Wait a moment and try again")
                    
                    # Print full error for debugging
                    print(f"AI News Error: {e}")
                    import traceback
                    traceback.print_exc()

        elif usecase == "Consultant Bot":
            # Display user message
            with st.chat_message("user"):
                st.write(user_message)

            with st.spinner("Preparing your consultation... 🤔"):
                try:
                    # Invoke the graph with proper state format
                    initial_state = {"messages": [HumanMessage(content=user_message)]}
                    result = graph.invoke(initial_state)
                    
                    # Debug: Print result structure
                    print(f"Consultant Bot Result Type: {type(result)}")
                    print(f"Consultant Bot Result Keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
                    
                    # Extract consultation content
                    consultation_content = None
                    
                    if isinstance(result, dict):
                        if "consultation" in result and result["consultation"]:
                            consultation_content = result["consultation"]
                            print("Found consultation in 'consultation' key")
                        else:
                            # Fallback: check other keys for substantial content
                            for key, value in result.items():
                                if isinstance(value, str) and len(value) > 100:
                                    consultation_content = value
                                    print(f"Found consultation in '{key}' key")
                                    break
                    
                    # Display the consultation
                    if consultation_content and consultation_content.strip():
                        with st.chat_message("assistant"):
                            st.markdown(consultation_content, unsafe_allow_html=True)
                    else:
                        with st.chat_message("assistant"):
                            st.warning("🤔 Unable to generate consultation at this time.")
                            st.write("**Please try:**")
                            st.write("• Rephrasing your question more specifically")
                            st.write("• Providing more context about your situation")
                            st.write("• Breaking down complex questions into smaller parts")
                            st.write("• Specifying your industry or domain")
                            
                            if isinstance(result, dict):
                                st.write(f"\n🔧 **Debug Info:** Available keys: {list(result.keys())}")

                except Exception as e:
                    with st.chat_message("assistant"):
                        st.error(f"❌ **Consultation Error:** {str(e)}")
                        st.write("**Troubleshooting steps:**")
                        st.write("1. Check your internet connection")
                        st.write("2. Try a simpler question")
                        st.write("3. Ensure your query is clear and specific")
                        st.write("4. Wait a moment and try again")
                    
                    print(f"Consultant Bot Error: {e}")
                    import traceback
                    traceback.print_exc()