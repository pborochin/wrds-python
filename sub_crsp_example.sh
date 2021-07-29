#!/bin/bash
#$ -cwd
#$ -pe onenode 1
#$ -l m_mem_free=48G
python3 load_crsp_example.py &> output_log.txt