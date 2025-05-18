from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from src.agent.llm import llm
from src.api_schemas import ChatResponse
from src.logger import logger

chat_history = []


def run_SP(new_message: str) -> ChatResponse:
    prompt_text = "Ты помощник по юридическим документам. Твоя обязанность предоставить пользователю документ, который ему нужен по его сообщениям в чате. \
            Твой механизм работы состоит из 4 шагов: 1 - определить название документа, 2 - определить законность составления такого документа, 3 - Определить подходящую структуру для документа, \
                4 - Сгенерировать маркдаун текст по структуре. Ты не можешь перейти к следущему шагу, если текущий не выполнен. Ты можешь задавать пользователю вопросы \
                    чтобы выполнить тот или иной шаг. Шаг 2 важный и если запрос не законный, дальше идти нельзя \
                        Формат твоих ответов это строгая json строка без оформления, который имеет поля message и markdown_str. Поле message обязательное и это твой ответ в чате. Поле markdown_str необязательное \
                            и может быть null, отправляй значение mardown_str только когда все шаги пройдены. \
                                История сообщений: {history} \
                                Текущее новое сообщение, на которое нужно ответить сейчас: {new_message}"
    
    prompt = PromptTemplate(
        input_variables=["history", "new_message"],
        template=prompt_text
    )
    
    human_message = HumanMessage(
        content=prompt.format(
            history=f"[{','.join(chat_history)}]",
            new_message=new_message
        )
    )
    chat_history.append({"role": "user", "text": new_message})

    response = llm.invoke([human_message]).content.strip()
    json_str = response.replace("```", "").replace("json", "")
    chat_history.append({"role": "ai", "text": json_str})

    logger.info(json_str)
    chat_answer = ChatResponse.model_validate_json(json_str)

    return chat_answer

