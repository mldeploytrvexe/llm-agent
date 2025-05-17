from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage


def document_name_node(state: State):
    ''' Define type of document by user messages '''
    
    prompt = PromptTemplate(
        input_variables=["message"],
        template="По сообщениям пользователя нужно понять, как назвать нужный пользователю документ. Выведи только название документа \
             без служебных сообщений и вводных слов \n\n Сообщение пользователя: {message} \n\nНазвание документа:"
    )
    human_message = HumanMessage(content=prompt.format(message=state["message"]))
    document_name = llm.invoke([human_message]).content.strip() #type:ignore
    return {"document_name": document_name}