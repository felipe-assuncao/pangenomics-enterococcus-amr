import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# COMPREENSÃO DO COMANDO:
# O Python por padrão limita a árvore a 1000 ramificações para proteger o computador.
# Como temos 13.389 genomas, aumentamos o limite para 40.000 para permitir o trabalho completo.
sys.setrecursionlimit(40000)

# Lista com as três matrizes globais que extraímos do servidor
bancos = ['card', 'vfdb', 'bacmet']

print("🚀 Iniciando a Renderização Gráfica do Pangenoma Global...\n")

for banco in bancos:
    arquivo_entrada = f'matriz_{banco}_global.csv'
    arquivo_saida = f'Heatmap_{banco.upper()}_Global.pdf'
    
    print(f"-> Processando banco: {banco.upper()}...")
    
    # COMPREENSÃO DO COMANDO:
    # Verifica se o arquivo CSV realmente existe na pasta Downloads antes de tentar ler
    if not os.path.exists(arquivo_entrada):
        print(f"   [Erro] Arquivo {arquivo_entrada} nao encontrado na pasta. Pulando...\n")
        continue
        
    # COMPREENSÃO DO COMANDO:
    # index_col=0 define a coluna dos genomas (Strains) como a chave primária
    df = pd.read_csv(arquivo_entrada, index_col=0)
    
    # COMPREENSÃO DO COMANDO:
    # Transforma valores brutos do PanViTa em binário (1 para presença do gene, 0 para ausência)
    df_binario = (df > 0).astype(int)
    
    print(f"   - Total de Genomas: {df_binario.shape[0]}")
    print(f"   - Total de Genes Únicos: {df_binario.shape[1]}")
    print("   - Calculando Clustering Hierárquico (Pode demorar um pouco)...")
    
    # COMPREENSÃO DO COMANDO:
    # O clustermap faz a mágica matemática de agrupar linhas e colunas semelhantes
    grafico = sns.clustermap(df_binario, 
                             cmap="Reds",          # Vermelho para presença, Branco para ausência
                             figsize=(20, 14),     # Tamanho da imagem em polegadas (proporção de pôster)
                             yticklabels=False,    # Oculta 13 mil IDs para não virar um borrão de tinta
                             xticklabels=True,     # Exibe o nome de cada gene no eixo horizontal
                             dendrogram_ratio=0.15 # Destina 15% do espaço do quadro para desenhar as árvores
                             )
    
    # COMPREENSÃO DO COMANDO:
    # Adiciona um título dinâmico no topo do PDF com base no banco atual
    grafico.fig.suptitle(f'Perfil Pangenômico Global - Banco {banco.upper()}', fontsize=22, y=1.03)
    
    # COMPREENSÃO DO COMANDO:
    # Salva em formato vetorial PDF (300 DPI) que permite zoom infinito sem pixelar
    grafico.savefig(arquivo_saida, dpi=300, bbox_inches='tight')
    plt.close() # Limpa a memória do computador para o próximo gráfico
    
    print(f"   [OK] Gráfico salvo com sucesso em: {arquivo_saida}\n")

print("🏆 Todos os 3 mapas de calor hierárquicos foram gerados perfeitamente!")
