import json

# Caminho do arquivo JSON em UTF-16
input_file = 'website/fixtures/dados.json'
output_file = 'website/fixtures/dados_website_utf8.json'

with open(input_file, 'r', encoding='utf-16') as f_in:
    data = json.load(f_in)

with open(output_file, 'w', encoding='utf-8') as f_out:
    json.dump(data, f_out, ensure_ascii=False, indent=4)

print("Conversão utf16 para utf8 realizada com sucesso!")
