from llama_index.core.storage import docstore
from markitdown import MarkItDown
from llama_index.core import Document, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.schema import IndexNode
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# converts pdf into md
md = MarkItDown()
result = md.convert("input.pdf")
with open("data/output.md", 'w', encoding='utf-8') as output:
    output.write(result.text_content)

# loading doc into index
documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents)

# ingestion pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=1024, chunk_overlap=128),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)

nodes = pipeline.run(documents=documents)
# docstore = SimpleDocumentStore()
# docstore.add_documents(nodes)

# # save pipeline to cache
# pipeline.persist("./pipeline_storage")

# # load pipeline from cache
# new_pipeline = IngestionPipeline(
#     transformations=[
#         SentenceSplitter(chunk_size=25, chunk_overlap=0),
#         TitleExtractor(),
#     ]
# )
# new_pipeline.load("./pipeline_storage")

#index
index = VectorStoreIndex(nodes=nodes)

# query engine & retriever
query_engine = index.as_query_engine()
retriever = index.as_retriever()

# Chat
while True:
    user_input = input("Ask a question: ")
    response = query_engine.query(user_input)
    nodes = retriever.retrieve(user_input)
    print(response)
    print("\n")
    
    # Print specific node information requested by user
    print("Retrieved Nodes:")
    for i, node in enumerate(nodes):
        print(f"Node {i}:")
        print(f"  Score: {node.score}")
        print(f"  Start Char Index: {node.node.start_char_idx}")
        print(f"  End Char Index: {node.node.end_char_idx}")
        print(f"  Text Content (preview): {node.node.text}")
        print("-" * 50)
