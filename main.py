from src.agent.graph import app
from src.logger import logger


sample_text = """
Я хочу купить квартиру, помоги мне составить договор. 
"""

state_input = {"message": sample_text}
result = app.invoke(state_input)

logger.info(result)