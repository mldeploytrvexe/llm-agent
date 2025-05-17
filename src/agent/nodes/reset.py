from src.agent.schemas import State
from src.agent.llm import llm
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage




def reset_node(state: State):
    state['message'] = None
    state['document_type'] = None
    state['is_legal'] = None

    return state