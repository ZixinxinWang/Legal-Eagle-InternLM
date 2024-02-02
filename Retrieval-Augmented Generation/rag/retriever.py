from langchain.schema import BaseRetriever
from langchain.pydantic_v1 import Field, BaseModel
from langchain.chains import LLMChain
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.output_parsers import PydanticOutputParser
from typing import List
from prompt import MULTI_QUERY_PROMPT_TEMPLATE


class LineList(BaseModel):
    # "lines" is the key (attribute name) of the parsed output
    lines: List[str] = Field(description="Lines of text")


class LineListOutputParser(PydanticOutputParser):
    def __init__(self) -> None:
        super().__init__(pydantic_object=LineList)

    def parse(self, text: str) -> LineList:
        lines = text.strip().split("\n")
        return LineList(lines=lines)


def get_retriever(retriever: BaseRetriever, model: BaseModel):
    output_parser = LineListOutputParser()

    llm_chain = LLMChain(llm=model, prompt=MULTI_QUERY_PROMPT_TEMPLATE, output_parser=output_parser)

    retriever = MultiQueryRetriever(
        retriever=retriever, llm_chain=llm_chain, parser_key="lines"
    )

    return retriever

