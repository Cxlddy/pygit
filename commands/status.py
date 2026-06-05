from pathlib import Path
from core.hashing import hash_file
from core.paths import COMMITS, HEAD, INDEX
from core.ignore import discover_files
from utils.json_utils import load_json

def raiz_repo():
    pasta_atual = Path.cwd()

    while True:
        if (pasta_atual / ".pygit").exists():
            return pasta_atual

        if pasta_atual == pasta_atual.parent:
            raise Exception("não é um repositório pygit")

        pasta_atual = pasta_atual.parent

def atual_stats():
    repo = raiz_repo()
    files = {}  
    for arquivo in discover_files():
        file_hash = hash_file((repo / arquivo))
        files[str(arquivo)] = file_hash

    return files

def status():
    with open(HEAD, 'r', encoding='utf-8') as f:
        last_commit = f.read().strip()
    if not last_commit:
        commit_files = {}
    else:
        commit_data = load_json(COMMITS / f'{last_commit}.json')
        commit_files = commit_data['files']
    
    index = load_json(INDEX)
    atual = atual_stats()
    
    staged_new = []
    staged_modified = []
    staged_deleted = []

    unstaged_modified = []
    unstaged_deleted = []
    untracked = []

    
    for arquivo in index:
        if arquivo not in commit_files:
            staged_new.append(arquivo)
        elif index[arquivo] != commit_files[arquivo]:
            staged_modified.append(arquivo)

    for arquivo in commit_files:
        if arquivo not in index:
            staged_deleted.append(arquivo)

    for arquivo in atual:
        if arquivo not in index:
            untracked.append(arquivo)
        elif atual[arquivo] != index[arquivo]:
            unstaged_modified.append(arquivo)

    for arquivo in index:
        if arquivo not in atual:
            unstaged_deleted.append(arquivo)
    
    if staged_new or staged_modified or staged_deleted:
        print("Changes to be committed:")

        for arquivo in staged_new:
            print(f"  new file: {arquivo}")

        for arquivo in staged_modified:
            print(f"  modified: {arquivo}")

        for arquivo in staged_deleted:
            print(f"  deleted: {arquivo}")

    if unstaged_modified or unstaged_deleted:
        print("\nChanges not staged for commit:")

        for arquivo in unstaged_modified:
            print(f"  modified: {arquivo}")

        for arquivo in unstaged_deleted:
            print(f"  deleted: {arquivo}")

    if untracked:
        print("\nUntracked files:")

        for arquivo in untracked:
            print(f"  {arquivo}")

    if not (
        staged_new
        or staged_modified
        or staged_deleted
        or unstaged_modified
        or unstaged_deleted
        or untracked
    ):
        print("nothing to commit, working tree clean")
        
