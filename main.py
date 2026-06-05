import sys
from commands.init import init_repository
from commands.add import add
from commands.commit import commit
from commands.status import status
from commands.log import log
from commands.show import show



command = sys.argv[1]
if len(sys.argv) < 2:
    print("o pygit não entendeu seu comando :/")

if command == 'init':
    init_repository()

if command == 'add':
    add(sys.argv[2])
    print("o pygit guardou seu(s) arquivo(s)")
    
if command == 'commit':
    commit(sys.argv[2])
    print("pygit salvou sua commit com sucesso! (e gostou muito do nome dela)")
    
if command == 'status':
    status()

if command == 'log':
    log()

if command == 'show':
    show(sys.argv[2])

if command == 'help':
    print(f'Commands:\ninit - inicia seu repositório\nadd [arg] adiciona um arquivo ao seu repo (add . adiciona tudo)\ncommit - cria uma commit\nstatus - mostra os arquivos a serem commitados\nlog - mostra as commits\nshow [arg]- mostra uma commit especifica')
    

    