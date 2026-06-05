from pathlib import Path
from datetime import datetime
from core.hashing import hash_file
from core.ignore import discover_files
from core.paths import REPO, COMMITS, OBJECTS, HEAD, INDEX
from utils.json_utils import load_json, save_json


def add_file(path: Path):
    hash_arquivo = hash_file(path)
    dados = load_json(INDEX)
    
    dados[str(path)] = hash_arquivo
    save_json(dados, INDEX)

    byte = path.read_bytes()

    OBJECTS.mkdir(exist_ok=True)
    obj = (OBJECTS / hash_arquivo)
    obj.write_bytes(byte)

def add(alvo: str):
    if alvo == '.':
        for arquivo in discover_files():
            add_file(arquivo)
    else:
        add_file(Path(alvo))



    
    