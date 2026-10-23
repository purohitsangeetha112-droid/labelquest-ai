RULES = {
    "sugar":  {"red": 10,  "yellow": 5},   
    "sodium": {"red": 300, "yellow": 150}, 
    "fat":    {"red": 15,  "yellow": 5},   
    "satFat": {"red": 2,   "yellow": 1},   
}

def level(value, rule):
    if value is None: return "green"
    if value >= rule["red"]: return "red"
    if value >= rule["yellow"]: return "yellow"
    return "green"

def product_score(per_serving):
    levels = [
        level(per_serving.get("sugar"),  RULES["sugar"]),
        level(per_serving.get("sodium"), RULES["sodium"]),
        level(per_serving.get("fat"),    RULES["fat"]),
        level(per_serving.get("satFat"), RULES["satFat"]),
    ]
    if "red" in levels:    return "red"
    if "yellow" in levels: return "yellow"
    return "green"