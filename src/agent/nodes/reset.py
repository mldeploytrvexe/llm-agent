from src.agent.schemas import State



def reset_node(state: State) -> State:
    state['message'] = None 
    state['document_type'] = None
    state['legality'] = None
    state['document_structure'] = None
    state['markdown_document'] = None

    return state