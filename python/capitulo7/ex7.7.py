import os

if not os.path.exists('temp'):
    os.makedirs('temp')

with open('temp/temp.txt', 'w') as file:
    file.write('Este é um arquivo temporário.')

print('Diretório e arquivo criados com sucesso!')
