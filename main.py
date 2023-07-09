import os
import shutil
from datetime import datetime
from tqdm import tqdm
from time import sleep

#Proxima att: Adicionar Icons, Mudar cor dos print, Criar executável

# # Função para obter a data de modificação do arquivo
# def get_file_date(file_path):
#     timestamp = os.path.getmtime(file_path)
#     return datetime.fromtimestamp(timestamp)

# Função para obter a data de criação do arquivo
def get_file_date(file_path):
    timestamp = os.path.getctime(file_path)
    return datetime.fromtimestamp(timestamp)


# Função para criar a estrutura de pastas
def create_folder_structure(destination_folder):
    organizer_folder = os.path.join(destination_folder, 'Organizer')
    os.makedirs(organizer_folder, exist_ok=True)

    folders = ['Imagens', 'Arquivos', 'Vídeos', 'Outros']
    for folder in folders:
        os.makedirs(os.path.join(organizer_folder, folder), exist_ok=True)

# Função para organizar os arquivos
def organize_files(root_folder, destination_folder):
    organizer_folder = os.path.join(destination_folder, 'Organizer')

    files = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if os.path.isfile(file_path):
                files.append(file_path)

    with tqdm(total=len(files), desc='Organizando arquivos') as pbar:
        for file_path in files:
            # Obter a data de modificação do arquivo
            file_date = get_file_date(file_path)
            # Obter o mês e ano da data de modificação
            folder_name = file_date.strftime('%b-%Y')
            # Obter a extensão do arquivo
            file_extension = os.path.splitext(os.path.basename(file_path))[1][1:].lower()

            # Verificar o tipo de arquivo e mover para a pasta apropriada
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                destination_folder = os.path.join(organizer_folder, 'Imagens', folder_name)
            elif file_extension in ['pdf', 'doc', 'docx', 'txt']:
                destination_folder = os.path.join(organizer_folder, 'Arquivos', folder_name)
            elif file_extension in ['mp4', 'avi', 'mov']:
                destination_folder = os.path.join(organizer_folder, 'Vídeos', folder_name)
            else:
                destination_folder = os.path.join(organizer_folder, 'Outros', folder_name)

            # Criar a pasta de destino, se necessário
            os.makedirs(destination_folder, exist_ok=True)

            # Mover o arquivo para a pasta de destino
            shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

            pbar.update(1)
            sleep(0.1)  # Simula um atraso para exibir a tela de carregamento

    # Excluir as pastas anteriores
    shutil.rmtree(root_folder, ignore_errors=True)

    print('Organização concluída com sucesso!')

# Obter o caminho da pasta raiz do usuário
root_folder = input('Digite o caminho da pasta raiz: ')

# Obter o caminho da pasta de destino do usuário
destination_folder = input('Digite o caminho da pasta de destino para a Organizer: ')

# Criar a estrutura de pastas
create_folder_structure(destination_folder)

# Organizar os arquivos
organize_files(root_folder, destination_folder)
