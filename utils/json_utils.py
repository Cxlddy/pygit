import json
from pathlib import Path

def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_json(data, path: Path):
    with open(path, 'w', encoding='utf-8') as f:
        return json.dump(data, f)