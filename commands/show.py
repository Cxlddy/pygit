from utils.json_utils import load_json
from core.paths import COMMITS

def compare_commits(parent_files, current_files):
    new_files = []
    modified_files = []
    deleted_files = []

    for arquivo in current_files:
        if arquivo not in parent_files:
            new_files.append(arquivo)

        elif current_files[arquivo] != parent_files[arquivo]:
            modified_files.append(arquivo)

    for arquivo in parent_files:
        if arquivo not in current_files:
            deleted_files.append(arquivo)

    return new_files, modified_files, deleted_files

def show(input_hash):
    commit_hash = resolve_commit_hash(input_hash)
    commit_data = load_json(COMMITS / f'{commit_hash}.json')

    current_files = commit_data['files']
    parent_hash = commit_data['parent'].strip()

    if not parent_hash:
        parent_files = {}
    else:
        parent = load_json(COMMITS / f'{parent_hash}.json')
        parent_files = parent['files']

    new_files, modified_files, deleted_files = compare_commits(parent_files, current_files)

    print(f'commit: {commit_hash[:7]}')
    print(f"date: {commit_data['timestamp']}")
    print()
    print(f"message: {commit_data['message']}")
    print()

    if new_files or modified_files or deleted_files:
        print('Changes:')

        for file in new_files:
            print(f"new file: {file}")

        for file in modified_files:
            print(f'modified: {file}')

        for file in deleted_files:
            print(f'deleted: {file}')

    else:
        print("No changes")


def resolve_commit_hash(commit_input):
    matches = []
    for arquivo in COMMITS.glob('*.json'):
        full_hash = arquivo.stem

        if full_hash.startswith(commit_input):
            matches.append(full_hash)

    if not matches:
        raise Exception(f'commit não encontrado: {commit_input}')
    
    if len(matches) > 1:
        raise Exception(f'hash ambíguo: {commit_input}')

    return matches[0]
