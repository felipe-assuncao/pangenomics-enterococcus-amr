# 📓 Computational Lab Notebook

This notebook logs chronological tasks, workflow updates, and troubleshooting performed during the 13k *Enterococcus* pangenome research.

### 📅 June 15, 2026
- **Task:** Annotation and metadata mapping for the initial 87-genome testing cohort.
- **Action:** Utilized NCBI Datasets CLI to fetch complete taxonomic metadata (`resumo_87.jsonl`) for the legacy GCF accession numbers. Developed a custom Python parsing script (`gera_tabela_iniciais.py`) to map and extract full species/strain identifiers into a structured CSV dataset (`tabela_87_iniciais.csv`).
- **Pipeline Progress:** Active tracking enabled for **Batch 13** (the final lot of the massive data acquisition phase).

### 📅 June 16, 2026
- **Task:** Optimization of data extraction and formatting for downstream analysis.
- **Action:** Upgraded the metadata parsing script (`gera_tabela_iniciais.py`) to employ a custom dictionary-mapping algorithm. This ensures the output CSV strictly adheres to a predefined, non-alphabetical sorting order, eliminating the need for manual row-matching and significantly reducing data-curation time.

### 📅 June 17/18, 2026
- **Task:** Massive Pangenomic Data Consolidation (13,389 Genomes).
- **Action:** Engineered a robust Python/Pandas script (`consolidar_matrizes.py`) to parse and fuse distributed outputs from the 13 computational batches. Addressed PanViTa's native formatting anomalies (trailing delimiters, non-standard separators) via Regex and index-anchoring.
- **Output:** Successfully generated a definitive Sparse Matrix for the global *Enterococcus* resistome/virulome, identifying 240 unique AMR genes (CARD) and 280 virulence factors (VFDB) across the entire dataset without altering raw computational backups.
- **Milestone:** Big Data processing phase officially concluded. Data extracted for downstream statistical rendering.

### 📅 June 19/25, 2026
- **Task:** Pangenome Visual Analytics and Figure Optimization.
- **Action:** Engineered a Python visualization pipeline utilizing `seaborn.clustermap` to render the global sparse matrices. Applied a binary transformation threshold (0 = absence, 1 = presence) to establish high-contrast clinical interpretation of the resistome/virulome. Executed hierarchical clustering (Euclidean distance) across all 13,389 genomes, expanding Python's native recursion limits to render deep phylogenetic branching. 
- **Refinement:** Optimized figure aesthetics for publication standards by stripping redundant colorbars and formatting x-axis gene labels (90-degree rotation, micro-font scaling) to resolve UI/UX rendering collisions.
- **Output:** Generated three publication-ready High-Resolution Clustered Heatmaps (CARD, VFDB, BACMET) revealing distinct co-occurrence gene blocks and core virulome patterns.
- **Milestone:** Data Visualization pipeline officially established, containerized locally, and synchronized with the remote GitHub repository.
