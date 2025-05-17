from src.agent.nodes.summarization import summarization_node
from src.agent.shcemas import State
from langgraph.graph import StateGraph, END


workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("summarize", summarization_node)

workflow.set_entry_point("summarize")
workflow.add_edge("summarize", END)

app = workflow.compile()