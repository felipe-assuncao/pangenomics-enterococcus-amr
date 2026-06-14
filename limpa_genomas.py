import glob
from Bio import SeqIO

# Busca dinamicamente todos os arquivos .gbf da pasta atual
arquivos = glob.glob("*.gbf")
print(f"Analisando {len(arquivos)} arquivos de genoma...")

erros_encontrados = 0

for caminho in arquivos:
    modificado = False
    try:
        records = list(SeqIO.parse(caminho, "genbank"))
        for record in records:
            for feature in record.features:
                if feature.type == "CDS":
                    # Se o gene não tiver a tag protein_id (comum em arquivos antigos/pseudogenes),
                    # o PanViTa quebra. Vamos corrigir criando um ID baseado no locus_tag.
                    if "protein_id" not in feature.qualifiers:
                        locus = feature.qualifiers.get("locus_tag", ["gene_antigo"])[0]
                        feature.qualifiers["protein_id"] = [f"fixed_{locus}"]
                        modificado = True
        
        if modificado:
            SeqIO.write(records, caminho, "genbank")
            print(f"-> {caminho} continha inconformidades e foi corrigido com sucesso!")
            erros_encontrados += 1
            
    except Exception as e:
        print(f"Erro crítico ao ler o arquivo {caminho}: {e}")

print(f"\nVarredura concluída! Total de genomas corrigidos e salvos: {erros_encontrados}")
