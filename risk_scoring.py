def calculate_risk(regex_matches, ml_probability=0.0):

    # --------------------------------
    # CATEGORY WEIGHTS
    # --------------------------------

    weights = {
        "instruction_override": 40,
        "jailbreak": 45,
        "system_prompt_extraction": 45,
        "security_disabling": 45
    }

    # --------------------------------
    # REGEX RISK
    # --------------------------------

    categories = set()

    for match in regex_matches:
        category = match.get("category", "")
        categories.add(category)

    regex_score = 0

    for category in categories:
        regex_score += weights.get(category, 20)

    # --------------------------------
    # ML RISK
    # --------------------------------

    ml_score = ml_probability * 40

    # --------------------------------
    # COMBINED RISK
    # --------------------------------

    risk_score = regex_score + ml_score

    # Maximum 100
    risk_score = min(risk_score, 100)

    # --------------------------------
    # DECISION
    # --------------------------------

    if risk_score >= 70:
        decision = "BLOCK"

    elif risk_score >= 40:
        decision = "REVIEW"

    else:
        decision = "ALLOW"

    return round(risk_score, 2), decision