def end_analysis_node(state):
    earnings = state["analysis"]["earnings_stability"]
    financial = state["analysis"]["financial_strength"]
    valuation = state["analysis"]["valuation"]["margin_of_safety"]

    # Score calculation
    score = round((earnings + financial + (valuation / 10)) / 3, 2)

    # Verdict
    if score >= 7:
        verdict = "✅ BUY"
    elif score >= 5:
        verdict = "⚠️ HOLD"
    else:
        verdict = "❌ SELL"

    # Summary text
    summary = (
        "\n".join(state["log"])
        + f"\n\n📊 Final Score: {score}/10\n"
        + f"📌 Recommendation: {verdict}"
    )

    state["summary"] = summary
    state["verdict"] = verdict
    state["score"] = score

    return state
