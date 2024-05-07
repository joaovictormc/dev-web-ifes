import os
import zipfile

if not os.path.exists('Textos'):
    os.makedirs('Textos')

nomes_arquivos = ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']

for nome_arquivo in nomes_arquivos:
    with open(os.path.join('Textos', nome_arquivo), 'w') as arquivo:
        arquivo.write('Python Essencial')

with zipfile.ZipFile('Textos.zip', 'w') as zipf:
    for root, dirs, files in os.walk('Textos'):
        for file in files:
            zipf.write(os.path.join(root, file))

print('Diretório, arquivos e arquivo compactado criados com sucesso!')
