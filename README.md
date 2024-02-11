# Organizador de Arquivos

Este é um pequeno script em Python que organiza os arquivos em uma determinada pasta de acordo com sua extensão e data de criação. Ele categoriza os arquivos em pastas separadas por tipo (Imagens, Arquivos, Vídeos e Outros) e dentro de cada tipo, organiza-os em subpastas por mês e ano de criação.

## Funcionalidades

- Organização automática de arquivos em subpastas por tipo e data de criação.
- Suporte para diferentes tipos de arquivos, incluindo imagens, documentos, vídeos e outros.
- Utiliza a biblioteca tqdm para exibir uma barra de progresso durante o processo de organização.

## Como Usar

1. Execute o script `organizador_de_arquivos.py`.
2. Insira o caminho da pasta raiz que contém os arquivos que deseja organizar.
3. Insira o caminho da pasta de destino onde deseja que os arquivos sejam organizados.
4. Aguarde enquanto o script organiza os arquivos. Uma barra de progresso será exibida para acompanhar o progresso.
5. Após a conclusão, os arquivos serão organizados na estrutura de pastas especificada.

## Requisitos

- Python 3.x
- Bibliotecas Python: `os`, `shutil`, `datetime`, `tqdm`
- Para instalar a biblioteca tqdm:
  ```pip install tqdm```
