# 首先导入所需第三方库
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from tqdm import tqdm
import os
from splitter import *


file_loader = LawLoader('../laws')

text_splitter = LawSplitter.from_tiktoken_encoder(
        chunk_size=100, chunk_overlap=20
    )

docs = file_loader.load_and_split(text_splitter=text_splitter)

# 加载开源词向量模型
embeddings = HuggingFaceEmbeddings(model_name="/root/sentence-transformer")

persist_directory = 'data_base/chroma'
# 加载数据库
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=persist_directory  # 允许我们将persist_directory目录保存到磁盘上
)
# 将加载的向量数据库持久化到磁盘上
vectordb.persist()



