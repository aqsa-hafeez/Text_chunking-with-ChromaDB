# Advanced AI Semantic Indexer with ChromaDB 🗄️🧠

A professional-grade RAG (Retrieval-Augmented Generation) ingestion pipeline that performs semantic chunking and stores text embeddings in a persistent Vector Database.

## 🌟 Key Features
* **Semantic Awareness**: Breaks documents into chunks based on context shifts rather than fixed character limits.
* **BGE Embedding Engine**: Integrated with `BAAI/bge-small-en-v1.5` for state-of-the-art text representation.
* **Persistent Vector Store**: Uses **ChromaDB** to index and save embeddings locally, ensuring data remains available after the script ends.
* **Automated PDF Workflow**: Complete pipeline from raw PDF loading to structured database storage.

## 🛠️ Tech Stack
* **Language**: Python
* **Orchestration**: [LangChain](https://www.langchain.com/)
* **Vector DB**: [ChromaDB](https://www.trychroma.com/)
* **Embeddings**: HuggingFace (BGE Model)
* **Libraries**: `langchain-experimental`, `pypdf`, `sentence-transformers`

## 📋 How It Works

[Image: PDF -> Semantic Chunks -> BGE Embeddings -> ChromaDB Storage]

1. **Load**: Extracts text from PDFs using `PyPDFLoader`.
2. **Chunk**: Analyzes sentence relationships and groups them into cohesive semantic units.
3. **Embed**: Converts each chunk into a 384-dimensional vector.
4. **Persist**: Saves the vectors and metadata into a local directory (`/chroma_db`).

## 💻 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/aqsa-hafeez/Text_chunking-with-ChromaDB.git](https://github.com/aqsa-hafeez/Text_chunking-with-ChromaDB.git)

```

2. **Install requirements**:
```bash
pip install langchain-experimental langchain-community langchain-chroma pypdf sentence-transformers

```


3. **Run the Indexer**:
```bash
python chunking-advance.py

```


*Enter the path of your PDF document when prompted.*

## 📂 Project Structure

* `chunking-advance.py`: Main execution script.
* `chroma_db/`: Local folder where your searchable AI memory is stored.

## 🚀 Future Roadmap

* Integration with an LLM (like Llama 3 or Gemini) for a complete Q&A system.
* Support for multi-modal data (images/tables inside PDFs).

---
