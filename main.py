from markitdown import MarkItDown
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
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
index = VectorStoreIndex.from_documents(documents)

# query engine
query_engine = index.as_query_engine()

# Chat
while True:
    user_input = input("Ask a question: ")
    response = query_engine.query(user_input)
    print(response)

