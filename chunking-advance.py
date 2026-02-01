from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# ============ LOAD PDF ============
def load_pdf(file_path):
    print("📄 Loading PDF...")
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"✅ Pages loaded: {len(documents)}")
    return documents

# ============ SEMANTIC CHUNKING ============
def semantic_chunking(documents):
    print("🧠 Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    print("✂️ Performing AI semantic chunking...")
    text_splitter = SemanticChunker(embeddings)
    chunks = text_splitter.split_documents(documents)
    print(f"✅ Total chunks created: {len(chunks)}")
    return chunks, embeddings

# ============ STORE IN CHROMA VECTOR DB ============
def save_to_chroma(chunks, embeddings):
    print("🗄 Storing embeddings in ChromaDB...")
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )
    print("✅ Chroma Vector DB created successfully!")

# ============ MAIN ============
file_path = input("Enter PDF file path: ")

print("\n🔍 Extracting text from PDF...")
documents = load_pdf(file_path)

print("\n🧩 Performing semantic chunking...")
chunks, embeddings = semantic_chunking(documents)

print("\n💾 Saving to vector database...")
save_to_chroma(chunks, embeddings)

print("\n🎉 Pipeline Complete! Your PDF is AI-ready.")




