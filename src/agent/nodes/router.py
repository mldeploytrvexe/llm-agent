from src.agent.schemas import State


def router(state: State):
    print('ROUTER')
    print(state)
    if not state.get("document_name"):
        print(1)
        return {"next": "doc_name_node"}
    elif not state.get("legality"):
        print(2)
        return {"next": "doc_legal_node"}
    elif state.get("legality").is_legal is False:
        print(3)
        return {"next": "doc_name_node"}
    
    elif not state.get("document_structure"):
        print(4)
        return {"next": "doc_struct_node"}

    # elif not state.markdown_document:    
    #     return {"next": "gen_md_node"}