from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage



def document_legal_node(state: State):
    ''' Define legal of document'''
    
    prompt = PromptTemplate(
        input_variables=["document_name"],
        template="По названию документа нужно определить, легально ли создать такой документ. Верни значение типа bool: True или False\n\n \
              Название документа: {document_name} \n\n Легально ли создать такой документ:"
    )
    human_message = HumanMessage(content=prompt.format(document_name=state["document_name"]))
    is_legal = llm.invoke([human_message]).content.strip()
    return {"is_legal": is_legal}