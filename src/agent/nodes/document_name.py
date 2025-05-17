from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import (PromptTemplate, ChatPromptTemplate, 
                               SystemMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import HumanMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor



system_messages = \
f"""
Твоя задача помогать пользователю составлять шаблоны документов для потребностей пользователя
Следуй этому алгоритму действий:
1. По первым сообщениям пользователя нужно понять, какой тип документа ему подходит (поименованный или непоименованный) 
и как кратко назвать нужный пользователю документ
2. По краткому названию документа определять, законно ли составлять такой документ
"""





def document_name_node(state: State):
    ''' Define type of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["message"],
        template="По сообщениям пользователя нужно понять, как назвать нужный пользователю документ. Выведи только название документа \
             без служебных сообщений и вводных слов \n\n Сообщение пользователя: {message} \n\nНазвание документа:"
    )
    human_message = HumanMessage(content=prompt.format(message=state["message"]))
    document_name = llm.invoke([human_message]).content.strip()
    return {"document_name": document_name}