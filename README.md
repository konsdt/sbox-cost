# SBOX
SBOX-COST is a version of the BBOB suite for single-objective, continuous, noiseless optimization (minimization). It consists of the same 24 base functions, but with changed instance generation mechanism. This allows the optimum of most problems to be located anywhere in the domain ([-5,5]^n), instead of [-4,4]^n as done in the original BBOB. In addition, points outside the domain are considered infeasible, and therefore given function value of infinity. 

The suite can be accessed using COCO (see branch suite-sbox on https://github.com/sbox-cost/coco) in the same way as the regular BBOB suite, or using IOHprofiler. 

# Examples
This repository contains some examples of using the SBOX-COST suite in IOHexperimenter. 

The file "Example.ipnb" provides a getting-started guide on using the suite, while the "data_collection_SBOX_cma.py" contains code for a full-scale experiment using several versions of the CMA-ES algorithm.
