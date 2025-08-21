# AGENTICLANGGRAPH

A comprehensive exploration of advanced conversational AI workflows using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and modern LLM tools. This project demonstrates modular, agentic, and extensible chatbot and workflow patterns, including RAG, multi-agent collaboration, tool integration, and advanced debugging/monitoring.

---

## Table of Contents

1. [LangGraph Component: Pydantic Chain & Streaming](#1-langgraph-component-pydantic-chain--streaming)
2. [Basic Chatbot in LangGraph](#2-basic-chatbot-in-langgraph)
3. [LangGraph with Tools (Tavily, Arxiv, Wiki, etc.)](#3-langgraph-with-tools)
4. [Monitoring & Debugging (LangSmith, LangGraph Dev)](#4-monitoring--debugging)
5. [LangGraph Debugging (LangGraph Dev)](#5-langgraph-debugging)
6. [Workflow Patterns: Prompt Chaining, Parallelization, Routing, Orchestration, Evaluation](#6-workflow-patterns)
7. [Human Feedback Integration](#7-human-feedback-integration)
8. [RAG: Agentic, Corrective, Adaptive](#8-rag-agentic-corrective-adaptive)
9. [Multi-Agent Collaboration](#9-multi-agent-collaboration)
10. [AgenticAI Project: Use Cases](#10-agenticai-project-use-cases)
11. [BlogAgentic: Blog Generation & Translation](#11-blogagentic-blog-generation--translation)

---

## 1. LangGraph Component: Pydantic Chain & Streaming

- **Goal:** Explore how to use Pydantic models for structured state management in LangGraph.
- **Streaming:** Demonstrates real-time streaming of LLM outputs within a LangGraph workflow.
- **Takeaway:** Learn how to build robust, type-safe conversational flows.

---

## 2. Basic Chatbot in LangGraph

- **Goal:** Build a simple chatbot using LangGraph.
- **Concepts:** Nodes, edges, and state transitions.
- **Takeaway:** Understand the fundamentals of graph-based conversational design.

---

## 3. LangGraph with Tools (Tavily, Arxiv, Wiki, etc.)

- **Goal:** Integrate external tools and APIs (e.g., Tavily for news, Arxiv for research, Wikipedia).
- **Concepts:** Tool nodes, API chaining, dynamic information retrieval.
- **Takeaway:** Enhance chatbot capabilities with real-time and domain-specific knowledge.

---

## 4. Monitoring & Debugging (LangSmith, LangGraph Dev)

- **Goal:** Use [LangSmith](https://smith.langchain.com/) and LangGraph Dev for workflow monitoring and debugging.
- **Concepts:** Tracing, logging, error analysis, and performance monitoring.
- **Takeaway:** Build reliable and observable conversational systems.

---

## 5. LangGraph Debugging (LangGraph Dev)

- **Goal:** Deep dive into debugging with LangGraph Dev tools.
- **Concepts:** Step-through execution, state inspection, and live graph visualization.
- **Takeaway:** Efficiently debug and optimize complex workflows.

---

## 6. Workflow Patterns

- **Prompt Chaining:** Sequentially connect multiple prompts for complex reasoning.
- **Parallelization:** Run multiple nodes/branches in parallel for efficiency.
- **Routing:** Dynamically select workflow paths based on user input or context.
- **Orchestration:** Coordinate multiple agents/tools in a single workflow.
- **Evaluation:** Assess and compare different workflow outputs.

---

## 7. Human Feedback Integration

- **Goal:** Incorporate user feedback directly into the workflow.
- **Concepts:** Human-in-the-loop, feedback nodes, adaptive responses.
- **Takeaway:** Improve chatbot quality and adaptability with real user input.

---

## 8. RAG: Agentic, Corrective, Adaptive

- **Agentic RAG:** Agents retrieve and synthesize information.
- **Corrective RAG:** The system corrects or refines its answers based on feedback.
- **Adaptive RAG:** Dynamically adjusts retrieval/generation strategies.

---

## 9. Multi-Agent Collaboration

- **Goal:** Explore collaboration between specialized agents (e.g., CEO Agent, Research Agent, Writing Agent).
- **Concepts:** Agent roles, inter-agent communication, task delegation.
- **Takeaway:** Build complex, multi-step workflows with specialized expertise.

---

## 10. AgenticAI Project: Use Cases

- **Basic Chatbot:**  
  Ask any general question. The bot responds using only its built-in LLM knowledge (no web search).

- **Chatbot With Web:**  
  Ask questions and get answers that combine the LLM’s knowledge with up-to-date information from the web (e.g., Google search).

- **AI News:**  
  Search for the latest news about topics like LangChain, LangGraph, etc., using the Tavily API for real-time updates.

- **Consultant Bot:**  
  Ask for expert advice on any topic. The bot responds as a professional consultant, providing detailed and expert-level answers.

---

## 11. BlogAgentic: Blog Generation & Translation

- **Blog Title and Content Generation:**  
  Uses an LLM to generate creative, SEO-friendly blog titles and detailed content based on a user-provided topic.

- **Multi-language Translation:**  
  Supports translation of blog content into multiple languages (Hindi, French, Thai, German, Italian, Portuguese, Spanish, etc.).

- **Graph-based Workflow:**  
  Modular nodes for each step (title creation, content generation, translation, routing) managed by LangGraph.

- **API Endpoint:**  
  Exposes a `/generate_blog` POST endpoint for easy integration.

- **Extensible Design:**  
  Easily add new nodes or languages by extending the graph and node classes.

---

## Getting Started

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

## Acknowledgements
LangChain
LangGraph
LangSmith
Tavily API
Arxiv API