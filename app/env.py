import os
import langchain
if os.environ.get("QNA_DEBUG") == "true":
    langchain.debug = True

from qna.llm import make_qna_chain, get_llm

from langchain.vectorstores import Pinecone
from torch import cuda
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
import pinecone

embed_model_id = 'BAAI/bge-large-en-v1.5'

device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={'device': device},
    encode_kwargs={'device': device, 'batch_size': 32}
)



# get API key from app.pinecone.io and environment from console
pinecone.init(
    # api_key=os.environ.get('PINECONE_API_KEY') or '84ae3144-97cc-4ca1-9ef4-5019c71964e7',
    api_key=os.environ.get('PINECONE_API_KEY') or '35f17c29-83cb-4481-92b4-5d6aedc605f5',
    environment=os.environ.get('PINECONE_ENVIRONMENT') or 'gcp-starter'
)

index_name = 'occupation-rag'
index = pinecone.Index(index_name)
text_field = 'text'  # field in metadata that contains text content

vectorstore = Pinecone(
    index, embed_model.embed_query, text_field
)

API_KEY = ""
os.environ["OPENAI_API_KEY"] = API_KEY
llm = get_llm(max_tokens=8192)

chain = make_qna_chain(
            llm,
            vectorstore,
            # prompt=query,
            k=6,
            search_type="similarity",
            # distance_threshold=0.5
        )


