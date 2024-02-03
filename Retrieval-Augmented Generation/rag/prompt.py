from langchain.prompts import PromptTemplate


multi_query_prompt_template = """您是 AI 语言模型助手。您的任务是生成给定用户问题的3个不同版本，以从矢量数据库中检索相关文档。
                                通过对用户问题生成多个视角，您的目标是帮助用户克服基于距离的相似性搜索的一些限制。
                                提供这些用换行符分隔的替代问题，不要给出多余的回答。问题：{question}""" # noqa
MULTI_QUERY_PROMPT_TEMPLATE = PromptTemplate(
    template=multi_query_prompt_template, input_variables=["question"]
)
