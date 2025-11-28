from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

# Import agent nodes
from agents.benjamin_graham import (
    start_analysis_node,
    earnings_stability_node,
    financial_strength_node,
    valuation_node,
    end_analysis_node
)

# =====================================================
# 1) GLOBAL STATE
# =====================================================
class AnalysisState(TypedDict, total=False):
    stock: str
    selected_agent: str
    log: list
    analysis: dict
    summary: str
    verdict: str
    score: float
    error: Optional[str]


# =====================================================
# 2) BUILD GRAHAM GRAPH
# =====================================================
def build_benjamin_graham_graph():
    graph = StateGraph(AnalysisState)

    graph.add_node("start", start_analysis_node)
    graph.add_node("earnings_stability", earnings_stability_node)
    graph.add_node("financial_strength", financial_strength_node)
    graph.add_node("valuation", valuation_node)
    graph.add_node("end", end_analysis_node)

    graph.set_entry_point("start")

    graph.add_edge("start", "earnings_stability")
    graph.add_edge("earnings_stability", "financial_strength")
    graph.add_edge("financial_strength", "valuation")
    graph.add_edge("valuation", "end")
    graph.add_edge("end", END)

    return graph.compile()


# =====================================================
# 3) MAIN EXECUTION WRAPPER
# =====================================================
def run_agent_analysis(stock: str, agent_name: str):
    agent_name = agent_name.lower()

    if agent_name == "benjamin_graham":
        graph = build_benjamin_graham_graph()
    else:
        return {"error": f"Unknown agent: {agent_name}"}

    initial_state = {
        "stock": stock,
        "selected_agent": agent_name
    }

    result = graph.invoke(initial_state)
    return result


# =====================================================
# 4) TEST EXECUTION
# =====================================================
if __name__ == "__main__":
    print("\n--- Running Benjamin Graham Analysis ---\n")

    output = run_agent_analysis("AAPL", "benjamin_graham")
    print(output)

    print("\n--- END ---")
