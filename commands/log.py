from utils.json_utils import load_json
from core.paths import HEAD, COMMITS


def log():
    commit_hash = HEAD.read_text().strip()

    while commit_hash:
        commit_data = load_json(COMMITS / f'{commit_hash}.json')

        print(f"commit {commit_hash[:7]}")
        print(f"Date: {commit_data['timestamp']}")
        print()
        print(f"    {commit_data['message']}")
        print()

        commit_hash = commit_data['parent'].strip()