import os

# Defina o caminho da pasta 'src'
src_dir = 'src'

# Verifica se o diretório 'src' existe
if not os.path.exists(src_dir):
    os.makedirs(src_dir)

# Caminho do arquivo __init__.py
init_file = os.path.join(src_dir, '__init__.py')

# Cria o arquivo __init__.py se ele não existir
if not os.path.exists(init_file):
    with open(init_file, 'w') as f:
        pass  # Cria um arquivo vazio

print(f"Arquivo {init_file} criado com sucesso.")
