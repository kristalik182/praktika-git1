import json
import os
DATA_FILE = "habits.json"
def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
def save_habits(habits):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(habits, f, ensure_ascii=False, indent=2)
