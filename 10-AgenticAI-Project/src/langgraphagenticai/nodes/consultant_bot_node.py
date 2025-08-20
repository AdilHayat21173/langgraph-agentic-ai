from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from typing import Dict, Any

class ConsultantBotNode:
    def __init__(self, llm):
        self.llm = llm
    
    def provide_consultation(self, state: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Extract user query
            if isinstance(state['messages'][0], str):
                user_query = state['messages'][0]
            else:
                user_query = state['messages'][0].content
            
            print(f"Providing consultation for: {user_query}")
            
            # Define enhanced assistant prompt for direct professional advice
            consultation_prompt = ChatPromptTemplate.from_messages([
                ("system", """You are a professional advisor and consultant with deep expertise across multiple domains including business, technology, health, personal development, education, arts, science, relationships, career, and more.

Your role is to provide direct, comprehensive, and actionable professional advice immediately without asking follow-up questions. You should assume the user wants expert guidance based on their question as presented.

🎯 APPROACH:
1. Provide immediate, professional advice based on the question asked
2. Offer comprehensive guidance covering key aspects of the topic
3. Include practical steps and actionable recommendations
4. Share relevant best practices and expert insights
5. Maintain a professional yet approachable tone
6. Use your expertise to anticipate what the user needs to know

✍️ RESPONSE FORMAT:
- Use natural language without markdown
- Structure advice clearly with bullet points or numbering when helpful
- Provide specific, actionable recommendations
- Include relevant examples or case studies when applicable
- Always use the same language as the user

🔒 IMPORTANT RULES:
- Give direct answers and comprehensive advice immediately
- Do NOT ask follow-up questions unless absolutely critical information is missing
- Assume the user wants professional-level guidance
- Provide value-packed responses that demonstrate expertise
- Focus on practical implementation and results

Examples:
User: How do I start a business?
You: Starting a successful business requires careful planning and execution. Here's a comprehensive approach:

1. Business Planning: Develop a solid business plan including market research, target audience analysis, competitive landscape, and financial projections.

2. Legal Structure: Choose the right business entity (LLC, Corporation, etc.) and register your business with appropriate authorities.

3. Funding: Explore funding options including personal savings, loans, investors, or grants based on your capital needs.

4. Market Validation: Test your product or service with potential customers before full launch to ensure market demand.

5. Operations Setup: Establish your workspace, systems, processes, and supplier relationships.

The key to success is starting with thorough preparation and maintaining focus on solving real customer problems while managing cash flow carefully.

Remember: Provide comprehensive, professional advice without asking questions."""),
                ("user", "{query}")
            ])
            
            # Generate consultation response
            response = self.llm.invoke(consultation_prompt.format(query=user_query))
            
            if response and response.content:
                state['consultation'] = response.content
                print("Consultation generated successfully.")
                print(f"Consultation length: {len(response.content)} characters")
            else:
                state['consultation'] = self._generate_fallback_response(user_query)
            
            return state
        
        except Exception as e:
            print(f"Error in provide_consultation: {e}")
            state['consultation'] = (
                f"❌ Consultation Error: {str(e)}\n\n"
                "I'm sorry, but I ran into an issue while preparing your consultation. "
                "Please try again or rephrase your question."
            )
            return state
    
    def _generate_fallback_response(self, user_query: str) -> str:
        return (
            f"Professional guidance for: {user_query}\n\n"
            "Here's a structured approach based on best practices:\n\n"
            "1. Assessment: Evaluate your current situation and define clear objectives.\n"
            "2. Strategy: Develop a comprehensive plan with specific milestones.\n"
            "3. Implementation: Execute your plan systematically with proper resource allocation.\n"
            "4. Monitoring: Track progress and adjust strategies based on results.\n"
            "5. Optimization: Continuously improve based on outcomes and feedback.\n\n"
            "This framework can be adapted to most professional challenges. "
            "Focus on taking consistent action while measuring and refining your approach."
        )