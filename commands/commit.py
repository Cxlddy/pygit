import json
from datetime import datetime
from core.hashing import generate_hash
from utils.json_utils import load_json, save_json
from core.paths import REPO, COMMITS, OBJECTS, HEAD, INDEX

def commit(message: str):
    files = load_json(INDEX)
    
    with open(HEAD, 'r', encoding='utf-8') as f:
        head = f.read().strip()

    commit_data = {
        'message': message,
        'timestamp': datetime.now().isoformat(),
        'parent': head,
        'files': files
    }
    commit_hash = generate_hash(json.dumps(commit_data).encode())
    save_json(
        commit_data,
        COMMITS / f'{commit_hash}.json'
    )
    HEAD.write_text(commit_hash)