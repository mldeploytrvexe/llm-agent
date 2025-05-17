from src.agent.graph import app
from src.logger import logger
from langchain_core.messages import HumanMessage
from src.agent.graph import document_name_node


user_text = """Я хочу купить квартиру, помоги мне составить договор."""



state_input = {"message": user_text}
result = document_name_node(state_input)