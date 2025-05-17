from src.agent.nodes import (document_name_node, document_legal_node, 
                             document_structure_node, gen_markdown_node,
                             router)
from src.agent.schemas import State
from langgraph.graph import StateGraph, END, START


workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("doc_name_node", document_name_node)
workflow.add_node("doc_legal_node", document_legal_node)
workflow.add_node("doc_struct_node", document_structure_node)
workflow.add_node("gen_md_node", gen_markdown_node)
workflow.add_node("router", router)

workflow.add_edge(START, "gen_md_node")
# workflow.set_entry_point("doc_name_node")
# workflow.add_edge("doc_name_node", "doc_legal_node")
# workflow.add_edge("doc_legal_node", "doc_struct_node")
# workflow.add_edge("doc_struct_node", "gen_md_node")
workflow.add_edge("gen_md_node", END)


members = ["doc_name_node", "doc_legal_node", "doc_struct_node", "gen_md_node"]
workflow.add_conditional_edges("router", lambda x: x["next"])


app = workflow.compile()