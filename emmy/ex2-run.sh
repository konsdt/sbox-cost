#!/bin/bash
#SBATCH --partition=standard96
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=8:00:00

set -euo pipefail

/home/nwmdietr/miniconda3/bin/python data_collection_SBOX_ng.py
