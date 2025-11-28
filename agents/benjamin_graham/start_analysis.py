def start_analysis_node(state):
    stock = state.get("stock", "").upper()

    return {
        "stock": stock,
        "log": [f"🔍 Starting Benjamin Graham analysis for {stock}"],
        "analysis": {}
    }
