from app.parser import parse_label
import json

sample = """
Ingredients: Wheat flour, Sugar, Milk solids, Salt.
Nutrition: Energy 150 kcal, Sugars 12 g, Sodium 180 mg, Saturated fat 4 g, Protein 2 g.
Servings per pack: 3
"""

result = parse_label(sample)
print(json.dumps(result, indent=2))