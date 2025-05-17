from src.agent.nodes.document_name import document_name_node
from src.agent.nodes.document_legal import document_legal_node
from src.agent.schemas import State
from langgraph.graph import StateGraph, END


workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("document_name_node", document_name_node)
workflow.add_node("document_legal_node", document_legal_node)

workflow.set_entry_point("document_name_node")
workflow.add_edge("document_name_node", "document_legal_node")
workflow.add_edge("document_legal_node", END)

app = workflow.compile()