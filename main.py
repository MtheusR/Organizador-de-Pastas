import os
import shutil
from datetime import datetime

# Função para obter a data de modificação do arquivo
def get_file_date(file_path):
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp)

# Função para criar a estrutura de pastas
def create_folder_structure(root_folder):
    organizer_folder = os.path.join(os.path.dirname(root_folder), 'Organizer')
    os.makedirs(organizer_folder, exist_ok=True)

    folders = ['Imagens', 'Arquivos', 'Vídeos', 'Outros']
    for folder in folders:
        os.makedirs(os.path.join(organizer_folder, folder), exist_ok=True)

# Função para organizar os arquivos
def organize_files(root_folder):
    organizer_folder = os.path.join(os.path.dirname(root_folder), 'Organizer')

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if os.path.isfile(file_path):
                # Obter a data de modificação do arquivo
                file_date = get_file_date(file_path)
                # Obter o mês e ano da data de modificação
                folder_name = file_date.strftime('%b-%Y')
                # Obter a extensão do arquivo
                file_extension = os.path.splitext(filename)[1][1:].lower()

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
                shutil.move(file_path, os.path.join(destination_folder, filename))

    # Excluir as pastas anteriores
    shutil.rmtree(root_folder, ignore_errors=True)

# Diretório raiz onde estão os arquivos a serem organizados
root_folder = 'D:\Documentos\Download'

# Criar a estrutura de pastas
create_folder_structure(root_folder)

# Organizar os arquivos
organize_files(root_folder)
