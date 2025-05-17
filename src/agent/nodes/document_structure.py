from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import (PromptTemplate, ChatPromptTemplate, 
                               SystemMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import HumanMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor


def document_structure_node(state: State):
    ''' Define structure of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["document_type", "document_name"],
        template="По типу и названию документа нужно понять, какая у документа должна быть структура. Выведи только структуру документа \
             без служебных сообщений и вводных слов \n\nТип документа: {document_type} \n\nНазвание документа:{document_name} \n\n Структура документа: "
    )
    human_message = HumanMessage(content=prompt.format(document_type=state["document_type"], document_name=state["document_name"]))
    document_structure = llm.invoke([human_message]).content.strip() #type:ignore
    return {"document_structure": document_structure}