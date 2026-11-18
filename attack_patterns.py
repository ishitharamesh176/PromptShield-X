import re


ATTACK_PATTERNS = {

    "instruction_override": [

        r"\b(ignore|disregard|forget|override|cancel)\b.*\b(previous|prior|earlier|old|existing|current)\b.*\b(instructions?|guidelines?|rules?|commands?)\b",

        r"\b(previous|prior|earlier|old|existing)\b.*\b(rules?|instructions?|guidelines?|commands?)\b.*\b(no\s+longer|not)\b.*\b(valid|apply|active)\b",

        r"\bfrom\s+now\s+on\b.*\b(ignore|disregard|forget|override)\b",

        r"\bfollow\s+my\s+(instructions?|commands?|rules?|guidelines?)\b",

        r"\bforget\s+everything\s+you\s+were\s+instructed\s+to\s+do\b"
    ],


    "jailbreak": [

        r"\byou\s+are\s+now\s+an?\s+unrestricted\s+(ai|assistant|model)\b",

        r"\bact\s+as\s+(an?\s+)?ai\s+without\s+(any\s+)?restrictions?\b",

        r"\benter\s+developer\s+mode\b",

        r"\bbypass\s+(your\s+)?safety\s+filters?\b",

        r"\bpretend\s+you\s+have\s+no\s+restrictions?\b",

        r"\byou\s+are\s+free\s+from\s+all\s+safety\s+(guidelines?|rules?|restrictions?)\b"
    ],


    "system_prompt_extraction": [

        r"\breveal\s+(your\s+)?system\s+prompt\b",

        r"\bshow\s+me\s+(your\s+)?hidden\s+instructions?\b",

        r"\bprint\s+(your\s+)?initial\s+prompt\b",

        r"\btell\s+me\s+the\s+instructions?\s+given\s+to\s+you\s+by\s+the\s+system\b",

        r"\bwhat\s+are\s+your\s+hidden\s+system\s+instructions?\b",

        r"\bshow\s+the\s+secret\s+prompt\s+controlling\s+your\s+behavior\b"
    ],


    "security_disabling": [

        r"\bdisable\s+(all\s+)?security\s+(checks|rules|filters)\b",

        r"\bturn\s+off\s+(your\s+)?safety\s+filters?\b",

        r"\bdisable\s+(your\s+)?security\s+rules?\b",

        r"\bstop\s+following\s+safety\s+restrictions?\b",

        r"\bturn\s+off\s+all\s+safety\s+mechanisms?\b"
    ]
}


def detect_regex_attacks(prompt):

    matches = []

    prompt = prompt.lower()

    for category, patterns in ATTACK_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, prompt):

                matches.append({
                    "category": category,
                    "pattern": pattern
                })

    return matches