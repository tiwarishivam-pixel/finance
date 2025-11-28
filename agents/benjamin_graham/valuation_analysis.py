def valuation_node(state):
    intrinsic_value = 120.50
    current_price = 100.00
    margin_of_safety = round((intrinsic_value - current_price) / intrinsic_value * 100, 2)

    state["analysis"]["valuation"] = {
        "intrinsic_value": intrinsic_value,
        "current_price": current_price,
        "margin_of_safety": margin_of_safety
    }

    state["log"].append(
        f"💰 Valuation → IV: ${intrinsic_value}, Price: ${current_price}, MOS: {margin_of_safety}%"
    )

    return state
