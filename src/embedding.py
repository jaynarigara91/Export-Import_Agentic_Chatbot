from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from pathlib import Path
import os
import yaml

import warnings
warnings.filterwarnings("ignore")

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

current_dir = Path(__file__).parent
config_path = current_dir / 'config.yaml'

with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

class EmbeddingProcess:
    
    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(model=config['config']['embedding_model'])
        self.urls = [config['urls']]
        
        print("web loading...")
        
        self.docs = [WebBaseLoader(url).load() for url in self.urls]
        self.docs_list = [item for sublist in self.docs for item in sublist]
        
        print("Chunking...")
        
        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=config['config']['chunk_size'], chunk_overlap=config['config']['chunk_overlap'], separators=["\n\n", "\n", ".", " "]
        )
        
        self.doc_split = self.text_splitter.split_documents(self.docs_list)
        
        print("embedding....")
        
        self.vector_store = Chroma.from_documents(
            documents=self.doc_split,
            embedding=self.embeddings,
        )
        
        self.retriever = self.vector_store.as_retriever()
    