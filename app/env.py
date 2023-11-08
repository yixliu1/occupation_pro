import os
import langchain
if os.environ.get("QNA_DEBUG") == "true":
    langchain.debug = True
from qna.llm import make_qna_chain, get_llm, get_embeddings
from langchain.vectorstores import Pinecone
from torch import cuda
from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
import pinecone
from qna.constants import (
    OPENAI_COMPLETIONS_ENGINE,
    OPENAI_EMBEDDINGS_ENGINE,
)

API_KEY = ""
os.environ["OPENAI_API_KEY"] = API_KEY

# embed_model_id = 'BAAI/bge-large-en-v1.5'
#
# device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
#
# embed_model = HuggingFaceEmbeddings(
#     model_name=embed_model_id,
#     model_kwargs={'device': device},
#     encode_kwargs={'device': device, 'batch_size': 32}
# )
embed = get_embeddings()


# get API key from app.pinecone.io and environment from console
pinecone.init(
    # api_key=os.environ.get('PINECONE_API_KEY') or '84ae3144-97cc-4ca1-9ef4-5019c71964e7',
    api_key=os.environ.get('PINECONE_API_KEY') or 'f7c73a05-ef87-4189-91b2-fa7b4523aa85',
    environment=os.environ.get('PINECONE_ENVIRONMENT') or 'gcp-starter'
)

index_name = 'occupation-rag'
index = pinecone.Index(index_name)
text_field = 'text'  # field in metadata that contains text content

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)

llm = get_llm(max_tokens=8192)

chain = make_qna_chain(
            llm,
            vectorstore,
            # prompt=query,
            k=6,
            search_type="similarity",
            # distance_threshold=0.5
        )


