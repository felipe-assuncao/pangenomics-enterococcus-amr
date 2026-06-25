import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sys.setrecursionlimit(40000)
bancos = ['card', 'vfdb', 'bacmet']

print("🚀 Iniciando a Renderização Gráfica Premium do Pangenoma...\n")

for banco in bancos:
    arquivo_entrada = f'matriz_{banco}_global.csv'
    arquivo_saida = f'Heatmap_{banco.upper()}_Global.pdf'
    
    print(f"-> Processando banco: {banco.upper()}...")
    
    if not os.path.exists(arquivo_entrada):
        print(f"   [Erro] Arquivo {arquivo_entrada} nao encontrado.\n")
        continue
        
    df = pd.read_csv(arquivo_entrada, index_col=0)
    df_binario = (df > 0).astype(int)
    
    print("   - Calculando Clustering Hierárquico...")
    
    grafico = sns.clustermap(df_binario, 
                             cmap="Reds",
                             figsize=(20, 14),
                             yticklabels=False,
                             xticklabels=True,
                             dendrogram_ratio=0.15,
                             cbar_pos=None # Isso desliga o termômetro (colorbar)
                             )
    
    # Reduz a fonte dos genes para tamanho 5 e gira o texto em 90 graus (em pé)
    plt.setp(grafico.ax_heatmap.get_xticklabels(), rotation=90, fontsize=5)
    
    grafico.fig.suptitle(f'Perfil Pangenômico Global - Banco {banco.upper()}', fontsize=22, y=1.03)
    grafico.savefig(arquivo_saida, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   [OK] Gráfico limpo salvo em: {arquivo_saida}\n")

print("🏆 Lapidação concluída!")
