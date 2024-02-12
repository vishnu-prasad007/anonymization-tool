# A list of predefined patterns
patterns = [ 
    {"label": "CAR_PLATE", "pattern": r"[A-Z]{2,3}\s\d{1,4}"},  # ABC 123 or XYZ 4567
    {"label": "CAR_PLATE", "pattern": r"[A-Z]{2,3}-\d{1,4}"},  # ABC-123 or XYZ-4567
    {"label": "SOCIAL_SECURITY_NUMBER", "pattern": r"\b\d{3}-\d{2}-\d{4}\b"},  
    {"label": "CREDIT_CARD", "pattern": r"\b(?:\d[ -]*?){13,16}\b"},
    {"label": "PASSPORT", "pattern":  r"\b[A-Z]{1,3}\d{3,8}\b"}
]