import json
raw = """{
"name": "John Smith",
"age": "35",
"occupation": "Data Scientist",
"city": "Kigali",
"research_area": "AI research on crop yield prediction"
}"""
# If the model wrapped JSON in ```json ... ```, remove the fences first.
raw = raw.strip()
if raw.startswith("```"):
    raw = raw.strip("`")
    raw = raw.replace("json", "", 1).strip()
data = json.loads(raw)
print(data["name"])
print(data["research_area"])