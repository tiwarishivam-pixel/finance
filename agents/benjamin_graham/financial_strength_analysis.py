def financial_strength_node(state):
    stock = state["stock"]

    score = 6.8  # placeholder logic

    state["analysis"]["financial_strength"] = score
    state["log"].append(f"💼 Financial Strength: {score}/10")

    return state
