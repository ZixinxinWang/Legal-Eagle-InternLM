from langchain_community.vectorstores import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os
from LLM import InternLM_LLM
from retriever import get_retriever
from utils import combine_law_docs
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# 定义 Embeddings
embeddings = HuggingFaceEmbeddings(model_name="/root/sentence-transformer")

# 向量数据库持久化路径
persist_directory = 'data_base/chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory, 
    embedding_function=embeddings
)

llm = InternLM_LLM(model_path = "/root/merged")

# Prompt 模板
template = """使用以下上下文来回答用户的问题。如果你不知道答案，就说你不知道。总是使用中文回答。
问题: {question}
可参考的上下文：
···
{context}
···
回答: 
"""

prompt = ChatPromptTemplate.from_template(template)

# multi_query_retriever
retriever = get_retriever(retriever = vectordb.as_retriever(), model = llm)

chain = (
    {"context": retriever | combine_law_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
    )

# test
while 1:
    input_text = input("User  >>> ")
    input_text = input_text.replace(' ', '')
    if input_text == "exit":
        break

    result = chain.invoke(input_text)
    print("检索问答链回答 question 的结果：")
    print(result)
