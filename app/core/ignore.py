from pathlib import Path
from fnmatch import fnmatch

def raiz_repo():
    pasta_atual = Path.cwd()

    while True:
        if (pasta_atual / ".pygit").exists():
            return pasta_atual

        if pasta_atual == pasta_atual.parent:
            raise Exception("não é um repositório pygit")

        pasta_atual = pasta_atual.parent

def load_pygitignore():
    repo = raiz_repo()
    pygitignore = repo / ".pygitignore"

    regras = []

    if not pygitignore.exists():
        return regras

    conteudo = pygitignore.read_text(encoding="utf-8")
    linhas = conteudo.splitlines()

    for linha in linhas:
        linha = linha.strip()

        if linha == "":
            continue

        if linha.startswith("#"):
            continue

        linha = linha.replace("\\", "/")
        regras.append(linha)

    return regras

def is_ignored(arquivo: Path, regras: list[str]) -> bool:
    arquivo_str = str(arquivo).replace("\\", "/")

    for regra in regras:

        if regra.endswith("/"):
            if arquivo_str.startswith(regra):
                return True

            pasta = regra.rstrip('/')
            if pasta in arquivo.parts:
                return True
    
        else:
            if fnmatch(arquivo.name, regra):
                return True
            
            if fnmatch(arquivo_str, regra):
                return True
            
    return False

def discover_files():
    repo = raiz_repo()
    regras = load_pygitignore()
    arquivos = []

    for item in repo.rglob("*"):

        if not item.is_file():
            continue
        if '.pygit' in item.parts:
            continue
            
        arquivo_relativo = item.relative_to(repo)

        if is_ignored(arquivo_relativo, regras):
            continue

        arquivos.append(arquivo_relativo)

    return arquivos








    