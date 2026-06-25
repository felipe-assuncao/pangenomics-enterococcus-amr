import json
import csv

arquivo_lista = 'lista_87_iniciais.txt'
arquivo_json = 'resumo_87.jsonl'
arquivo_saida = 'tabela_87_iniciais.csv'

# 1. Ler a ordem exata que você colou no arquivo de texto
with open(arquivo_lista, 'r') as f_lista:
    ordem_desejada = [linha.strip() for linha in f_lista if linha.strip()]

# 2. Criar um dicionário na memória com os dados que vieram do NCBI
dados_ncbi = {}
with open(arquivo_json, 'r') as f_in:
    for line in f_in:
        data = json.loads(line)
        accession = data.get('accession', 'Unknown')
        organism = data.get('organism', {})
        organism_name = organism.get('organism_name', 'Enterococcus sp.')
        
        infraspecific = organism.get('infraspecific_names', {})
        strain = infraspecific.get('strain', '')
        
        if strain and strain not in organism_name:
            nome_final = f"{organism_name} strain {strain}"
        else:
            nome_final = organism_name
            
        dados_ncbi[accession] = nome_final

# 3. Escrever a tabela final respeitando a sua ordem original
with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['Organism_Name'])
    
    for acc in ordem_desejada:
        # Puxa o nome correspondente. Se o NCBI falhar em algum, ele avisa na tabela.
        nome = dados_ncbi.get(acc, "Nome nao encontrado")
        writer.writerow([nome])

print("Sucesso! Tabela gerada na ordem exata da sua lista original.")
