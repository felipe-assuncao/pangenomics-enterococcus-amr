import os
import glob
import pandas as pd

pasta_saida = 'resultados_consolidados'
os.makedirs(pasta_saida, exist_ok=True)

bancos = ['card', 'vfdb', 'bacmet']
print("Iniciando a Fusão de Dados Massiva (Read-Only nos originais)...\n")

for banco in bancos:
    print(f"-> Processando banco: {banco.upper()}...")
    
    padrao_busca = f"lotes_concluidos/lote_*_concluido/Results_{banco}_*/matriz_{banco}.csv"
    arquivos = glob.glob(padrao_busca)
    
    if not arquivos:
        print(f"   [Aviso] Nenhuma matriz encontrada para {banco.upper()}.\n")
        continue
        
    lista_dfs = []
    for arquivo in arquivos:
        # 1. Avisamos o Python que o separador é o ponto e vírgula
        df = pd.read_csv(arquivo, index_col=0, sep=';')
        lista_dfs.append(df)
        
    df_final = pd.concat(lista_dfs, axis=0).fillna(0)
    
    # 2. Limpamos a "coluna fantasma" gerada pelo último ; da linha
    df_final = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
    
    caminho_saida = os.path.join(pasta_saida, f"matriz_{banco}_global.csv")
    df_final.to_csv(caminho_saida)
    
    print(f"   [OK] Matriz {banco.upper()} concluída e salva em: {caminho_saida}")
    print(f"   - Total de genomas: {df_final.shape[0]}")
    print(f"   - Total de genes únicos encontrados: {df_final.shape[1]}\n")

print("🚀 Consolidação concluída com sucesso! Os dados originais continuam intactos.")
