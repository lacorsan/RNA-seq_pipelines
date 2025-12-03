# RNA-seq_pipelines

This repository provides a structured collection of scripts and workflows for RNA-seq data processing and analysis, including trimming, alignment, quantification, pseudalignment, and differential expression. It also contains auxiliary tools for microarray analysis and additional utilities commonly used in NGS pipelines.

## Repository Structure
---
RNA-seq_pipelines/
│
├── 1_RNA-seq_Analysis/
│   ├── 1_Trimming/
│   │   ├── BBDuk.txt
│   │   ├── Cutadapt.txt
│   │   └── Trimmomatic.txt
│   │
│   ├── 2_Alignment/
│   │   ├── 1_Genome-based/
│   │   │   ├── Hisat2_Aligner.txt
│   │   │   ├── STAR_Aligner.txt
│   │   │   └── TopHat2_Aligner.txt
│   │   ├── 2_Transcriptome-based/
│   │   │   ├── Bowtie2_Aligner.txt
│   │   │   └── STAR_Aligner_Transcriptome.txt
│   │   └── 3_Hybrid/
│   │       └── RUM_Aligner.txt
│   │
│   ├── 3_Counting_&_Normalization/
│   │   ├── Script_Cufflinks.txt
│   │   ├── Script_HTSeq-INTER_Count.txt
│   │   ├── Script_HTSeq-UNION_Count.txt
│   │   ├── Script_RSEM.txt
│   │   ├── Script_Stringtie.txt
│   │   └── Script_eXpress.txt
│   │
│   ├── 4_Pseudoalignment/
│   │   ├── Kallisto_PseudoAligner.txt
│   │   ├── Sailfish_Pseudoaligner.txt
│   │   └── Salmon_Pseudoaligner.txt
│   │
│   └── 5_Differential_expression/
│       ├── Negative-Binomial/
│       │   ├── BaySeq_Script.txt
│       │   ├── Cuffdiff.txt
│       │   ├── DESeq2_Script.txt
│       │   ├── EBSeq_Script.txt
│       │   └── edgeR_Script.txt
│       ├── Non-Parametric_methods/
│       │   ├── NOISeq_Script.txt
│       │   └── SAMSeq_samr.txt
│       └── log-normal/
│           ├── Ballgown.txt
│           └── Limma_Script.txt
│
├── 2_Microarray_Analysis/
│   └── Oligo_Pck_CustomCDF.txt
│
└── 3_Miscellaneous/
    ├── AddN_to_fastq/
    │   ├── AddN_to_fastq_(Script).txt
    │   └── addN.py
    ├── Dunn_test/
    │   └── Dunn_post-hoc_Test.txt
    ├── fastqc/
    │   └── fastqc_script.txt
    ├── picard/
    │   ├── picard-tools_Alignment_Summary.txt
    │   └── picard-tools_CollectInsertSize.txt
    └── samtools/
        ├── Samtools_Extract_Mapped_Reads.txt
        └── Samtools_Reheader_BAM.txt
---


---

## 🧬 RNA-seq Workflow Overview

A typical RNA-seq analysis workflow supported by this repository includes:

1. **Quality trimming & adapter removal**  
   Tools: `BBDuk`, `Cutadapt`, `Trimmomatic`

2. **Read alignment (genome, transcriptome, or hybrid-based)**  
   Tools: `Hisat2`, `STAR`, `TopHat2`, `Bowtie2`, `RUM`

3. **Read quantification & normalization**  
   Tools: `HTSeq`, `RSEM`, `StringTie`, `Cufflinks`, `eXpress`

4. **Pseudalignment approaches**  
   Tools: `Kallisto`, `Salmon`, `Sailfish`

5. **Differential expression analysis**
   - Negative binomial: `DESeq2`, `edgeR`, `EBSeq`, `Cuffdiff`, `BaySeq`
   - Non-parametric: `NOISeq`, `SAMseq`
   - Log-normal: `Limma`, `Ballgown`

---

## 🧪 Microarray Analysis

Scripts for processing microarray data using Custom CDFs and the `oligo` package.

---

## 🔧 Miscellaneous Tools

Additional helper utilities for:
- Adding N bases to FASTQ reads
- Quality control using `fastqc`
- Basic BAM handling via `samtools` & `picard`
- Non-parametric statistical testing (Dunn’s test)

---

## 📌 Notes

- Scripts may require adaptation depending on program versions, HPC environment, or species annotations.
- Please check tool documentation for installation and system requirements.

---










