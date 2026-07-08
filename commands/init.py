import sys
import json
from pygit.core.paths import REPO, COMMITS, OBJECTS, HEAD, INDEX

def init_repository():
    command = sys.argv[1]
    if len(sys.argv) < 2:
        print("o pygit não entendeu seu comando :/")

    if command == 'init':
        REPO.mkdir(exist_ok=True)
        OBJECTS.mkdir(exist_ok=True)
        COMMITS.mkdir(exist_ok=True)
        data = {}
        with open(INDEX, 'w') as f:
            json.dump(data, f)
        HEAD.write_text('')
        print("Repositório Criado com sucesso")