from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from src.logger import logger
from src.global_store import GlobalStore


def gen_markdown_node(state: State):
    ''' Generating markdown by document structure '''
    
    logger.info("GEN MDOWN NODE")

    prompt = PromptTemplate(
        input_variables=["message", "document_structure"],
        template="По сообщениям пользователя и структуре документа сгенерируй markdown документ с пропусками для ввода пользователем данных \
            именно для потребности из его сообщений. Выведи готовый документ с заполненными тобой текстом общими полями по типу: общие положения, \
                 обязанности сторон, ответственность сторон и так далее; обязательно используй информацию из сообщения пользователя \
             без служебных сообщений и вводных слов \n\n Сообщения пользователя: {message} \n\n Структура документа: {document_structure} \n\n Готовый markdown документ \
                с кореектным переносом строк и правильной структурой:"
    )
    human_message = HumanMessage(content=prompt.format(message=state.get("message"),
                                                       document_structure=state.get("document_structure")))
    markdown_document = llm.invoke([human_message]).content.strip()
    if markdown_document:
        GlobalStore.answer = "Ваш документ готов в редакторе"
        GlobalStore.mdwn = markdown_document
    return {"markdown_document": markdown_document, "next": "gen_md_node"}
