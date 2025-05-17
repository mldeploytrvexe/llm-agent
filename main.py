from src.agent.graph import app
from src.logger import logger


sample_text = """
Я продаю квартиру, хочу составить для её продажи. 
"""

state_input = {"message": sample_text}
result = app.invoke(state_input)

logger.info(result)
logger.info(f"{result['document_name']}")