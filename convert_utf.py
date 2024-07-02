import chardet

"""
# Ler os bytes do arquivo para detectar a codificação
with open('website/fixtures/dados_website.json', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)

# Resultado da detecção da codificação
print(result['encoding'])

# Abrir o arquivo com a codificação detectada
with open('website/fixtures/dados_website.json', 'r', encoding=result['encoding']) as f:
    content = f.read()
    print(content)
"""

import json

# Caminho do arquivo JSON em UTF-16
input_file = 'website/fixtures/dados_website.json'
output_file = 'website/fixtures/dados_website_utf8.json'

with open(input_file, 'r', encoding='utf-16') as f_in:
    data = json.load(f_in)

with open(output_file, 'w', encoding='utf-8') as f_out:
    json.dump(data, f_out, ensure_ascii=False, indent=4)

"""
import json

def corrigir_caracteres(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    # Substituições específicas para corrigir os caracteres especiais
    correcoes = {
        '├¡': 'í',
        '├┤': 'ô',
        '├¬': 'ê',
        '├í': 'í',
        '├®': 'é',
        '├�': 'Ó',
        '├º': 'ç',
        '├ú': 'ã',
        '├Á': 'õ',
        '├': 'á',
        '├ü': 'Á',
    }

    # Aplica as correções no texto
    for incorreto, correto in correcoes.items():
        data = data.replace(incorreto, correto)

    # Corrige casos específicos onde há a sequência "ções" seguida de caracteres indesejados
    data = data.replace('ções ', 'ção ')

    # Salva o arquivo corrigido
    with open('website/fixtures/dados_corrigidos.json', 'w', encoding='utf-8') as output_file:
        output_file.write(data)

    print(f'Arquivo corrigido salvo como "dados_corrigidos.json".')

# Substitua 'website/fixtures/dados_website_utf8.json' pelo nome do seu arquivo JSON
corrigir_caracteres('website/fixtures/dados_website_utf8.json')
"""
