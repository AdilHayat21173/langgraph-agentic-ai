# PDF RAG System with Groq and Google Embeddings

A high-performance Retrieval-Augmented Generation (RAG) system that allows you to ask questions about PDF documents using Groq's fast inference and Google's embeddings.

## 🚀 Features

- **Fast Inference**: Uses Groq for ultra-fast LLM responses
- **Smart Caching**: Intelligent caching system to avoid reprocessing documents
- **Google Embeddings**: High-quality semantic search with Google's embedding models
- **LangSmith Integration**: Comprehensive monitoring and tracing
- **Production Ready**: Robust error handling and performance optimization

## 📋 Prerequisites

- Python 3.8+
- API keys for:
  - [Groq](https://console.groq.com/)
  - [Google AI Studio](https://aistudio.google.com/)
  - [LangSmith](https://smith.langchain.com/) (optional but recommended)

## 🔧 Installation

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -U langchain langchain-groq langchain-community langchain-google-genai faiss-cpu pypdf python-dotenv langsmith
```

3. **Create environment file**:
Create a `.env` file in your project root:
```env
# Groq API Key (get from https://console.groq.com/)
GROQ_API_KEY=gsk_your_groq_api_key_here

# Google AI API Key (get from https://aistudio.google.com/)
GOOGLE_API_KEY=your_google_api_key_here

# LangSmith Configuration (optional)
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=pdf-rag-groq
```

4. **Place your PDF**:
Put your PDF file in the project directory and update the `PDF_PATH` variable in the script.

## 🏃‍♂️ Quick Start

### Basic Usage

```python
from your_script import setup_pipeline_and_query

# Ask a question about your PDF
question = "What is the main topic of this document?"
answer = setup_pipeline_and_query("your_document.pdf", question)
print(answer)
```

### Command Line Usage

```bash
python your_script.py
```
Then enter your question when prompted.

### Advanced Usage

```python
# Custom configuration
answer = setup_pipeline_and_query(
    pdf_path="research_paper.pdf",
    question="Explain the methodology used in the study",
    chunk_size=1500,        # Larger chunks for more context
    chunk_overlap=200,      # More overlap for better continuity
    force_rebuild=True      # Force rebuild index
)
```

## ⚙️ Configuration Options

### Model Configuration

**Groq Models** (update in script):
```python
# Fast and efficient (default)
llm = ChatGroq(model="openai/gpt-oss-20b")

# Alternative models
llm = ChatGroq(model="llama-3.1-70b-versatile")  # More capable
llm = ChatGroq(model="llama-3.1-8b-instant")    # Faster
```

**Embedding Models**:
```python
# Default Google embedding
embed_model_name = "models/embedding-001"

# Advanced embedding (if available)
embed_model_name = "models/text-embedding-004"
```

### Chunking Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `chunk_size` | 1000 | Maximum characters per chunk |
| `chunk_overlap` | 150 | Overlap between chunks |
| `k` | 4 | Number of chunks to retrieve |

### Retrieval Configuration

```python
# Retrieve more chunks for complex questions
retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

# Use Maximum Marginal Relevance for diverse results
retriever = vectorstore.as_retriever(search_type="mmr")
```

## 📁 Project Structure

```
your_project/
├── pdf_rag_system.py      # Main script
├── your_document.pdf      # Your PDF file
├── .env                   # Environment variables
├── README.md             # This file
└── .indices/             # Auto-generated cache directory
    └── [hash_folders]/   # Cached embeddings (one per config)
        ├── index.faiss   # Vector index
        ├── index.pkl     # FAISS metadata
        └── meta.json     # Processing metadata
```

## 🔍 How It Works

### 1. Document Processing
- **PDF Loading**: Extracts text from PDF pages
- **Text Splitting**: Breaks text into manageable chunks with overlap
- **Embedding**: Converts chunks to vectors using Google's embeddings
- **Indexing**: Creates FAISS index for fast similarity search

### 2. Query Processing
- **Question Embedding**: Converts user question to vector
- **Similarity Search**: Finds most relevant document chunks
- **Context Assembly**: Combines retrieved chunks
- **Generation**: Groq model generates answer from context

### 3. Caching System
- **File Fingerprinting**: Tracks PDF changes via SHA256 hash
- **Configuration Hashing**: Separate caches for different settings
- **Smart Loading**: Reuses existing embeddings when possible

## 📊 Monitoring with LangSmith

### View Traces
1. Visit [LangSmith Dashboard](https://smith.langchain.com/)
2. Select your project (default: `pdf-rag-groq`)
3. View detailed execution traces

### Tracked Metrics
- **Latency**: Response times for each component
- **Token Usage**: Input/output tokens and costs
- **Retrieval Quality**: Which chunks are being retrieved
- **Error Rates**: Failed operations and debugging info

### Trace Hierarchy
```
pdf_rag_full_run
├── setup_pipeline
│   ├── load_pdf
│   ├── split_documents
│   └── build_vectorstore
└── retrieval_and_generation
```
# LangSmith Trace: `pdf_rag_full_run`

We traced the input in **LangSmith** and observed the following steps:

## Pipeline Execution

- **setup_pipeline** → **5.19s**
- **build_index** → **5.14s**
  - **load_pdf** → **1.17s**
  - **split_documents** → **0.03s**
  - **build_vectorstore** → **3.85s**
- **pdf_rag_query** → **1.14s**
  - **map:key:context** → **0.47s**
  - **VectorStoreRetriever** → **0.46s**
  - **format_docs** → **0.00s**

## Model Used
- **openai/gpt-oss-20b**

## video demo 

## 🎯 Best Practices

### Document Preparation
- **Clean PDFs**: Ensure text is extractable (not image-only)
- **File Size**: Larger files take longer on first processing
- **Content Quality**: Better organized documents = better results

### Query Optimization
- **Specific Questions**: More specific queries get better answers
- **Document Scope**: Ask questions that match document content
- **Context Limits**: Very broad questions may exceed context windows

### Performance Tuning
- **Chunk Size**: 
  - Smaller (500-800): More precise retrieval
  - Larger (1200-1500): More context per chunk
- **Overlap**: 150-200 characters usually optimal
- **Top-K**: Start with 4, increase for complex questions

## 🐛 Troubleshooting

### Common Issues

**Slow First Run**
- ✅ **Normal behavior**: First run processes entire PDF
- ✅ **Subsequent runs**: Much faster due to caching

**Empty or Poor Answers**
- ❌ **Check**: Question relevance to document content
- ❌ **Try**: More specific questions
- ❌ **Adjust**: Increase `k` value for more context

**API Errors**
- ❌ **Check**: API keys in `.env` file
- ❌ **Verify**: API key permissions and quotas
- ❌ **Test**: Individual API endpoints

**Memory Issues**
- ❌ **Reduce**: `chunk_size` parameter
- ❌ **Process**: Smaller PDF files
- ❌ **Upgrade**: System RAM if possible

### Debug Mode
```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.INFO)

# Force rebuild to test processing
answer = setup_pipeline_and_query(
    pdf_path="document.pdf",
    question="test question",
    force_rebuild=True
)
```

## 💡 Tips & Tricks

### Question Formulation
```python
# ✅ Good questions
"What methodology was used in the study?"
"List the key findings from Chapter 3"
"What are the main benefits mentioned?"

# ❌ Avoid overly broad questions
"Tell me everything about this document"
"What is this document about?"
```

### Custom Prompts
```python
# Modify the system prompt for specialized use cases
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research analyst. Provide detailed explanations with specific examples and page references when possible."),
    ("human", "Question: {question}\n\nContext:\n{context}")
])
```

### Batch Processing
```python
questions = [
    "What is the main research question?",
    "What methodology was used?",
    "What are the key findings?",
    "What are the limitations?"
]

for q in questions:
    answer = setup_pipeline_and_query("paper.pdf", q)
    print(f"Q: {q}")
    print(f"A: {answer}\n")
```

## 📈 Performance Benchmarks

### Typical Performance
- **First Run**: 30-120 seconds (depending on PDF size)
- **Cached Runs**: 2-5 seconds per query
- **Groq Inference**: ~500ms for generation
- **Memory Usage**: ~100-500MB depending on document size

### Optimization Results
- **Caching**: 20-50x faster subsequent runs
- **Groq vs OpenAI**: 5-10x faster inference
- **FAISS**: Sub-second similarity search

## 🔄 Updates and Maintenance

### Rebuilding Indices
```python
# When to rebuild:
# - PDF content changed
# - Different chunk parameters needed
# - Embedding model updated

answer = setup_pipeline_and_query(
    pdf_path="updated_document.pdf",
    question="Your question",
    force_rebuild=True  # Forces fresh processing
)
```

### Cache Management
```bash
# Clear all cached indices
rm -rf .indices/

# Or selectively delete specific caches from .indices/ directory
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [FAISS Documentation](https://faiss.ai/)

## 🆘 Support

For issues and questions:
1. Check this README and troubleshooting section
2. Review LangSmith traces for debugging
3. Check API provider status pages
4. Create an issue in the repository

---

Made with ❤️ using LangChain, Groq, and Google AI