from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from src.agent.schemas import Legality
from src.logger import logger
from src.global_store import GlobalStore


def document_name_node(state: State):
    ''' Define type of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["message"],
        template="По сообщениям пользователя нужно понять, как назвать нужный пользователю документ. Выведи только название документа \
             без служебных сообщений и вводных слов \n\n Сообщение пользователя: {message} \n\n Если у тебя достаточно информации, чтобы \
                сформулировать название для документа, верни только название документа без каких-либо служебных фраз, иначе верни None:"
    )
    human_message = HumanMessage(content=prompt.format(message=state.get("message")))
    document_name = llm.invoke([human_message]).content.strip()
    
    if document_name:
        GlobalStore.answer = f"Я смог определить тип подходящего для вас документа.Вам подойдёт: {document_name}"
    else:
        GlobalStore.answer = f"Я не смог определить тип подходящего для вас документа. Попробуйте более подробно рассказать о своих целях"
    state['document_name'] = document_name
    state["next"] = "router"
    return state


def document_legal_node(state: State):
    ''' Define legal of document'''
    
    prompt = PromptTemplate(
        input_variables=["document_name", "messages"],
        template="По названию документа и сообщениям пользователя нужно определить, легально ли создать такой документ. Верни значение типа bool: True или False\n\n \
              Название документа: {document_name} \n\n Сообщения пользователя:  {messages} \n\n Очень тщательно проверь, соответствует ли законодательству этот документ?: \
                | Если результат проверки документа на законность True, верни результат в таком виде: True|None \
                     Если результат проверки документа на законность False, верни результат в таком виде: False|причина незаконности документа"
    )
    human_message = HumanMessage(content=prompt.format(document_name=state.get("document_name"),
                                                       messages=state.get("message")))
    
    legality = llm.invoke([human_message]).content.strip()

    state['legality'] = Legality(is_legal=legality[0],
                                 reason=legality[1])
    state['next'] = "router"

    answer = "Ваш документ является законным"
    if not state['legality'].is_legal:
        answer = f"Ваш документ не является законным. Причина: {state['legality'].reason}"
    
    GlobalStore.answer = answer
    return state


def document_structure_node(state: State):
    ''' Define structure of document by user messages '''
    if state.get("document_structure") is not None:
        return {}
    
    prompt = PromptTemplate(
        input_variables=["document_name"],
        template="По названию документа нужно понять, какая у документа должна быть структура. Выведи только структуру документа \
             без служебных сообщений и вводных слов \n\nНазвание документа:{document_name} \n\n Структура документа: "
    )
    human_message = HumanMessage(content=prompt.format(document_name=state.get("document_name")))
    
    document_structure = llm.invoke([human_message]).content.strip() #type:ignore
    # state["document_structure"] = document_structure
    # state["next"] = "router"
    print('STRUCTURE is READY')
    return {"document_structure": document_structure}
