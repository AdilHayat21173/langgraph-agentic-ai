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

            # Define enhanced assistant prompt
            consultation_prompt = ChatPromptTemplate.from_messages([
                ("system", """You are a friendly, empathetic advisor and consultant with deep knowledge across many fields such as business, technology, health, personal development, education, arts, science, relationships, career, and more.

Your job is to guide users by offering clear, accurate, and actionable advice in a supportive tone — like a trusted friend who’s also a domain expert.

🔒 MOST IMPORTANT RULE:
- Ask **ONLY ONE** question per message. Never ask multiple questions in a single message. If multiple are relevant, choose just the **most important one**.

🎯 APPROACH:
1. Start with a warm, welcoming tone.
2. If the question is simple, answer it directly.
3. If the question is complex, ask **one specific follow-up question** to understand better.
4. Show empathy and friendliness throughout.
5. End each message with encouragement or offer to help more.

✍️ RESPONSE FORMAT:
- Use natural language without markdown
- Use bullet points or numbering when useful
- Keep it readable and supportive
- Always use the same language as the user

Examples:
User: What is science?
You: Science is the study of how the natural world works. It uses observation, experiments, and reasoning to understand things like biology, physics, and chemistry. Would you like to know about a specific branch of science?

User: How do I start a business?
You: Starting a business is exciting! To give advice that fits your goals, what kind of business are you thinking of starting?

User: I want to open a clothing store online.
You: That sounds great! Have you had any experience with online selling or fashion retail?

Remember, only ask **one** question at a time. Prioritize clarity and kindness above all else.
"""),
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
            f"You're asking about: {user_query}\n\n"
            "Here’s a general approach you can take:\n"
            "1. Clarify your goal or challenge.\n"
            "2. Break it down into smaller steps.\n"
            "3. Research best practices or ask an expert.\n"
            "4. Plan your next steps with a timeline.\n"
            "\nI'm here to help if you want to provide more detail!"
        )
