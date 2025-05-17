from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from src.agent.schemas import Legality
from src.logger import logger



def document_name_node(state: State):
    ''' Define type of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["message"],
        template="По сообщениям пользователя нужно понять, как назвать нужный пользователю документ. Выведи только название документа \
             без служебных сообщений и вводных слов \n\n Сообщение пользователя: {message} \n\n Если у тебя достаточно информации, чтобы \
                сформулировать название для документа, верни только название документа без каких-либо служебных фраз, иначе верни None:"
    )
    human_message = HumanMessage(content=prompt.format(message=state.message))
    document_name = llm.invoke([human_message]).content.strip()
    return {"document_name": document_name}


def document_legal_node(state: State):
    ''' Define legal of document'''
    
    prompt = PromptTemplate(
        input_variables=["document_name", "messages"],
        template="По названию документа и сообщениям пользователя нужно определить, легально ли создать такой документ. Верни значение типа bool: True или False\n\n \
              Название документа: {document_name} \n\n Сообщения пользователя:  {messages} \n\n Очень тщательно проверь, соответствует ли законодательству этот документ?: \
                | Если результат проверки документа на законность True, верни результат в таком виде: True|None \
                     Если результат проверки документа на законность False, верни результат в таком виде: False|причина незаконности документа"
    )
    human_message = HumanMessage(content=prompt.format(document_name=state.document_name,
                                                       messages=state.message))
    
    legality = llm.invoke([human_message]).content.strip()

    return {"legality": Legality(is_legal=legality[0],
                                 reason=legality[1])}



def document_structure_node(state: State):
    ''' Define structure of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["document_name"],
        template="По названию документа нужно понять, какая у документа должна быть структура. Выведи только структуру документа \
             без служебных сообщений и вводных слов \n\nНазвание документа:{document_name} \n\n Структура документа: "
    )
    human_message = HumanMessage(content=prompt.format(document_name=state.document_name))
    
    document_structure = llm.invoke([human_message]).content.strip() #type:ignore
    return {"document_structure": document_structure}