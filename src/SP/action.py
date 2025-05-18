from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from src.agent.llm import llm

chat_history = []


def run_SP(new_message: str):
    prompt = PromptTemplate(
        input_variables=["messages", "new_message"],
        template=f"Ты личный юрист. Ответ своему клиенту на следующее сообщение: {new_message}"
    )
    human_message = HumanMessage(
        content=prompt.format(
            messages="",
            new_message=new_message
        )
    )
    chat_history.append({"role": "user", "text": new_message})

    response = llm.invoke([human_message]).content.strip()

    return response

