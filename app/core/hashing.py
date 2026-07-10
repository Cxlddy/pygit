import hashlib
from pathlib import Path

def generate_hash(content: bytes) -> str:
    return hashlib.sha1(content).hexdigest()

def hash_file(path: Path) -> str:
    conteudo = path.read_bytes()
    return generate_hash(conteudo)