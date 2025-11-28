def earnings_stability_node(state):
    stock = state["stock"]

    stability_score = 7.5  # placeholder logic

    state["analysis"]["earnings_stability"] = stability_score
    state["log"].append(f"📈 Earnings Stability: {stability_score}/10")

    return state
