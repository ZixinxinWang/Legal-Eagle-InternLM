from typing import List
from collections import defaultdict

from langchain.docstore.document import Document

def combine_law_docs(docs: List[Document]) -> str:
    # 将检索到的法条合并为str
    # 相关法律：《中华人民共和国刑法》
    # 第一条 XXXX
    # 相关法律：《中华人民共和国宪法》
    # 第三条 XXXX
    law_books = defaultdict(list)
    for doc in docs:
        metadata = doc.metadata
        if 'book' in metadata:
            law_books[metadata["book"]].append(doc)

    law_str = ""
    for book, docs in law_books.items():
        law_str += f"相关法律：《{book}》\n"
        law_str += "\n".join([doc.page_content.strip("\n") for doc in docs])
        law_str += "\n"

    return law_str

