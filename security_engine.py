from attack_patterns import detect_regex_attacks
from risk_scoring import calculate_risk


def analyze_prompt(prompt, ml_probability=0.0):

    # 1. Detect attacks using Regex
    regex_matches = detect_regex_attacks(prompt)

    # 2. Calculate risk using Regex + ML probability
    risk_score, decision = calculate_risk(
        regex_matches,
        ml_probability
    )

    # 3. Extract unique attack categories
    categories = list(
        set(
            match["category"]
            for match in regex_matches
        )
    )

    # 4. Return complete security result
    return {
        "prompt": prompt,
        "regex_matches": regex_matches,
        "categories": categories,
        "ml_probability": ml_probability,
        "risk_score": risk_score,
        "decision": decision
    }