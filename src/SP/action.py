from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from src.agent.llm import llm
from src.api_schemas import ChatResponse

chat_history = []


def run_SP(new_message: str) -> ChatResponse:
    prompt = PromptTemplate(
        input_variables=["history", "new_message"],
        template=f"Ты личный юрист. Ответ своему клиенту на следующее сообщение: {new_message}"
    )
    human_message = HumanMessage(
        content=prompt.format(
            history=f"[{','.join(chat_history)}]",
            new_message=new_message
        )
    )
    chat_history.append({"role": "user", "text": new_message})

    response = llm.invoke([human_message]).content.strip()
    chat_history.append({"role": "ai", "text": response})

    chat_answer = ChatResponse.model_validate_json(response)

    return chat_answer

