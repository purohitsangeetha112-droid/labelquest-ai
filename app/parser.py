import re

def extract_nutrition(raw_text):
    data = {"calories": 0, "sugar": 0, "sodium": 0, "fat": 0, "satFat": 0, "protein": 0}
    lines = raw_text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        
        # Helper: Look for a keyword, and grab the FIRST number that appears AFTER the keyword
        def get_num_after(text, keyword):
            # This regex finds the keyword, allows any text/letters/slashes after it, then grabs the number
            m = re.search(rf'{keyword}.*?([0-9]+(?:\.[0-9]+)?)', text)
            return float(m.group(1)) if m else 0.0

        # Calories
        if 'calorie' in line_lower and data['calories'] == 0:
            data['calories'] = int(get_num_after(line_lower, 'calorie'))
            
        # Sugar
        if 'sugar' in line_lower and data['sugar'] == 0:
            data['sugar'] = get_num_after(line_lower, 'sugar')
            
        # Sodium
        if 'sodium' in line_lower and data['sodium'] == 0:
            data['sodium'] = int(get_num_after(line_lower, 'sodium'))
            
        # Fat
        if 'saturat' in line_lower and 'fat' in line_lower:
            if data['satFat'] == 0: data['satFat'] = get_num_after(line_lower, 'saturat')
        elif 'fat' in line_lower:
            if 'total' in line_lower or 'lipides' in line_lower:
                if data['fat'] == 0: data['fat'] = get_num_after(line_lower, 'fat')

        # Protein
        if 'protein' in line_lower and data['protein'] == 0:
            data['protein'] = get_num_after(line_lower, 'protein')
            
    return data

def extract_servings(text: str):
    lines = text.split('\n')
    for line in lines:
        if 'serving' in line.lower() and ('per' in line.lower() or 'container' in line.lower()):
            m = re.search(r'([0-9]+)', line)
            if m and int(m.group(1)) <= 20:
                return int(m.group(1))
    return 1

ALLERGENS = {
    "Milk": ["milk", "dairy", "whey", "casein"],
    "Wheat": ["wheat", "maida", "gluten", "atta", "flour"],
    "Soy": ["soy", "soya"],
    "Peanut": ["peanut", "groundnut"],
    "Egg": ["egg", "albumin"],
    "Tree Nuts": ["almond", "cashew", "pista", "walnut"],
}

def detect_allergens(text: str):
    low = text.lower()
    return [name for name, kws in ALLERGENS.items() if any(kw in low for kw in kws)]

def extract_ingredients(text: str):
    m = re.search(r"ingredients?\s*[:\-]?\s*(.+)", text, re.IGNORECASE | re.DOTALL)
    if not m: return []
    raw = m.group(1)
    raw = re.split(r"nutrition|typical\s+values", raw, flags=re.IGNORECASE)[0]
    parts = re.split(r"[,;•\n]", raw)
    return [p.strip(" .") for p in parts if 2 < len(p.strip()) < 60][:15]

def parse_label(raw_text: str, product_name: str = "Scanned Product"):
    nutrients = extract_nutrition(raw_text)
    return {
        "emoji": "📦", "name": product_name, "servings": extract_servings(raw_text),
        "perServing": nutrients, "allergens": detect_allergens(raw_text),
        "ingredients": extract_ingredients(raw_text), "rawText": raw_text,
    }