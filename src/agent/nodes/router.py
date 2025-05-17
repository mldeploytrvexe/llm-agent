from src.agent.schemas import State


def router(state: State):
    if not state.document_name:
        return {"next": "doc_name_node"}
    elif not state.legality:
        return {"next": "doc_legal_node"}
    elif state.legality.is_legal is False:
        return {"next": "doc_name_node"}
    
    elif not state.document_structure:
        return {"next": "doc_struct_node"}

    elif not state.markdown_document:    
        return {"next": "gen_md_node"}