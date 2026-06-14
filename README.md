# Massive-Scale Pangenomics and AMR Evolution in Enterococcus 🧬💻

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Bash](https://img.shields.io/badge/bash-scripting-green.svg)
![Data](https://img.shields.io/badge/dataset-13k_genomes-orange.svg)
![Status](https://img.shields.io/badge/status-active_processing-brightgreen.svg)

## 📌 Project Overview
*Enterococcus* species are leading causes of nosocomial infections globally, heavily driven by the rapid acquisition of Antimicrobial Resistance (AMR), such as Vancomycin-Resistant Enterococci (VRE). 

This project aims to map the evolutionary landscape of the resistome, virulome, and heavy metal resistance across a massive cohort of **13,000 publicly available *Enterococcus* genomes** from the NCBI. To process Big Data at this scale, we deployed an automated, high-performance computing (HPC) pipeline utilizing customized data-curation scripts and parallelized execution batches.

## 🛠️ Computational Architecture & Pipeline

Processing 13k genomes requires robust handling of heterogeneous public metadata. The pipeline follows a structured workflow:

1. **Data Acquisition:** Genomes are downloaded in systematic batches of 1,000 via NCBI Datasets CLI.
2. **Metadata Curation (The "Vaccine"):** Legacy or pseudogene-heavy genomes often lack proper translation tags (`/protein_id`), causing downstream validators to crash. We developed a custom `Biopython` script (`limpa_genomas.py`) to dynamically parse, clean, and inject compliant metadata tags, ensuring 100% genome retention.
3. **Core Processing:** We utilize the **PanViTa** pipeline to map features against leading databases:
   - **CARD** (Comprehensive Antibiotic Resistance Database)
   - **VFDB** (Virulence Factor Database)
   - **BacMet** (Antibacterial Biocide and Metal Resistance Database)
4. **HPC Execution:** Jobs are managed asynchronously via `nohup` in a Linux cluster environment to optimize CPU/RAM usage.

*(Flowchart of the architecture will be added here)*

## 📂 Repository Structure

```text
├── DB/                 # Core databases (CARD, VFDB, BacMet) formatted for DIAMOND Blastp
├── listas_ncbi/        # NCBI Accession ID lists divided by 1k batches
├── limpa_genomas.py    # Custom Biopython metadata curation script
└── panvita.py          # Main pipeline executable


🔬 Author & Acknowledgments
Researcher: Felipe Assunção
B.Sc. student in Information Technology (transitioning to Computer Science) | UFRN, Brazil.
Advisor: Prof. Dr. Tetsu
Software Credit: The core mapping pipeline is based on PanViTa (Pangenome, Virulome, and Antimicrobial Resistance), originally developed by D. L. N. Rodrigues et al. (2023).
📄 Citation: 10.3389/fbinf.2023.1070406
